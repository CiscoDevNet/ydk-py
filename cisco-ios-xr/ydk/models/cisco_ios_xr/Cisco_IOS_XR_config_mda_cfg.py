""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ActiveNodes(_Entity_):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of  		 :py:class:`ActiveNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(ActiveNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "active-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("active-node", ("active_node", ActiveNodes.ActiveNode))])
        self._leafs = OrderedDict()

        self.active_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ActiveNodes, [], name, value)


    class ActiveNode(_Entity_):
        """
        The configuration for an active node
        
        .. attribute:: node_name  (key)
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: ssrp_group
        
        	Per\-node SSRP configuration data
        	**type**\:  :py:class:`SsrpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:  :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace>`
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:  :py:class:`CiscoIOSXRWatchdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:  :py:class:`CiscoIOSXRWdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:  :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:  :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface>`
        
        .. attribute:: fia_buffer_profile_cfg
        
        	fia buffer profile cfg
        	**type**\:  :py:class:`FiaBufferProfileCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.FiaBufferProfileCfg>`
        
        .. attribute:: fia_vqi_shaper_cfg
        
        	fia vqi shaper cfg
        	**type**\:  :py:class:`FiaVqiShaperCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.FiaVqiShaperCfg>`
        
        .. attribute:: port_queue_remaps
        
        	port queue remaps
        	**type**\:  :py:class:`PortQueueRemaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.PortQueueRemaps>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(ActiveNodes.ActiveNode, self).__init__()

            self.yang_name = "active-node"
            self.yang_parent_name = "active-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group", ("ssrp_group", ActiveNodes.ActiveNode.SsrpGroup)), ("Cisco-IOS-XR-infra-ltrace-cfg:ltrace", ("ltrace", ActiveNodes.ActiveNode.Ltrace)), ("Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold", ("cisco_ios_xr_watchd_cfg_watchdog_node_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold)), ("Cisco-IOS-XR-wd-cfg:watchdog-node-threshold", ("cisco_ios_xr_wd_cfg_watchdog_node_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local", ("lpts_local", ActiveNodes.ActiveNode.LptsLocal)), ("Cisco-IOS-XR-freqsync-cfg:clock-interface", ("clock_interface", ActiveNodes.ActiveNode.ClockInterface)), ("Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg", ("fia_buffer_profile_cfg", ActiveNodes.ActiveNode.FiaBufferProfileCfg)), ("Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg", ("fia_vqi_shaper_cfg", ActiveNodes.ActiveNode.FiaVqiShaperCfg)), ("Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps", ("port_queue_remaps", ActiveNodes.ActiveNode.PortQueueRemaps))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
            self.ssrp_group.parent = self
            self._children_name_map["ssrp_group"] = "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group"

            self.ltrace = ActiveNodes.ActiveNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg:watchdog-node-threshold"

            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"

            self.clock_interface = ActiveNodes.ActiveNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "Cisco-IOS-XR-freqsync-cfg:clock-interface"

            self.fia_buffer_profile_cfg = ActiveNodes.ActiveNode.FiaBufferProfileCfg()
            self.fia_buffer_profile_cfg.parent = self
            self._children_name_map["fia_buffer_profile_cfg"] = "Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg"

            self.fia_vqi_shaper_cfg = ActiveNodes.ActiveNode.FiaVqiShaperCfg()
            self.fia_vqi_shaper_cfg.parent = self
            self._children_name_map["fia_vqi_shaper_cfg"] = "Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg"

            self.port_queue_remaps = ActiveNodes.ActiveNode.PortQueueRemaps()
            self.port_queue_remaps.parent = self
            self._children_name_map["port_queue_remaps"] = "Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps"
            self._segment_path = lambda: "active-node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:active-nodes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ActiveNodes.ActiveNode, ['node_name'], name, value)


        class SsrpGroup(_Entity_):
            """
            Per\-node SSRP configuration data
            
            .. attribute:: groups
            
            	Table of SSRP Group configuration
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups>`
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.SsrpGroup, self).__init__()

                self.yang_name = "ssrp-group"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("groups", ("groups", ActiveNodes.ActiveNode.SsrpGroup.Groups))])
                self._leafs = OrderedDict()

                self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup, [], name, value)


            class Groups(_Entity_):
                """
                Table of SSRP Group configuration
                
                .. attribute:: group
                
                	SSRP Group configuration
                	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups.Group>`
                
                

                """

                _prefix = 'ppp-ma-ssrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.SsrpGroup.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "ssrp-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group", ("group", ActiveNodes.ActiveNode.SsrpGroup.Groups.Group))])
                    self._leafs = OrderedDict()

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups, [], name, value)


                class Group(_Entity_):
                    """
                    SSRP Group configuration
                    
                    .. attribute:: group_id  (key)
                    
                    	The identifier for this group
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: profile
                    
                    	This specifies the SSRP profile to use for this group
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ppp-ma-ssrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                            ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                        ])
                        self.group_id = None
                        self.profile = None
                        self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.SsrpGroup.Groups.Group, ['group_id', 'profile'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup.Groups.Group']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup.Groups']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup']['meta_info']


        class Ltrace(_Entity_):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:  :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("allocation-params", ("allocation_params", ActiveNodes.ActiveNode.Ltrace.AllocationParams))])
                self._leafs = OrderedDict()

                self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.Ltrace, [], name, value)


            class AllocationParams(_Entity_):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:  :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:  :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceMode', '')])),
                        ('scale_factor', (YLeaf(YType.enumeration, 'scale-factor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceScale', '')])),
                    ])
                    self.mode = None
                    self.scale_factor = None
                    self._segment_path = lambda: "allocation-params"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.Ltrace.AllocationParams']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.Ltrace']['meta_info']


        class CiscoIOSXRWatchdCfgWatchdogNodeThreshold(_Entity_):
            """
            watchdog node threshold
            
            .. attribute:: disk_threshold
            
            	Disk thresholds
            	**type**\:  :py:class:`DiskThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold>`
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disk-threshold", ("disk_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold)), ("memory-threshold", ("memory_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.disk_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold()
                self.disk_threshold.parent = self
                self._children_name_map["disk_threshold"] = "disk-threshold"

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, [], name, value)


            class DiskThreshold(_Entity_):
                """
                Disk thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold, self).__init__()

                    self.yang_name = "disk-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "disk-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold']['meta_info']


            class MemoryThreshold(_Entity_):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold']['meta_info']


        class CiscoIOSXRWdCfgWatchdogNodeThreshold(_Entity_):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("memory-threshold", ("memory_threshold", ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, [], name, value)


            class MemoryThreshold(_Entity_):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfgWatchdogNodeThreshold']['meta_info']


        class LptsLocal(_Entity_):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipunt_policer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpuntPolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipunt-policer-local", ("ipunt_policer_local", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal)), ("ipolicer-local-tables", ("ipolicer_local_tables", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables)), ("dynamic-flows-tables", ("dynamic_flows_tables", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables)), ("ipolicer-local", ("ipolicer_local", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal))])
                self._leafs = OrderedDict()

                self.ipunt_policer_local = None
                self._children_name_map["ipunt_policer_local"] = "ipunt-policer-local"

                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"

                self.dynamic_flows_tables = ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal, [], name, value)


            class IpuntPolicerLocal(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: punt_type_local_table
                
                	Punt Policer Table
                	**type**\:  :py:class:`PuntTypeLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable>`
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: punt_policer_domains
                
                	Punt Policer Domain Table
                	**type**\:  :py:class:`PuntPolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains>`
                
                .. attribute:: punt_policer_interface_names
                
                	Punt Policer Interface
                	**type**\:  :py:class:`PuntPolicerInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal, self).__init__()

                    self.yang_name = "ipunt-policer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("punt-type-local-table", ("punt_type_local_table", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable)), ("punt-policer-domains", ("punt_policer_domains", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains)), ("punt-policer-interface-names", ("punt_policer_interface_names", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.punt_type_local_table = ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable()
                    self.punt_type_local_table.parent = self
                    self._children_name_map["punt_type_local_table"] = "punt-type-local-table"

                    self.punt_policer_domains = ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains()
                    self.punt_policer_domains.parent = self
                    self._children_name_map["punt_policer_domains"] = "punt-policer-domains"

                    self.punt_policer_interface_names = ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames()
                    self.punt_policer_interface_names.parent = self
                    self._children_name_map["punt_policer_interface_names"] = "punt-policer-interface-names"
                    self._segment_path = lambda: "ipunt-policer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal, ['enable'], name, value)


                class PuntTypeLocalTable(_Entity_):
                    """
                    Punt Policer Table
                    
                    .. attribute:: punt_type
                    
                    	Punt Protocol Type
                    	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable, self).__init__()

                        self.yang_name = "punt-type-local-table"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-type", ("punt_type", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType))])
                        self._leafs = OrderedDict()

                        self.punt_type = YList(self)
                        self._segment_path = lambda: "punt-type-local-table"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable, [], name, value)


                    class PuntType(_Entity_):
                        """
                        Punt Protocol Type
                        
                        .. attribute:: punt_id  (key)
                        
                        	Punt Type
                        	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                        
                        .. attribute:: rate
                        
                        	Enable or Disable Punt Police and corresponding Rate in PPS
                        	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType, self).__init__()

                            self.yang_name = "punt-type"
                            self.yang_parent_name = "punt-type-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_id']
                            self._child_classes = OrderedDict([("rate", ("rate", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate))])
                            self._leafs = OrderedDict([
                                ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                            ])
                            self.punt_id = None

                            self.rate = None
                            self._children_name_map["rate"] = "rate"
                            self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType, ['punt_id'], name, value)


                        class Rate(_Entity_):
                            """
                            Enable or Disable Punt Police and corresponding
                            Rate in PPS
                            
                            .. attribute:: is_enabled
                            
                            	Is Punt Policer enabled
                            	**type**\: bool
                            
                            	**mandatory**\: True
                            
                            .. attribute:: rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate, self).__init__()

                                self.yang_name = "rate"
                                self.yang_parent_name = "punt-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                    ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ])
                                self.is_enabled = None
                                self.rate = None
                                self._segment_path = lambda: "rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable']['meta_info']


                class PuntPolicerDomains(_Entity_):
                    """
                    Punt Policer Domain Table
                    
                    .. attribute:: punt_policer_domain
                    
                    	Domain name
                    	**type**\: list of  		 :py:class:`PuntPolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains, self).__init__()

                        self.yang_name = "punt-policer-domains"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-policer-domain", ("punt_policer_domain", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain))])
                        self._leafs = OrderedDict()

                        self.punt_policer_domain = YList(self)
                        self._segment_path = lambda: "punt-policer-domains"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains, [], name, value)


                    class PuntPolicerDomain(_Entity_):
                        """
                        Domain name
                        
                        .. attribute:: domain_name  (key)
                        
                        	Domain name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: punt_type_domain_table
                        
                        	Punt Policer Table
                        	**type**\:  :py:class:`PuntTypeDomainTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain, self).__init__()

                            self.yang_name = "punt-policer-domain"
                            self.yang_parent_name = "punt-policer-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['domain_name']
                            self._child_classes = OrderedDict([("punt-type-domain-table", ("punt_type_domain_table", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable))])
                            self._leafs = OrderedDict([
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ])
                            self.domain_name = None

                            self.punt_type_domain_table = ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable()
                            self.punt_type_domain_table.parent = self
                            self._children_name_map["punt_type_domain_table"] = "punt-type-domain-table"
                            self._segment_path = lambda: "punt-policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain, ['domain_name'], name, value)


                        class PuntTypeDomainTable(_Entity_):
                            """
                            Punt Policer Table
                            
                            .. attribute:: punt_type
                            
                            	Punt Protocol Type
                            	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, self).__init__()

                                self.yang_name = "punt-type-domain-table"
                                self.yang_parent_name = "punt-policer-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("punt-type", ("punt_type", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType))])
                                self._leafs = OrderedDict()

                                self.punt_type = YList(self)
                                self._segment_path = lambda: "punt-type-domain-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, [], name, value)


                            class PuntType(_Entity_):
                                """
                                Punt Protocol Type
                                
                                .. attribute:: punt_id  (key)
                                
                                	Punt Type
                                	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                                
                                .. attribute:: rate
                                
                                	Enable or Disable Punt Police and corresponding Rate in PPS
                                	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, self).__init__()

                                    self.yang_name = "punt-type"
                                    self.yang_parent_name = "punt-type-domain-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['punt_id']
                                    self._child_classes = OrderedDict([("rate", ("rate", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate))])
                                    self._leafs = OrderedDict([
                                        ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                                    ])
                                    self.punt_id = None

                                    self.rate = None
                                    self._children_name_map["rate"] = "rate"
                                    self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, ['punt_id'], name, value)


                                class Rate(_Entity_):
                                    """
                                    Enable or Disable Punt Police and corresponding
                                    Rate in PPS
                                    
                                    .. attribute:: is_enabled
                                    
                                    	Is Punt Policer enabled
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: rate
                                    
                                    	Configured rate value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, self).__init__()

                                        self.yang_name = "rate"
                                        self.yang_parent_name = "punt-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                        ])
                                        self.is_enabled = None
                                        self.rate = None
                                        self._segment_path = lambda: "rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains']['meta_info']


                class PuntPolicerInterfaceNames(_Entity_):
                    """
                    Punt Policer Interface
                    
                    .. attribute:: punt_policer_interface_name
                    
                    	Pre\-ifib Punt Policer Interface Configuration
                    	**type**\: list of  		 :py:class:`PuntPolicerInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames, self).__init__()

                        self.yang_name = "punt-policer-interface-names"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-policer-interface-name", ("punt_policer_interface_name", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName))])
                        self._leafs = OrderedDict()

                        self.punt_policer_interface_name = YList(self)
                        self._segment_path = lambda: "punt-policer-interface-names"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames, [], name, value)


                    class PuntPolicerInterfaceName(_Entity_):
                        """
                        Pre\-ifib Punt Policer Interface Configuration
                        
                        .. attribute:: punt_interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: punt_type_interface_table
                        
                        	Punt Policer Table
                        	**type**\:  :py:class:`PuntTypeInterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, self).__init__()

                            self.yang_name = "punt-policer-interface-name"
                            self.yang_parent_name = "punt-policer-interface-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_interface_name']
                            self._child_classes = OrderedDict([("punt-type-interface-table", ("punt_type_interface_table", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable))])
                            self._leafs = OrderedDict([
                                ('punt_interface_name', (YLeaf(YType.str, 'punt-interface-name'), ['str'])),
                            ])
                            self.punt_interface_name = None

                            self.punt_type_interface_table = ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable()
                            self.punt_type_interface_table.parent = self
                            self._children_name_map["punt_type_interface_table"] = "punt-type-interface-table"
                            self._segment_path = lambda: "punt-policer-interface-name" + "[punt-interface-name='" + str(self.punt_interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, ['punt_interface_name'], name, value)


                        class PuntTypeInterfaceTable(_Entity_):
                            """
                            Punt Policer Table
                            
                            .. attribute:: punt_type
                            
                            	Punt Protocol Type
                            	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, self).__init__()

                                self.yang_name = "punt-type-interface-table"
                                self.yang_parent_name = "punt-policer-interface-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("punt-type", ("punt_type", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType))])
                                self._leafs = OrderedDict()

                                self.punt_type = YList(self)
                                self._segment_path = lambda: "punt-type-interface-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, [], name, value)


                            class PuntType(_Entity_):
                                """
                                Punt Protocol Type
                                
                                .. attribute:: punt_id  (key)
                                
                                	Punt Type
                                	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                                
                                .. attribute:: rate
                                
                                	Enable or Disable Punt Police and corresponding Rate in PPS
                                	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, self).__init__()

                                    self.yang_name = "punt-type"
                                    self.yang_parent_name = "punt-type-interface-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['punt_id']
                                    self._child_classes = OrderedDict([("rate", ("rate", ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate))])
                                    self._leafs = OrderedDict([
                                        ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                                    ])
                                    self.punt_id = None

                                    self.rate = None
                                    self._children_name_map["rate"] = "rate"
                                    self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, ['punt_id'], name, value)


                                class Rate(_Entity_):
                                    """
                                    Enable or Disable Punt Police and corresponding
                                    Rate in PPS
                                    
                                    .. attribute:: is_enabled
                                    
                                    	Is Punt Policer enabled
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: rate
                                    
                                    	Configured rate value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, self).__init__()

                                        self.yang_name = "rate"
                                        self.yang_parent_name = "punt-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                        ])
                                        self.is_enabled = None
                                        self.rate = None
                                        self._segment_path = lambda: "rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpuntPolicerLocal']['meta_info']


            class IpolicerLocalTables(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of  		 :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipolicer-local-table", ("ipolicer_local_table", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable))])
                    self._leafs = OrderedDict()

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(_Entity_):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  (key)
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: np_flows
                    
                    	NP name
                    	**type**\:  :py:class:`NpFlows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id1']
                        self._child_classes = OrderedDict([("np-flows", ("np_flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows))])
                        self._leafs = OrderedDict([
                            ('id1', (YLeaf(YType.str, 'id1'), ['str'])),
                        ])
                        self.id1 = None

                        self.np_flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows()
                        self.np_flows.parent = self
                        self._children_name_map["np_flows"] = "np-flows"
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + str(self.id1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class NpFlows(_Entity_):
                        """
                        NP name
                        
                        .. attribute:: np_flow
                        
                        	Table of NP Flow names
                        	**type**\: list of  		 :py:class:`NpFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, self).__init__()

                            self.yang_name = "np-flows"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("np-flow", ("np_flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow))])
                            self._leafs = OrderedDict()

                            self.np_flow = YList(self)
                            self._segment_path = lambda: "np-flows"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, [], name, value)


                        class NpFlow(_Entity_):
                            """
                            Table of NP Flow names
                            
                            .. attribute:: flow_type  (key)
                            
                            	LPTS Flow Type
                            	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                            
                            .. attribute:: np_rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, self).__init__()

                                self.yang_name = "np-flow"
                                self.yang_parent_name = "np-flows"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_type']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                    ('np_rate', (YLeaf(YType.uint32, 'np-rate'), ['int'])),
                                ])
                                self.flow_type = None
                                self.np_rate = None
                                self._segment_path = lambda: "np-flow" + "[flow-type='" + str(self.flow_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, ['flow_type', 'np_rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables']['meta_info']


            class DynamicFlowsTables(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of  		 :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dynamic-flows-table", ("dynamic_flows_table", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable))])
                    self._leafs = OrderedDict()

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(_Entity_):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  (key)
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:  :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of  		 :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['table_type']
                        self._child_classes = OrderedDict([("flow-type", ("flow_type", ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType))])
                        self._leafs = OrderedDict([
                            ('table_type', (YLeaf(YType.enumeration, 'table-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsDynamicFlowConfig', '')])),
                        ])
                        self.table_type = None

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + str(self.table_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(_Entity_):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                            ])
                            self.flow_type = None
                            self.max = None
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.DynamicFlowsTables']['meta_info']


            class IpolicerLocal(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: policer_domains
                
                	Policer Domain Table
                	**type**\:  :py:class:`PolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains>`
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policer-domains", ("policer_domains", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains)), ("flows", ("flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.policer_domains = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains()
                    self.policer_domains.parent = self
                    self._children_name_map["policer_domains"] = "policer-domains"

                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._segment_path = lambda: "ipolicer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class PolicerDomains(_Entity_):
                    """
                    Policer Domain Table
                    
                    .. attribute:: policer_domain
                    
                    	Domain name
                    	**type**\: list of  		 :py:class:`PolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains, self).__init__()

                        self.yang_name = "policer-domains"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("policer-domain", ("policer_domain", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain))])
                        self._leafs = OrderedDict()

                        self.policer_domain = YList(self)
                        self._segment_path = lambda: "policer-domains"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains, [], name, value)


                    class PolicerDomain(_Entity_):
                        """
                        Domain name
                        
                        .. attribute:: domain_name  (key)
                        
                        	Domain name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: flows
                        
                        	Table for Flows
                        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain, self).__init__()

                            self.yang_name = "policer-domain"
                            self.yang_parent_name = "policer-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['domain_name']
                            self._child_classes = OrderedDict([("flows", ("flows", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows))])
                            self._leafs = OrderedDict([
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ])
                            self.domain_name = None

                            self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows()
                            self.flows.parent = self
                            self._children_name_map["flows"] = "flows"
                            self._segment_path = lambda: "policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain, ['domain_name'], name, value)


                        class Flows(_Entity_):
                            """
                            Table for Flows
                            
                            .. attribute:: flow
                            
                            	selected flow type
                            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows, self).__init__()

                                self.yang_name = "flows"
                                self.yang_parent_name = "policer-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("flow", ("flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow))])
                                self._leafs = OrderedDict()

                                self.flow = YList(self)
                                self._segment_path = lambda: "flows"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows, [], name, value)


                            class Flow(_Entity_):
                                """
                                selected flow type
                                
                                .. attribute:: flow_type  (key)
                                
                                	LPTS Flow Type
                                	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                                
                                .. attribute:: precedences
                                
                                	TOS Precedence value(s)
                                	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences>`
                                
                                .. attribute:: rate
                                
                                	Configured rate value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow, self).__init__()

                                    self.yang_name = "flow"
                                    self.yang_parent_name = "flows"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['flow_type']
                                    self._child_classes = OrderedDict([("precedences", ("precedences", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences))])
                                    self._leafs = OrderedDict([
                                        ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                    ])
                                    self.flow_type = None
                                    self.rate = None

                                    self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences()
                                    self.precedences.parent = self
                                    self._children_name_map["precedences"] = "precedences"
                                    self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow, ['flow_type', 'rate'], name, value)


                                class Precedences(_Entity_):
                                    """
                                    TOS Precedence value(s)
                                    
                                    .. attribute:: precedence
                                    
                                    	Precedence values
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 0..7
                                    
                                    

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, self).__init__()

                                        self.yang_name = "precedences"
                                        self.yang_parent_name = "flow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                        ])
                                        self.precedence = []
                                        self._segment_path = lambda: "precedences"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, ['precedence'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.PolicerDomains']['meta_info']


                class Flows(_Entity_):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow", ("flow", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow))])
                        self._leafs = OrderedDict()

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(_Entity_):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([("precedences", ("precedences", ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences))])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ])
                            self.flow_type = None
                            self.rate = None

                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(_Entity_):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: union of the below types:
                            
                            		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            		**type**\: list of int
                            
                            			**range:** 0..7
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                ])
                                self.precedence = []
                                self._segment_path = lambda: "precedences"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info']


        class ClockInterface(_Entity_):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:  :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("clocks", ("clocks", ActiveNodes.ActiveNode.ClockInterface.Clocks))])
                self._leafs = OrderedDict()

                self.clocks = ActiveNodes.ActiveNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface, [], name, value)


            class Clocks(_Entity_):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of  		 :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock", ("clock", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock))])
                    self._leafs = OrderedDict()

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks, [], name, value)


                class Clock(_Entity_):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:  :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','port']
                        self._child_classes = OrderedDict([("frequency-synchronization", ("frequency_synchronization", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ])
                        self.clock_type = None
                        self.port = None

                        self.frequency_synchronization = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"
                        self._segment_path = lambda: "clock" + "[clock-type='" + str(self.clock_type) + "']" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(_Entity_):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:  :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:  :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\: int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-quality-level", ("output_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)), ("input-quality-level", ("input_quality_level", ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel))])
                            self._leafs = OrderedDict([
                                ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('selection_input', (YLeaf(YType.empty, 'selection-input'), ['Empty'])),
                                ('time_of_day_priority', (YLeaf(YType.uint32, 'time-of-day-priority'), ['int'])),
                                ('ssm_disable', (YLeaf(YType.empty, 'ssm-disable'), ['Empty'])),
                            ])
                            self.wait_to_restore_time = None
                            self.priority = None
                            self.selection_input = None
                            self.time_of_day_priority = None
                            self.ssm_disable = None

                            self.output_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"

                            self.input_quality_level = ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._segment_path = lambda: "frequency-synchronization"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['wait_to_restore_time', 'priority', 'selection_input', 'time_of_day_priority', 'ssm_disable'], name, value)


                        class OutputQualityLevel(_Entity_):
                            """
                            Set the output quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "output-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel']['meta_info']


                        class InputQualityLevel(_Entity_):
                            """
                            Set the input quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "input-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock.FrequencySynchronization']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface.Clocks.Clock']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface.Clocks']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.ClockInterface']['meta_info']


        class FiaBufferProfileCfg(_Entity_):
            """
            fia buffer profile cfg
            
            .. attribute:: xl
            
            	Enable to use Extra large Buffer profile
            	**type**\: bool
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.FiaBufferProfileCfg, self).__init__()

                self.yang_name = "fia-buffer-profile-cfg"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('xl', (YLeaf(YType.boolean, 'xl'), ['bool'])),
                ])
                self.xl = None
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.FiaBufferProfileCfg, ['xl'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.FiaBufferProfileCfg']['meta_info']


        class FiaVqiShaperCfg(_Entity_):
            """
            fia vqi shaper cfg
            
            .. attribute:: enhance
            
            	Enable to use Enhanced VQI shaper limit
            	**type**\: bool
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.FiaVqiShaperCfg, self).__init__()

                self.yang_name = "fia-vqi-shaper-cfg"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enhance', (YLeaf(YType.boolean, 'enhance'), ['bool'])),
                ])
                self.enhance = None
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.FiaVqiShaperCfg, ['enhance'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.FiaVqiShaperCfg']['meta_info']


        class PortQueueRemaps(_Entity_):
            """
            port queue remaps
            
            .. attribute:: port_queue_remap
            
            	Front panel port number
            	**type**\: list of  		 :py:class:`PortQueueRemap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.PortQueueRemaps.PortQueueRemap>`
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(ActiveNodes.ActiveNode.PortQueueRemaps, self).__init__()

                self.yang_name = "port-queue-remaps"
                self.yang_parent_name = "active-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("port-queue-remap", ("port_queue_remap", ActiveNodes.ActiveNode.PortQueueRemaps.PortQueueRemap))])
                self._leafs = OrderedDict()

                self.port_queue_remap = YList(self)
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ActiveNodes.ActiveNode.PortQueueRemaps, [], name, value)


            class PortQueueRemap(_Entity_):
                """
                Front panel port number
                
                .. attribute:: port  (key)
                
                	port number <10,11,22,23 34,35,46,47>
                	**type**\: int
                
                	**range:** 0..47
                
                .. attribute:: fabric_queue
                
                	queue number <0\-19>
                	**type**\: int
                
                	**range:** 0..19
                
                

                """

                _prefix = 'asr9k-fia-cfg'
                _revision = '2017-08-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(ActiveNodes.ActiveNode.PortQueueRemaps.PortQueueRemap, self).__init__()

                    self.yang_name = "port-queue-remap"
                    self.yang_parent_name = "port-queue-remaps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['port']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ('fabric_queue', (YLeaf(YType.uint32, 'fabric-queue'), ['int'])),
                    ])
                    self.port = None
                    self.fabric_queue = None
                    self._segment_path = lambda: "port-queue-remap" + "[port='" + str(self.port) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ActiveNodes.ActiveNode.PortQueueRemaps.PortQueueRemap, ['port', 'fabric_queue'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.PortQueueRemaps.PortQueueRemap']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.PortQueueRemaps']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['ActiveNodes.ActiveNode']['meta_info']

    def clone_ptr(self):
        self._top_entity = ActiveNodes()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['ActiveNodes']['meta_info']


