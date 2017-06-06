""" Cisco_IOS_XR_config_mda_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-mda package configuration.

This module contains definitions
for the following management objects\:
  active\-nodes\: Per\-node configuration for active nodes
  preconfigured\-nodes\: preconfigured nodes

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ActiveNodes(object):
    """
    Per\-node configuration for active nodes
    
    .. attribute:: active_node
    
    	The configuration for an active node
    	**type**\: list of    :py:class:`ActiveNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.active_node = YList()
        self.active_node.parent = self
        self.active_node.name = 'active_node'


    class ActiveNode(object):
        """
        The configuration for an active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIosXrWatchdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIosXrWdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace>`
        
        .. attribute:: ssrp_group
        
        	Per\-node SSRP configuration data
        	**type**\:   :py:class:`SsrpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self.lpts_local = ActiveNodes.ActiveNode.LptsLocal()
            self.lpts_local.parent = self
            self.ltrace = ActiveNodes.ActiveNode.Ltrace()
            self.ltrace.parent = self
            self.ssrp_group = ActiveNodes.ActiveNode.SsrpGroup()
            self.ssrp_group.parent = self


        class Ltrace(object):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.allocation_params = ActiveNodes.ActiveNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self


            class AllocationParams(object):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceModeEnum>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScaleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScaleEnum>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mode = None
                    self.scale_factor = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-ltrace-cfg:allocation-params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mode is not None:
                        return True

                    if self.scale_factor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.Ltrace.AllocationParams']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-infra-ltrace-cfg:ltrace'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.allocation_params is not None and self.allocation_params._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.Ltrace']['meta_info']


        class LptsLocal(object):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipolicer_local = None
                self.ipolicer_local_tables = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self


            class IpolicerLocalTables(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipolicer_local_table = YList()
                    self.ipolicer_local_table.parent = self
                    self.ipolicer_local_table.name = 'ipolicer_local_table'


                class IpolicerLocalTable(object):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.id1 = None
                        self.nps = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self


                    class Nps(object):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np = YList()
                            self.np.parent = self
                            self.np.name = 'np'


                        class Np(object):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.id1 = None
                                self.rate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.id1 is None:
                                    raise YPYModelError('Key property id1 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:np[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.id1 is not None:
                                    return True

                                if self.rate is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:nps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.np is not None:
                                for child_ref in self.np:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.id1 is None:
                            raise YPYModelError('Key property id1 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-table[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.id1 is not None:
                            return True

                        if self.nps is not None and self.nps._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-tables'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipolicer_local_table is not None:
                        for child_ref in self.ipolicer_local_table:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables']['meta_info']


            class IpolicerLocal(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.enable = None
                    self.flows = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self


                class Flows(object):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow = YList()
                        self.flow.parent = self
                        self.flow.name = 'flow'


                    class Flow(object):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlowEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlowEnum>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_type = None
                            self.precedences = ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self.rate = None


                        class Precedences(object):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumberEnum>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.precedence = YLeafList()
                                self.precedence.parent = self
                                self.precedence.name = 'precedence'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.precedence is not None:
                                    for child in self.precedence:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.flow_type is None:
                                raise YPYModelError('Key property flow_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.flow_type is not None:
                                return True

                            if self.precedences is not None and self.precedences._has_data():
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.flow is not None:
                            for child_ref in self.flow:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.enable is not None:
                        return True

                    if self.flows is not None and self.flows._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipolicer_local is not None and self.ipolicer_local._has_data():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info']


        class SsrpGroup(object):
            """
            Per\-node SSRP configuration data
            
            .. attribute:: groups
            
            	Table of SSRP Group configuration
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups>`
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.groups = ActiveNodes.ActiveNode.SsrpGroup.Groups()
                self.groups.parent = self


            class Groups(object):
                """
                Table of SSRP Group configuration
                
                .. attribute:: group
                
                	SSRP Group configuration
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.SsrpGroup.Groups.Group>`
                
                

                """

                _prefix = 'ppp-ma-ssrp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group = YList()
                    self.group.parent = self
                    self.group.name = 'group'


                class Group(object):
                    """
                    SSRP Group configuration
                    
                    .. attribute:: group_id  <key>
                    
                    	The identifier for this group
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: profile
                    
                    	This specifies the SSRP profile to use for this group
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ppp-ma-ssrp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.group_id = None
                        self.profile = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_id is None:
                            raise YPYModelError('Key property group_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-ssrp-cfg:group[Cisco-IOS-XR-ppp-ma-ssrp-cfg:group-id = ' + str(self.group_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.group_id is not None:
                            return True

                        if self.profile is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup.Groups.Group']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-ssrp-cfg:groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group is not None:
                        for child_ref in self.group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup.Groups']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp-group'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.groups is not None and self.groups._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.SsrpGroup']['meta_info']


        class CiscoIosXrWatchdCfg_WatchdogNodeThreshold(object):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold']['meta_info']


        class CiscoIosXrWdCfg_WatchdogNodeThreshold(object):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['ActiveNodes.ActiveNode.CiscoIosXrWdCfg_WatchdogNodeThreshold']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-config-mda-cfg:active-nodes/Cisco-IOS-XR-config-mda-cfg:active-node[Cisco-IOS-XR-config-mda-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.node_name is not None:
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.lpts_local is not None and self.lpts_local._has_data():
                return True

            if self.ltrace is not None and self.ltrace._has_data():
                return True

            if self.ssrp_group is not None and self.ssrp_group._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['ActiveNodes.ActiveNode']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-mda-cfg:active-nodes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.active_node is not None:
            for child_ref in self.active_node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['ActiveNodes']['meta_info']


class PreconfiguredNodes(object):
    """
    preconfigured nodes
    
    .. attribute:: preconfigured_node
    
    	The configuration for a non\-active node
    	**type**\: list of    :py:class:`PreconfiguredNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode>`
    
    

    """

    _prefix = 'config-mda-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.preconfigured_node = YList()
        self.preconfigured_node.parent = self
        self.preconfigured_node.name = 'preconfigured_node'


    class PreconfiguredNode(object):
        """
        The configuration for a non\-active node
        
        .. attribute:: node_name  <key>
        
        	The identifier for this node
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: cisco_ios_xr_watchd_cfg_watchdog_node_threshold
        
        	watchdog node threshold
        	**type**\:   :py:class:`CiscoIosXrWatchdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: cisco_ios_xr_wd_cfg_watchdog_node_threshold
        
        	Watchdog threshold configuration
        	**type**\:   :py:class:`CiscoIosXrWdCfg_WatchdogNodeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold>`
        
        .. attribute:: lpts_local
        
        	lpts node specific configuration commands
        	**type**\:   :py:class:`LptsLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal>`
        
        .. attribute:: ltrace
        
        	Ltrace Memory configuration
        	**type**\:   :py:class:`Ltrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace>`
        
        

        """

        _prefix = 'config-mda-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold.parent = self
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold()
            self.cisco_ios_xr_wd_cfg_watchdog_node_threshold.parent = self
            self.lpts_local = PreconfiguredNodes.PreconfiguredNode.LptsLocal()
            self.lpts_local.parent = self
            self.ltrace = PreconfiguredNodes.PreconfiguredNode.Ltrace()
            self.ltrace.parent = self


        class Ltrace(object):
            """
            Ltrace Memory configuration
            
            .. attribute:: allocation_params
            
            	Select Ltrace mode and scale\-factor
            	**type**\:   :py:class:`AllocationParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams>`
            
            

            """

            _prefix = 'infra-ltrace-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.allocation_params = PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams()
                self.allocation_params.parent = self


            class AllocationParams(object):
                """
                Select Ltrace mode and scale\-factor
                
                .. attribute:: mode
                
                	Select an allocation mode (static\:1, dynamic \:2)
                	**type**\:   :py:class:`InfraLtraceModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceModeEnum>`
                
                .. attribute:: scale_factor
                
                	Select a scaling down factor
                	**type**\:   :py:class:`InfraLtraceScaleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_ltrace_cfg.InfraLtraceScaleEnum>`
                
                

                """

                _prefix = 'infra-ltrace-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mode = None
                    self.scale_factor = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-ltrace-cfg:allocation-params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mode is not None:
                        return True

                    if self.scale_factor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.Ltrace.AllocationParams']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-infra-ltrace-cfg:ltrace'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.allocation_params is not None and self.allocation_params._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.Ltrace']['meta_info']


        class LptsLocal(object):
            """
            lpts node specific configuration commands
            
            .. attribute:: ipolicer_local
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal>`
            
            	**presence node**\: True
            
            .. attribute:: ipolicer_local_tables
            
            	Node specific Pre IFIB (Internal Forwarding Information Base) Configuration
            	**type**\:   :py:class:`IpolicerLocalTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipolicer_local = None
                self.ipolicer_local_tables = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables()
                self.ipolicer_local_tables.parent = self


            class IpolicerLocalTables(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: ipolicer_local_table
                
                	Pre IFIB (Internal Forwarding Information Base) configuration table
                	**type**\: list of    :py:class:`IpolicerLocalTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipolicer_local_table = YList()
                    self.ipolicer_local_table.parent = self
                    self.ipolicer_local_table.name = 'ipolicer_local_table'


                class IpolicerLocalTable(object):
                    """
                    Pre IFIB (Internal Forwarding Information
                    Base) configuration table
                    
                    .. attribute:: id1  <key>
                    
                    	none
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: nps
                    
                    	NP name
                    	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.id1 = None
                        self.nps = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps()
                        self.nps.parent = self


                    class Nps(object):
                        """
                        NP name
                        
                        .. attribute:: np
                        
                        	Table of NP names
                        	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.np = YList()
                            self.np.parent = self
                            self.np.name = 'np'


                        class Np(object):
                            """
                            Table of NP names
                            
                            .. attribute:: id1  <key>
                            
                            	none
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate
                            
                            	Packets per second
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.id1 = None
                                self.rate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.id1 is None:
                                    raise YPYModelError('Key property id1 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:np[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.id1 is not None:
                                    return True

                                if self.rate is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:nps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.np is not None:
                                for child_ref in self.np:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.id1 is None:
                            raise YPYModelError('Key property id1 is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-table[Cisco-IOS-XR-lpts-pre-ifib-cfg:id1 = ' + str(self.id1) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.id1 is not None:
                            return True

                        if self.nps is not None and self.nps._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local-tables'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ipolicer_local_table is not None:
                        for child_ref in self.ipolicer_local_table:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables']['meta_info']


            class IpolicerLocal(object):
                """
                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                
                .. attribute:: enable
                
                	Enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.enable = None
                    self.flows = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows()
                    self.flows.parent = self


                class Flows(object):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow = YList()
                        self.flow.parent = self
                        self.flow.name = 'flow'


                    class Flow(object):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  <key>
                        
                        	LPTS Flow Type
                        	**type**\:   :py:class:`LptsFlowEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlowEnum>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:   :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.flow_type = None
                            self.precedences = PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self.rate = None


                        class Precedences(object):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of   :py:class:`LptsPreIFibPrecedenceNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumberEnum>`
                            
                            
                            ----
                            	**type**\:  list of int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.precedence = YLeafList()
                                self.precedence.parent = self
                                self.precedence.name = 'precedence'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:precedences'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.precedence is not None:
                                    for child in self.precedence:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.flow_type is None:
                                raise YPYModelError('Key property flow_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flow[Cisco-IOS-XR-lpts-pre-ifib-cfg:flow-type = ' + str(self.flow_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.flow_type is not None:
                                return True

                            if self.precedences is not None and self.precedences._has_data():
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:flows'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.flow is not None:
                            for child_ref in self.flow:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                        return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer-local'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.enable is not None:
                        return True

                    if self.flows is not None and self.flows._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-lpts-pre-ifib-cfg:lpts-local'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipolicer_local is not None and self.ipolicer_local._has_data():
                    return True

                if self.ipolicer_local_tables is not None and self.ipolicer_local_tables._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info']


        class CiscoIosXrWatchdCfg_WatchdogNodeThreshold(object):
            """
            watchdog node threshold
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'watchd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'watchd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-watchd-cfg:Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWatchdCfg_WatchdogNodeThreshold']['meta_info']


        class CiscoIosXrWdCfg_WatchdogNodeThreshold(object):
            """
            Watchdog threshold configuration
            
            .. attribute:: memory_threshold
            
            	Memory thresholds
            	**type**\:   :py:class:`MemoryThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_mda_cfg.PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold>`
            
            

            """

            _prefix = 'wd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_threshold = PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold()
                self.memory_threshold.parent = self


            class MemoryThreshold(object):
                """
                Memory thresholds
                
                .. attribute:: critical
                
                	Threshold, Range(3, severe)
                	**type**\:  int
                
                	**range:** 3..40
                
                .. attribute:: minor
                
                	Threshold, Range(5, 40)
                	**type**\:  int
                
                	**range:** 5..40
                
                .. attribute:: severe
                
                	Threshold, Range(4, minor)
                	**type**\:  int
                
                	**range:** 4..40
                
                

                """

                _prefix = 'wd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.critical = None
                    self.minor = None
                    self.severe = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:memory-threshold'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.critical is not None:
                        return True

                    if self.minor is not None:
                        return True

                    if self.severe is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                    return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold.MemoryThreshold']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-wd-cfg:Cisco-IOS-XR-wd-cfg_watchdog-node-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.memory_threshold is not None and self.memory_threshold._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
                return meta._meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIosXrWdCfg_WatchdogNodeThreshold']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes/Cisco-IOS-XR-config-mda-cfg:preconfigured-node[Cisco-IOS-XR-config-mda-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.node_name is not None:
                return True

            if self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_watchd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.cisco_ios_xr_wd_cfg_watchdog_node_threshold is not None and self.cisco_ios_xr_wd_cfg_watchdog_node_threshold._has_data():
                return True

            if self.lpts_local is not None and self.lpts_local._has_data():
                return True

            if self.ltrace is not None and self.ltrace._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
            return meta._meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-mda-cfg:preconfigured-nodes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.preconfigured_node is not None:
            for child_ref in self.preconfigured_node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_mda_cfg as meta
        return meta._meta_table['PreconfiguredNodes']['meta_info']