class PreconfiguredNodes(_Entity_):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of  		 :py:class:`PreconfiguredNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PreconfiguredNodes, self).__init__()
        self._top_entity = None

        self.yang_name = "preconfigured-nodes"
        self.yang_parent_name = "Cisco-IOS-XR-config-mda-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("preconfigured-node", ("preconfigured_node", PreconfiguredNodes.PreconfiguredNode))])
        self._leafs = OrderedDict()

        self.preconfigured_node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PreconfiguredNodes, [], name, value)


    class PreconfiguredNode(_Entity_):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name  (key)
        
        	The identifier for this node
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:  :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace>`
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:  :py:class:`CiscoIOSXRWatchdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:  :py:class:`CiscoIOSXRWdCfgWatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:  :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        .. attribute:: clock_interface
        
        	Configuration for a clock interface
        	**type**\:  :py:class:`ClockInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface>`
        
        .. attribute:: fia_buffer_profile_cfg
        
        	fia buffer profile cfg
        	**type**\:  :py:class:`FiaBufferProfileCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg>`
        
        .. attribute:: fia_vqi_shaper_cfg
        
        	fia vqi shaper cfg
        	**type**\:  :py:class:`FiaVqiShaperCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg>`
        
        .. attribute:: port_queue_remaps
        
        	port queue remaps
        	**type**\:  :py:class:`PortQueueRemaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PreconfiguredNodes.PreconfiguredNode, self).__init__()

            self.yang_name = "preconfigured-node"
            self.yang_parent_name = "preconfigured-nodes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("Cisco-IOS-XR-infra-ltrace-cfg:ltrace", ("ltrace", PreconfiguredNodes.PreconfiguredNode.Ltrace)), ("Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold", ("cisco_ios_xr_watchd_cfg_watchdog_node_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold)), ("Cisco-IOS-XR-wd-cfg:watchdog-node-threshold", ("cisco_ios_xr_wd_cfg_watchdog_node_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local", ("lpts_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal)), ("Cisco-IOS-XR-freqsync-cfg:clock-interface", ("clock_interface", PreconfiguredNodes.PreconfiguredNode.ClockInterface)), ("Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg", ("fia_buffer_profile_cfg", PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg)), ("Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg", ("fia_vqi_shaper_cfg", PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg)), ("Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps", ("port_queue_remaps", PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
            self.ltrace.parent = self
            self._children_name_map["ltrace"] = "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"

            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_watchd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"

            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self._children_name_map["cisco_ios_xr_wd_cfg_watchdog_node_threshold"] = "Cisco-IOS-XR-wd-cfg:watchdog-node-threshold"

            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self
            self._children_name_map["lpts_local"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"

            self.clock_interface = PreconfiguredNodes.PreconfiguredNode.ClockInterface()
            self.clock_interface.parent = self
            self._children_name_map["clock_interface"] = "Cisco-IOS-XR-freqsync-cfg:clock-interface"

            self.fia_buffer_profile_cfg = PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg()
            self.fia_buffer_profile_cfg.parent = self
            self._children_name_map["fia_buffer_profile_cfg"] = "Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg"

            self.fia_vqi_shaper_cfg = PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg()
            self.fia_vqi_shaper_cfg.parent = self
            self._children_name_map["fia_vqi_shaper_cfg"] = "Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg"

            self.port_queue_remaps = PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps()
            self.port_queue_remaps.parent = self
            self._children_name_map["port_queue_remaps"] = "Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps"
            self._segment_path = lambda: "preconfigured-node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode, ['node_name'], name, value)


        class Ltrace(_Entity_):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:  :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.Ltrace, self).__init__()

                self.yang_name = "ltrace"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("allocation-params", ("allocation_params", PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams))])
                self._leafs = OrderedDict()

                self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self
                self._children_name_map["allocation_params"] = "allocation-params"
                self._segment_path = lambda: "Cisco-IOS-XR-infra-ltrace-cfg:ltrace"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.Ltrace, [], name, value)


            class AllocationParams(_Entity_):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:  :py:class:`InfraLtraceMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceMode>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:  :py:class:`InfraLtraceScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScale>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, self).__init__()

                    self.yang_name = "allocation-params"
                    self.yang_parent_name = "ltrace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceMode', '')])),
                        ('scale_factor', (YLeaf(YType.enumeration, 'scale-factor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg', 'InfraLtraceScale', '')])),
                    ])
                    self.mode = None
                    self.scale_factor = None
                    self._segment_path = lambda: "allocation-params"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams, ['mode', 'scale_factor'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.Ltrace']['meta_info']


        class CiscoIOSXRWatchdCfgWatchdogNodeThreshold(_Entity_):
            """
            watchdog node threshold
            
            .. attribute:: disk_threshold
            
            	Disk thresholds
            	**type**\:  :py:class:`DiskThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold>`
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disk-threshold", ("disk_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold)), ("memory-threshold", ("memory_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.disk_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold()
                self.disk_threshold.parent = self
                self._children_name_map["disk_threshold"] = "disk-threshold"

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold, [], name, value)


            class DiskThreshold(_Entity_):
                """
                Disk thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold, self).__init__()

                    self.yang_name = "disk-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "disk-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.DiskThreshold']['meta_info']


            class MemoryThreshold(_Entity_):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfgWatchdogNodeThreshold']['meta_info']


        class CiscoIOSXRWdCfgWatchdogNodeThreshold(_Entity_):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:  :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, self).__init__()

                self.yang_name = "watchdog-node-threshold"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("memory-threshold", ("memory_threshold", PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold))])
                self._leafs = OrderedDict()

                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self
                self._children_name_map["memory_threshold"] = "memory-threshold"
                self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog-node-threshold"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold, [], name, value)


            class MemoryThreshold(_Entity_):
                """
                Memory thresholds
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\: int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\: int
                
                	**range:** 4..40
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\: int
                
                	**range:** 3..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, self).__init__()

                    self.yang_name = "memory-threshold"
                    self.yang_parent_name = "watchdog-node-threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
                    ])
                    self.minor = None
                    self.severe = None
                    self.critical = None
                    self._segment_path = lambda: "memory-threshold"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold, ['minor', 'severe', 'critical'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfgWatchdogNodeThreshold']['meta_info']


        class LptsLocal(_Entity_):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipunt_policer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpuntPolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            .. attribute:: dynamic_flows_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`DynamicFlowsTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables>`
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:  :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal, self).__init__()

                self.yang_name = "lpts-local"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipunt-policer-local", ("ipunt_policer_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal)), ("ipolicer-local-tables", ("ipolicer_local_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables)), ("dynamic-flows-tables", ("dynamic_flows_tables", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables)), ("ipolicer-local", ("ipolicer_local", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal))])
                self._leafs = OrderedDict()

                self.ipunt_policer_local = None
                self._children_name_map["ipunt_policer_local"] = "ipunt-policer-local"

                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self
                self._children_name_map["ipolicer_local_tables"] = "ipolicer-local-tables"

                self.dynamic_flows_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables()
                self.dynamic_flows_tables.parent = self
                self._children_name_map["dynamic_flows_tables"] = "dynamic-flows-tables"

                self.ipolicer_local = None
                self._children_name_map["ipolicer_local"] = "ipolicer-local"
                self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal, [], name, value)


            class IpuntPolicerLocal(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: punt_type_local_table
                
                	Punt Policer Table
                	**type**\:  :py:class:`PuntTypeLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable>`
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: punt_policer_domains
                
                	Punt Policer Domain Table
                	**type**\:  :py:class:`PuntPolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains>`
                
                .. attribute:: punt_policer_interface_names
                
                	Punt Policer Interface
                	**type**\:  :py:class:`PuntPolicerInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal, self).__init__()

                    self.yang_name = "ipunt-policer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("punt-type-local-table", ("punt_type_local_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable)), ("punt-policer-domains", ("punt_policer_domains", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains)), ("punt-policer-interface-names", ("punt_policer_interface_names", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.punt_type_local_table = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable()
                    self.punt_type_local_table.parent = self
                    self._children_name_map["punt_type_local_table"] = "punt-type-local-table"

                    self.punt_policer_domains = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains()
                    self.punt_policer_domains.parent = self
                    self._children_name_map["punt_policer_domains"] = "punt-policer-domains"

                    self.punt_policer_interface_names = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames()
                    self.punt_policer_interface_names.parent = self
                    self._children_name_map["punt_policer_interface_names"] = "punt-policer-interface-names"
                    self._segment_path = lambda: "ipunt-policer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal, ['enable'], name, value)


                class PuntTypeLocalTable(_Entity_):
                    """
                    Punt Policer Table
                    
                    .. attribute:: punt_type
                    
                    	Punt Protocol Type
                    	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable, self).__init__()

                        self.yang_name = "punt-type-local-table"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-type", ("punt_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType))])
                        self._leafs = OrderedDict()

                        self.punt_type = YList(self)
                        self._segment_path = lambda: "punt-type-local-table"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable, [], name, value)


                    class PuntType(_Entity_):
                        """
                        Punt Protocol Type
                        
                        .. attribute:: punt_id  (key)
                        
                        	Punt Type
                        	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                        
                        .. attribute:: rate
                        
                        	Enable or Disable Punt Police and corresponding Rate in PPS
                        	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType, self).__init__()

                            self.yang_name = "punt-type"
                            self.yang_parent_name = "punt-type-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_id']
                            self._child_classes = OrderedDict([("rate", ("rate", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate))])
                            self._leafs = OrderedDict([
                                ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                            ])
                            self.punt_id = None

                            self.rate = None
                            self._children_name_map["rate"] = "rate"
                            self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType, ['punt_id'], name, value)


                        class Rate(_Entity_):
                            """
                            Enable or Disable Punt Police and corresponding
                            Rate in PPS
                            
                            .. attribute:: is_enabled
                            
                            	Is Punt Policer enabled
                            	**type**\: bool
                            
                            	**mandatory**\: True
                            
                            .. attribute:: rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate, self).__init__()

                                self.yang_name = "rate"
                                self.yang_parent_name = "punt-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                    ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ])
                                self.is_enabled = None
                                self.rate = None
                                self._segment_path = lambda: "rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType.Rate']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable.PuntType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntTypeLocalTable']['meta_info']


                class PuntPolicerDomains(_Entity_):
                    """
                    Punt Policer Domain Table
                    
                    .. attribute:: punt_policer_domain
                    
                    	Domain name
                    	**type**\: list of  		 :py:class:`PuntPolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains, self).__init__()

                        self.yang_name = "punt-policer-domains"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-policer-domain", ("punt_policer_domain", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain))])
                        self._leafs = OrderedDict()

                        self.punt_policer_domain = YList(self)
                        self._segment_path = lambda: "punt-policer-domains"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains, [], name, value)


                    class PuntPolicerDomain(_Entity_):
                        """
                        Domain name
                        
                        .. attribute:: domain_name  (key)
                        
                        	Domain name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: punt_type_domain_table
                        
                        	Punt Policer Table
                        	**type**\:  :py:class:`PuntTypeDomainTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain, self).__init__()

                            self.yang_name = "punt-policer-domain"
                            self.yang_parent_name = "punt-policer-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['domain_name']
                            self._child_classes = OrderedDict([("punt-type-domain-table", ("punt_type_domain_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable))])
                            self._leafs = OrderedDict([
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ])
                            self.domain_name = None

                            self.punt_type_domain_table = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable()
                            self.punt_type_domain_table.parent = self
                            self._children_name_map["punt_type_domain_table"] = "punt-type-domain-table"
                            self._segment_path = lambda: "punt-policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain, ['domain_name'], name, value)


                        class PuntTypeDomainTable(_Entity_):
                            """
                            Punt Policer Table
                            
                            .. attribute:: punt_type
                            
                            	Punt Protocol Type
                            	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, self).__init__()

                                self.yang_name = "punt-type-domain-table"
                                self.yang_parent_name = "punt-policer-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("punt-type", ("punt_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType))])
                                self._leafs = OrderedDict()

                                self.punt_type = YList(self)
                                self._segment_path = lambda: "punt-type-domain-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, [], name, value)


                            class PuntType(_Entity_):
                                """
                                Punt Protocol Type
                                
                                .. attribute:: punt_id  (key)
                                
                                	Punt Type
                                	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                                
                                .. attribute:: rate
                                
                                	Enable or Disable Punt Police and corresponding Rate in PPS
                                	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, self).__init__()

                                    self.yang_name = "punt-type"
                                    self.yang_parent_name = "punt-type-domain-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['punt_id']
                                    self._child_classes = OrderedDict([("rate", ("rate", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate))])
                                    self._leafs = OrderedDict([
                                        ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                                    ])
                                    self.punt_id = None

                                    self.rate = None
                                    self._children_name_map["rate"] = "rate"
                                    self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, ['punt_id'], name, value)


                                class Rate(_Entity_):
                                    """
                                    Enable or Disable Punt Police and corresponding
                                    Rate in PPS
                                    
                                    .. attribute:: is_enabled
                                    
                                    	Is Punt Policer enabled
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: rate
                                    
                                    	Configured rate value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, self).__init__()

                                        self.yang_name = "rate"
                                        self.yang_parent_name = "punt-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                        ])
                                        self.is_enabled = None
                                        self.rate = None
                                        self._segment_path = lambda: "rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains.PuntPolicerDomain']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerDomains']['meta_info']


                class PuntPolicerInterfaceNames(_Entity_):
                    """
                    Punt Policer Interface
                    
                    .. attribute:: punt_policer_interface_name
                    
                    	Pre\-ifib Punt Policer Interface Configuration
                    	**type**\: list of  		 :py:class:`PuntPolicerInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames, self).__init__()

                        self.yang_name = "punt-policer-interface-names"
                        self.yang_parent_name = "ipunt-policer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-policer-interface-name", ("punt_policer_interface_name", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName))])
                        self._leafs = OrderedDict()

                        self.punt_policer_interface_name = YList(self)
                        self._segment_path = lambda: "punt-policer-interface-names"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames, [], name, value)


                    class PuntPolicerInterfaceName(_Entity_):
                        """
                        Pre\-ifib Punt Policer Interface Configuration
                        
                        .. attribute:: punt_interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: punt_type_interface_table
                        
                        	Punt Policer Table
                        	**type**\:  :py:class:`PuntTypeInterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, self).__init__()

                            self.yang_name = "punt-policer-interface-name"
                            self.yang_parent_name = "punt-policer-interface-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_interface_name']
                            self._child_classes = OrderedDict([("punt-type-interface-table", ("punt_type_interface_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable))])
                            self._leafs = OrderedDict([
                                ('punt_interface_name', (YLeaf(YType.str, 'punt-interface-name'), ['str'])),
                            ])
                            self.punt_interface_name = None

                            self.punt_type_interface_table = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable()
                            self.punt_type_interface_table.parent = self
                            self._children_name_map["punt_type_interface_table"] = "punt-type-interface-table"
                            self._segment_path = lambda: "punt-policer-interface-name" + "[punt-interface-name='" + str(self.punt_interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, ['punt_interface_name'], name, value)


                        class PuntTypeInterfaceTable(_Entity_):
                            """
                            Punt Policer Table
                            
                            .. attribute:: punt_type
                            
                            	Punt Protocol Type
                            	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, self).__init__()

                                self.yang_name = "punt-type-interface-table"
                                self.yang_parent_name = "punt-policer-interface-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("punt-type", ("punt_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType))])
                                self._leafs = OrderedDict()

                                self.punt_type = YList(self)
                                self._segment_path = lambda: "punt-type-interface-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, [], name, value)


                            class PuntType(_Entity_):
                                """
                                Punt Protocol Type
                                
                                .. attribute:: punt_id  (key)
                                
                                	Punt Type
                                	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                                
                                .. attribute:: rate
                                
                                	Enable or Disable Punt Police and corresponding Rate in PPS
                                	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate>`
                                
                                	**presence node**\: True
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, self).__init__()

                                    self.yang_name = "punt-type"
                                    self.yang_parent_name = "punt-type-interface-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['punt_id']
                                    self._child_classes = OrderedDict([("rate", ("rate", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate))])
                                    self._leafs = OrderedDict([
                                        ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                                    ])
                                    self.punt_id = None

                                    self.rate = None
                                    self._children_name_map["rate"] = "rate"
                                    self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, ['punt_id'], name, value)


                                class Rate(_Entity_):
                                    """
                                    Enable or Disable Punt Police and corresponding
                                    Rate in PPS
                                    
                                    .. attribute:: is_enabled
                                    
                                    	Is Punt Policer enabled
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: rate
                                    
                                    	Configured rate value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, self).__init__()

                                        self.yang_name = "rate"
                                        self.yang_parent_name = "punt-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                        ])
                                        self.is_enabled = None
                                        self.rate = None
                                        self._segment_path = lambda: "rate"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames.PuntPolicerInterfaceName']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal.PuntPolicerInterfaceNames']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpuntPolicerLocal']['meta_info']


            class IpolicerLocalTables(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of  		 :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, self).__init__()

                    self.yang_name = "ipolicer-local-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipolicer-local-table", ("ipolicer_local_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable))])
                    self._leafs = OrderedDict()

                    self.ipolicer_local_table = YList(self)
                    self._segment_path = lambda: "ipolicer-local-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables, [], name, value)


                class IpolicerLocalTable(_Entity_):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  (key)
                    
                    	none
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: np_flows
                    
                    	NP name
                    	**type**\:  :py:class:`NpFlows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, self).__init__()

                        self.yang_name = "ipolicer-local-table"
                        self.yang_parent_name = "ipolicer-local-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id1']
                        self._child_classes = OrderedDict([("np-flows", ("np_flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows))])
                        self._leafs = OrderedDict([
                            ('id1', (YLeaf(YType.str, 'id1'), ['str'])),
                        ])
                        self.id1 = None

                        self.np_flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows()
                        self.np_flows.parent = self
                        self._children_name_map["np_flows"] = "np-flows"
                        self._segment_path = lambda: "ipolicer-local-table" + "[id1='" + str(self.id1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable, ['id1'], name, value)


                    class NpFlows(_Entity_):
                        """
                        NP name
                        
                        .. attribute:: np_flow
                        
                        	Table of NP Flow names
                        	**type**\: list of  		 :py:class:`NpFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, self).__init__()

                            self.yang_name = "np-flows"
                            self.yang_parent_name = "ipolicer-local-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("np-flow", ("np_flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow))])
                            self._leafs = OrderedDict()

                            self.np_flow = YList(self)
                            self._segment_path = lambda: "np-flows"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows, [], name, value)


                        class NpFlow(_Entity_):
                            """
                            Table of NP Flow names
                            
                            .. attribute:: flow_type  (key)
                            
                            	LPTS Flow Type
                            	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                            
                            .. attribute:: np_rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, self).__init__()

                                self.yang_name = "np-flow"
                                self.yang_parent_name = "np-flows"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['flow_type']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                    ('np_rate', (YLeaf(YType.uint32, 'np-rate'), ['int'])),
                                ])
                                self.flow_type = None
                                self.np_rate = None
                                self._segment_path = lambda: "np-flow" + "[flow-type='" + str(self.flow_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow, ['flow_type', 'np_rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows.NpFlow']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.NpFlows']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables']['meta_info']


            class DynamicFlowsTables(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: dynamic_flows_table
                
                	Table for Dynamic Flows
                	**type**\: list of  		 :py:class:`DynamicFlowsTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, self).__init__()

                    self.yang_name = "dynamic-flows-tables"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dynamic-flows-table", ("dynamic_flows_table", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable))])
                    self._leafs = OrderedDict()

                    self.dynamic_flows_table = YList(self)
                    self._segment_path = lambda: "dynamic-flows-tables"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables, [], name, value)


                class DynamicFlowsTable(_Entity_):
                    """
                    Table for Dynamic Flows
                    
                    .. attribute:: table_type  (key)
                    
                    	LPTS Dynamic Flows Table Type
                    	**type**\:  :py:class:`LptsDynamicFlowConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsDynamicFlowConfig>`
                    
                    .. attribute:: flow_type
                    
                    	Selected flow type
                    	**type**\: list of  		 :py:class:`FlowType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, self).__init__()

                        self.yang_name = "dynamic-flows-table"
                        self.yang_parent_name = "dynamic-flows-tables"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['table_type']
                        self._child_classes = OrderedDict([("flow-type", ("flow_type", PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType))])
                        self._leafs = OrderedDict([
                            ('table_type', (YLeaf(YType.enumeration, 'table-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsDynamicFlowConfig', '')])),
                        ])
                        self.table_type = None

                        self.flow_type = YList(self)
                        self._segment_path = lambda: "dynamic-flows-table" + "[table-type='" + str(self.table_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable, ['table_type'], name, value)


                    class FlowType(_Entity_):
                        """
                        Selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: max
                        
                        	Configured Max TCAM value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, self).__init__()

                            self.yang_name = "flow-type"
                            self.yang_parent_name = "dynamic-flows-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                            ])
                            self.flow_type = None
                            self.max = None
                            self._segment_path = lambda: "flow-type" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType, ['flow_type', 'max'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable.FlowType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables.DynamicFlowsTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.DynamicFlowsTables']['meta_info']


            class IpolicerLocal(_Entity_):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: policer_domains
                
                	Policer Domain Table
                	**type**\:  :py:class:`PolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains>`
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, self).__init__()

                    self.yang_name = "ipolicer-local"
                    self.yang_parent_name = "lpts-local"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policer-domains", ("policer_domains", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains)), ("flows", ("flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.policer_domains = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains()
                    self.policer_domains.parent = self
                    self._children_name_map["policer_domains"] = "policer-domains"

                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._segment_path = lambda: "ipolicer-local"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal, ['enable'], name, value)


                class PolicerDomains(_Entity_):
                    """
                    Policer Domain Table
                    
                    .. attribute:: policer_domain
                    
                    	Domain name
                    	**type**\: list of  		 :py:class:`PolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains, self).__init__()

                        self.yang_name = "policer-domains"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("policer-domain", ("policer_domain", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain))])
                        self._leafs = OrderedDict()

                        self.policer_domain = YList(self)
                        self._segment_path = lambda: "policer-domains"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains, [], name, value)


                    class PolicerDomain(_Entity_):
                        """
                        Domain name
                        
                        .. attribute:: domain_name  (key)
                        
                        	Domain name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: flows
                        
                        	Table for Flows
                        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain, self).__init__()

                            self.yang_name = "policer-domain"
                            self.yang_parent_name = "policer-domains"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['domain_name']
                            self._child_classes = OrderedDict([("flows", ("flows", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows))])
                            self._leafs = OrderedDict([
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                            ])
                            self.domain_name = None

                            self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows()
                            self.flows.parent = self
                            self._children_name_map["flows"] = "flows"
                            self._segment_path = lambda: "policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain, ['domain_name'], name, value)


                        class Flows(_Entity_):
                            """
                            Table for Flows
                            
                            .. attribute:: flow
                            
                            	selected flow type
                            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows, self).__init__()

                                self.yang_name = "flows"
                                self.yang_parent_name = "policer-domain"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("flow", ("flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow))])
                                self._leafs = OrderedDict()

                                self.flow = YList(self)
                                self._segment_path = lambda: "flows"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows, [], name, value)


                            class Flow(_Entity_):
                                """
                                selected flow type
                                
                                .. attribute:: flow_type  (key)
                                
                                	LPTS Flow Type
                                	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                                
                                .. attribute:: precedences
                                
                                	TOS Precedence value(s)
                                	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences>`
                                
                                .. attribute:: rate
                                
                                	Configured rate value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow, self).__init__()

                                    self.yang_name = "flow"
                                    self.yang_parent_name = "flows"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['flow_type']
                                    self._child_classes = OrderedDict([("precedences", ("precedences", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences))])
                                    self._leafs = OrderedDict([
                                        ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                    ])
                                    self.flow_type = None
                                    self.rate = None

                                    self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences()
                                    self.precedences.parent = self
                                    self._children_name_map["precedences"] = "precedences"
                                    self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow, ['flow_type', 'rate'], name, value)


                                class Precedences(_Entity_):
                                    """
                                    TOS Precedence value(s)
                                    
                                    .. attribute:: precedence
                                    
                                    	Precedence values
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                                    
                                    		**type**\: list of int
                                    
                                    			**range:** 0..7
                                    
                                    

                                    """

                                    _prefix = 'lpts-pre-ifib-cfg'
                                    _revision = '2019-10-23'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, self).__init__()

                                        self.yang_name = "precedences"
                                        self.yang_parent_name = "flow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                        ])
                                        self.precedence = []
                                        self._segment_path = lambda: "precedences"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, ['precedence'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow.Precedences']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows.Flow']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain.Flows']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains.PolicerDomain']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.PolicerDomains']['meta_info']


                class Flows(_Entity_):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "ipolicer-local"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow", ("flow", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow))])
                        self._leafs = OrderedDict()

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows, [], name, value)


                    class Flow(_Entity_):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([("precedences", ("precedences", PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences))])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ])
                            self.flow_type = None
                            self.rate = None

                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(_Entity_):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: union of the below types:
                            
                            		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            		**type**\: list of int
                            
                            			**range:** 0..7
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                ])
                                self.precedence = []
                                self._segment_path = lambda: "precedences"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences, ['precedence'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info']


        class ClockInterface(_Entity_):
            """
            Configuration for a clock interface
            
            .. attribute:: clocks
            
            	Configuration for a clock interface
            	**type**\:  :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks>`
            
            

            """

            _prefix = 'freqsync-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface, self).__init__()

                self.yang_name = "clock-interface"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("clocks", ("clocks", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks))])
                self._leafs = OrderedDict()

                self.clocks = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._segment_path = lambda: "Cisco-IOS-XR-freqsync-cfg:clock-interface"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface, [], name, value)


            class Clocks(_Entity_):
                """
                Configuration for a clock interface
                
                .. attribute:: clock
                
                	Configuration for a clock interface
                	**type**\: list of  		 :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "clock-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clock", ("clock", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock))])
                    self._leafs = OrderedDict()

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks, [], name, value)


                class Clock(_Entity_):
                    """
                    Configuration for a clock interface
                    
                    .. attribute:: clock_type  (key)
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  (key)
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: frequency_synchronization
                    
                    	Frequency Synchronization clock configuraiton
                    	**type**\:  :py:class:`FrequencySynchronization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization>`
                    
                    

                    """

                    _prefix = 'freqsync-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['clock_type','port']
                        self._child_classes = OrderedDict([("frequency-synchronization", ("frequency_synchronization", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization))])
                        self._leafs = OrderedDict([
                            ('clock_type', (YLeaf(YType.enumeration, 'clock-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncClock', '')])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ])
                        self.clock_type = None
                        self.port = None

                        self.frequency_synchronization = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization()
                        self.frequency_synchronization.parent = self
                        self._children_name_map["frequency_synchronization"] = "frequency-synchronization"
                        self._segment_path = lambda: "clock" + "[clock-type='" + str(self.clock_type) + "']" + "[port='" + str(self.port) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock, ['clock_type', 'port'], name, value)


                    class FrequencySynchronization(_Entity_):
                        """
                        Frequency Synchronization clock configuraiton
                        
                        .. attribute:: output_quality_level
                        
                        	Set the output quality level
                        	**type**\:  :py:class:`OutputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel>`
                        
                        .. attribute:: input_quality_level
                        
                        	Set the input quality level
                        	**type**\:  :py:class:`InputQualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel>`
                        
                        .. attribute:: wait_to_restore_time
                        
                        	Set the wait\-to\-restore time for this source
                        	**type**\: int
                        
                        	**range:** 0..12
                        
                        	**default value**\: 5
                        
                        .. attribute:: priority
                        
                        	Set the priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: selection_input
                        
                        	Assign this source as a selection input
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: time_of_day_priority
                        
                        	Set the time\-of\-day priority of this source
                        	**type**\: int
                        
                        	**range:** 1..254
                        
                        	**default value**\: 100
                        
                        .. attribute:: ssm_disable
                        
                        	Disable SSM on this source
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'freqsync-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, self).__init__()

                            self.yang_name = "frequency-synchronization"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-quality-level", ("output_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel)), ("input-quality-level", ("input_quality_level", PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel))])
                            self._leafs = OrderedDict([
                                ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('selection_input', (YLeaf(YType.empty, 'selection-input'), ['Empty'])),
                                ('time_of_day_priority', (YLeaf(YType.uint32, 'time-of-day-priority'), ['int'])),
                                ('ssm_disable', (YLeaf(YType.empty, 'ssm-disable'), ['Empty'])),
                            ])
                            self.wait_to_restore_time = None
                            self.priority = None
                            self.selection_input = None
                            self.time_of_day_priority = None
                            self.ssm_disable = None

                            self.output_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel()
                            self.output_quality_level.parent = self
                            self._children_name_map["output_quality_level"] = "output-quality-level"

                            self.input_quality_level = PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel()
                            self.input_quality_level.parent = self
                            self._children_name_map["input_quality_level"] = "input-quality-level"
                            self._segment_path = lambda: "frequency-synchronization"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization, ['wait_to_restore_time', 'priority', 'selection_input', 'time_of_day_priority', 'ssm_disable'], name, value)


                        class OutputQualityLevel(_Entity_):
                            """
                            Set the output quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, self).__init__()

                                self.yang_name = "output-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "output-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.OutputQualityLevel']['meta_info']


                        class InputQualityLevel(_Entity_):
                            """
                            Set the input quality level
                            
                            .. attribute:: quality_level_option
                            
                            	Quality level option
                            	**type**\:  :py:class:`FsyncQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlOption>`
                            
                            .. attribute:: exact_quality_level_value
                            
                            	Exact quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: min_quality_level_value
                            
                            	Minimum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            .. attribute:: max_quality_level_value
                            
                            	Maximum quality level value
                            	**type**\:  :py:class:`FsyncQlValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncQlValue>`
                            
                            

                            """

                            _prefix = 'freqsync-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, self).__init__()

                                self.yang_name = "input-quality-level"
                                self.yang_parent_name = "frequency-synchronization"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('quality_level_option', (YLeaf(YType.enumeration, 'quality-level-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlOption', '')])),
                                    ('exact_quality_level_value', (YLeaf(YType.enumeration, 'exact-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('min_quality_level_value', (YLeaf(YType.enumeration, 'min-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                    ('max_quality_level_value', (YLeaf(YType.enumeration, 'max-quality-level-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes', 'FsyncQlValue', '')])),
                                ])
                                self.quality_level_option = None
                                self.exact_quality_level_value = None
                                self.min_quality_level_value = None
                                self.max_quality_level_value = None
                                self._segment_path = lambda: "input-quality-level"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel, ['quality_level_option', 'exact_quality_level_value', 'min_quality_level_value', 'max_quality_level_value'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization.InputQualityLevel']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock.FrequencySynchronization']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks.Clock']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface.Clocks']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.ClockInterface']['meta_info']


        class FiaBufferProfileCfg(_Entity_):
            """
            fia buffer profile cfg
            
            .. attribute:: xl
            
            	Enable to use Extra large Buffer profile
            	**type**\: bool
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg, self).__init__()

                self.yang_name = "fia-buffer-profile-cfg"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('xl', (YLeaf(YType.boolean, 'xl'), ['bool'])),
                ])
                self.xl = None
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fia-buffer-profile-cfg"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg, ['xl'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.FiaBufferProfileCfg']['meta_info']


        class FiaVqiShaperCfg(_Entity_):
            """
            fia vqi shaper cfg
            
            .. attribute:: enhance
            
            	Enable to use Enhanced VQI shaper limit
            	**type**\: bool
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg, self).__init__()

                self.yang_name = "fia-vqi-shaper-cfg"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enhance', (YLeaf(YType.boolean, 'enhance'), ['bool'])),
                ])
                self.enhance = None
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:fia-vqi-shaper-cfg"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg, ['enhance'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.FiaVqiShaperCfg']['meta_info']


        class PortQueueRemaps(_Entity_):
            """
            port queue remaps
            
            .. attribute:: port_queue_remap
            
            	Front panel port number
            	**type**\: list of  		 :py:class:`PortQueueRemap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps.PortQueueRemap>`
            
            

            """

            _prefix = 'asr9k-fia-cfg'
            _revision = '2017-08-17'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps, self).__init__()

                self.yang_name = "port-queue-remaps"
                self.yang_parent_name = "preconfigured-node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("port-queue-remap", ("port_queue_remap", PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps.PortQueueRemap))])
                self._leafs = OrderedDict()

                self.port_queue_remap = YList(self)
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-fia-cfg:port-queue-remaps"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps, [], name, value)


            class PortQueueRemap(_Entity_):
                """
                Front panel port number
                
                .. attribute:: port  (key)
                
                	port number <10,11,22,23 34,35,46,47>
                	**type**\: int
                
                	**range:** 0..47
                
                .. attribute:: fabric_queue
                
                	queue number <0\-19>
                	**type**\: int
                
                	**range:** 0..19
                
                

                """

                _prefix = 'asr9k-fia-cfg'
                _revision = '2017-08-17'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps.PortQueueRemap, self).__init__()

                    self.yang_name = "port-queue-remap"
                    self.yang_parent_name = "port-queue-remaps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['port']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ('fabric_queue', (YLeaf(YType.uint32, 'fabric-queue'), ['int'])),
                    ])
                    self.port = None
                    self.fabric_queue = None
                    self._segment_path = lambda: "port-queue-remap" + "[port='" + str(self.port) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps.PortQueueRemap, ['port', 'fabric_queue'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps.PortQueueRemap']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.PortQueueRemaps']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']

    def clone_ptr(self):
        self._top_entity = PreconfiguredNodes()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['PreconfiguredNodes']['meta_info']


