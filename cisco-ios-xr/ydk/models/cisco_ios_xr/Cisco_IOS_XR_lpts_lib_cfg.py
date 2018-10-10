""" Cisco_IOS_XR_lpts_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-lib package configuration.

This module contains definitions
for the following management objects\:
  lpts\: lpts configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Lpts(Entity):
    """
    lpts configuration commands
    
    .. attribute:: punt
    
    	Configure penalty timeout value
    	**type**\:  :py:class:`Punt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt>`
    
    .. attribute:: ipolicer
    
    	Pre IFiB Configuration 
    	**type**\:  :py:class:`Ipolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'lpts-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lpts, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-lib-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt", ("punt", Lpts.Punt)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer", ("ipolicer", Lpts.Ipolicer))])
        self._leafs = OrderedDict()

        self.punt = Lpts.Punt()
        self.punt.parent = self
        self._children_name_map["punt"] = "Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt"

        self.ipolicer = None
        self._children_name_map["ipolicer"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer"
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lpts, [], name, value)


    class Punt(Entity):
        """
        Configure penalty timeout value
        
        .. attribute:: flowtrap
        
        	excessive punt flow trap configuration commands
        	**type**\:  :py:class:`Flowtrap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap>`
        
        

        """

        _prefix = 'lpts-punt-flowtrap-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Lpts.Punt, self).__init__()

            self.yang_name = "punt"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("flowtrap", ("flowtrap", Lpts.Punt.Flowtrap))])
            self._leafs = OrderedDict()

            self.flowtrap = Lpts.Punt.Flowtrap()
            self.flowtrap.parent = self
            self._children_name_map["flowtrap"] = "flowtrap"
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.Punt, [], name, value)


        class Flowtrap(Entity):
            """
            excessive punt flow trap configuration commands
            
            .. attribute:: penalty_rates
            
            	Configure penalty policing rate
            	**type**\:  :py:class:`PenaltyRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates>`
            
            .. attribute:: penalty_timeouts
            
            	Configure penalty timeout value
            	**type**\:  :py:class:`PenaltyTimeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts>`
            
            .. attribute:: exclude
            
            	Exclude an item from all traps
            	**type**\:  :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude>`
            
            .. attribute:: max_flow_gap
            
            	Maximum flow gap in milliseconds
            	**type**\: int
            
            	**range:** 1..60000
            
            .. attribute:: et_size
            
            	Should be power of 2. Any one of 1,2,4,8,16,32 ,64,128
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: eviction_threshold
            
            	Eviction threshold, should be less than report\-threshold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: report_threshold
            
            	Threshold to cross for a flow to be considered as bad actor flow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: non_subscriber_interfaces
            
            	Enable trap based on source mac on non\-subscriber interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sample_prob
            
            	Probability of packets to be sampled
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: eviction_search_limit
            
            	Eviction search limit, should be less than trap\-size
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: routing_protocols_enable
            
            	Allow routing protocols to pass through copp sampler
            	**type**\: bool
            
            .. attribute:: subscriber_interfaces
            
            	Enable the trap on subscriber interfaces
            	**type**\: bool
            
            .. attribute:: interface_based_flow
            
            	Identify flow based on interface and flowtype
            	**type**\: bool
            
            .. attribute:: dampening
            
            	Dampening period for a bad actor flow in milliseconds
            	**type**\: int
            
            	**range:** 5000..60000
            
            

            """

            _prefix = 'lpts-punt-flowtrap-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Lpts.Punt.Flowtrap, self).__init__()

                self.yang_name = "flowtrap"
                self.yang_parent_name = "punt"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("penalty-rates", ("penalty_rates", Lpts.Punt.Flowtrap.PenaltyRates)), ("penalty-timeouts", ("penalty_timeouts", Lpts.Punt.Flowtrap.PenaltyTimeouts)), ("exclude", ("exclude", Lpts.Punt.Flowtrap.Exclude))])
                self._leafs = OrderedDict([
                    ('max_flow_gap', (YLeaf(YType.uint32, 'max-flow-gap'), ['int'])),
                    ('et_size', (YLeaf(YType.uint32, 'et-size'), ['int'])),
                    ('eviction_threshold', (YLeaf(YType.uint32, 'eviction-threshold'), ['int'])),
                    ('report_threshold', (YLeaf(YType.uint16, 'report-threshold'), ['int'])),
                    ('non_subscriber_interfaces', (YLeaf(YType.uint32, 'non-subscriber-interfaces'), ['int'])),
                    ('sample_prob', (YLeaf(YType.str, 'sample-prob'), ['str'])),
                    ('eviction_search_limit', (YLeaf(YType.uint32, 'eviction-search-limit'), ['int'])),
                    ('routing_protocols_enable', (YLeaf(YType.boolean, 'routing-protocols-enable'), ['bool'])),
                    ('subscriber_interfaces', (YLeaf(YType.boolean, 'subscriber-interfaces'), ['bool'])),
                    ('interface_based_flow', (YLeaf(YType.boolean, 'interface-based-flow'), ['bool'])),
                    ('dampening', (YLeaf(YType.uint32, 'dampening'), ['int'])),
                ])
                self.max_flow_gap = None
                self.et_size = None
                self.eviction_threshold = None
                self.report_threshold = None
                self.non_subscriber_interfaces = None
                self.sample_prob = None
                self.eviction_search_limit = None
                self.routing_protocols_enable = None
                self.subscriber_interfaces = None
                self.interface_based_flow = None
                self.dampening = None

                self.penalty_rates = Lpts.Punt.Flowtrap.PenaltyRates()
                self.penalty_rates.parent = self
                self._children_name_map["penalty_rates"] = "penalty-rates"

                self.penalty_timeouts = Lpts.Punt.Flowtrap.PenaltyTimeouts()
                self.penalty_timeouts.parent = self
                self._children_name_map["penalty_timeouts"] = "penalty-timeouts"

                self.exclude = Lpts.Punt.Flowtrap.Exclude()
                self.exclude.parent = self
                self._children_name_map["exclude"] = "exclude"
                self._segment_path = lambda: "flowtrap"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Punt.Flowtrap, ['max_flow_gap', 'et_size', 'eviction_threshold', 'report_threshold', 'non_subscriber_interfaces', 'sample_prob', 'eviction_search_limit', 'routing_protocols_enable', 'subscriber_interfaces', 'interface_based_flow', 'dampening'], name, value)


            class PenaltyRates(Entity):
                """
                Configure penalty policing rate
                
                .. attribute:: penalty_rate
                
                	none
                	**type**\: list of  		 :py:class:`PenaltyRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.PenaltyRates, self).__init__()

                    self.yang_name = "penalty-rates"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("penalty-rate", ("penalty_rate", Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate))])
                    self._leafs = OrderedDict()

                    self.penalty_rate = YList(self)
                    self._segment_path = lambda: "penalty-rates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyRates, [], name, value)


                class PenaltyRate(Entity):
                    """
                    none
                    
                    .. attribute:: protocol_name  (key)
                    
                    	none
                    	**type**\:  :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: rate
                    
                    	Penalty policer rate in packets\-per\-second
                    	**type**\: int
                    
                    	**range:** 2..100
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, self).__init__()

                        self.yang_name = "penalty-rate"
                        self.yang_parent_name = "penalty-rates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['protocol_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId', '')])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ])
                        self.protocol_name = None
                        self.rate = None
                        self._segment_path = lambda: "penalty-rate" + "[protocol-name='" + str(self.protocol_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-rates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, ['protocol_name', 'rate'], name, value)


            class PenaltyTimeouts(Entity):
                """
                Configure penalty timeout value
                
                .. attribute:: penalty_timeout
                
                	none
                	**type**\: list of  		 :py:class:`PenaltyTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.PenaltyTimeouts, self).__init__()

                    self.yang_name = "penalty-timeouts"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("penalty-timeout", ("penalty_timeout", Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout))])
                    self._leafs = OrderedDict()

                    self.penalty_timeout = YList(self)
                    self._segment_path = lambda: "penalty-timeouts"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyTimeouts, [], name, value)


                class PenaltyTimeout(Entity):
                    """
                    none
                    
                    .. attribute:: protocol_name  (key)
                    
                    	none
                    	**type**\:  :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: timeout
                    
                    	Timeout value in minutes
                    	**type**\: int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, self).__init__()

                        self.yang_name = "penalty-timeout"
                        self.yang_parent_name = "penalty-timeouts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['protocol_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId', '')])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ])
                        self.protocol_name = None
                        self.timeout = None
                        self._segment_path = lambda: "penalty-timeout" + "[protocol-name='" + str(self.protocol_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-timeouts/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, ['protocol_name', 'timeout'], name, value)


            class Exclude(Entity):
                """
                Exclude an item from all traps
                
                .. attribute:: interface_names
                
                	none
                	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Lpts.Punt.Flowtrap.Exclude, self).__init__()

                    self.yang_name = "exclude"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-names", ("interface_names", Lpts.Punt.Flowtrap.Exclude.InterfaceNames))])
                    self._leafs = OrderedDict()

                    self.interface_names = Lpts.Punt.Flowtrap.Exclude.InterfaceNames()
                    self.interface_names.parent = self
                    self._children_name_map["interface_names"] = "interface-names"
                    self._segment_path = lambda: "exclude"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.Exclude, [], name, value)


                class InterfaceNames(Entity):
                    """
                    none
                    
                    .. attribute:: interface_name
                    
                    	Name of interface to exclude from all traps
                    	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, self).__init__()

                        self.yang_name = "interface-names"
                        self.yang_parent_name = "exclude"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-name", ("interface_name", Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName))])
                        self._leafs = OrderedDict()

                        self.interface_name = YList(self)
                        self._segment_path = lambda: "interface-names"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, [], name, value)


                    class InterfaceName(Entity):
                        """
                        Name of interface to exclude from all traps
                        
                        .. attribute:: ifname  (key)
                        
                        	Name of interface to exclude from all traps
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: id1
                        
                        	Enabled or disabled
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'lpts-punt-flowtrap-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, self).__init__()

                            self.yang_name = "interface-name"
                            self.yang_parent_name = "interface-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['ifname']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                                ('id1', (YLeaf(YType.boolean, 'id1'), ['bool'])),
                            ])
                            self.ifname = None
                            self.id1 = None
                            self._segment_path = lambda: "interface-name" + "[ifname='" + str(self.ifname) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/interface-names/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, ['ifname', 'id1'], name, value)


    class Ipolicer(Entity):
        """
        Pre IFiB Configuration 
        
        .. attribute:: acls
        
        	Table for ACLs
        	**type**\:  :py:class:`Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls>`
        
        .. attribute:: enable
        
        	Enabled
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: flows
        
        	Table for Flows
        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Lpts.Ipolicer, self).__init__()

            self.yang_name = "ipolicer"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("acls", ("acls", Lpts.Ipolicer.Acls)), ("flows", ("flows", Lpts.Ipolicer.Flows))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.acls = Lpts.Ipolicer.Acls()
            self.acls.parent = self
            self._children_name_map["acls"] = "acls"

            self.flows = Lpts.Ipolicer.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.Ipolicer, ['enable'], name, value)


        class Acls(Entity):
            """
            Table for ACLs
            
            .. attribute:: acl
            
            	ACL name
            	**type**\: list of  		 :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Lpts.Ipolicer.Acls, self).__init__()

                self.yang_name = "acls"
                self.yang_parent_name = "ipolicer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("acl", ("acl", Lpts.Ipolicer.Acls.Acl))])
                self._leafs = OrderedDict()

                self.acl = YList(self)
                self._segment_path = lambda: "acls"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Ipolicer.Acls, [], name, value)


            class Acl(Entity):
                """
                ACL name
                
                .. attribute:: acl_name  (key)
                
                	ACL name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: afi_types
                
                	AFI Family
                	**type**\:  :py:class:`AfiTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Lpts.Ipolicer.Acls.Acl, self).__init__()

                    self.yang_name = "acl"
                    self.yang_parent_name = "acls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['acl_name']
                    self._child_classes = OrderedDict([("afi-types", ("afi_types", Lpts.Ipolicer.Acls.Acl.AfiTypes))])
                    self._leafs = OrderedDict([
                        ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                    ])
                    self.acl_name = None

                    self.afi_types = Lpts.Ipolicer.Acls.Acl.AfiTypes()
                    self.afi_types.parent = self
                    self._children_name_map["afi_types"] = "afi-types"
                    self._segment_path = lambda: "acl" + "[acl-name='" + str(self.acl_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/acls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Ipolicer.Acls.Acl, ['acl_name'], name, value)


                class AfiTypes(Entity):
                    """
                    AFI Family
                    
                    .. attribute:: afi_type
                    
                    	AFI Family type
                    	**type**\: list of  		 :py:class:`AfiType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Lpts.Ipolicer.Acls.Acl.AfiTypes, self).__init__()

                        self.yang_name = "afi-types"
                        self.yang_parent_name = "acl"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("afi-type", ("afi_type", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType))])
                        self._leafs = OrderedDict()

                        self.afi_type = YList(self)
                        self._segment_path = lambda: "afi-types"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes, [], name, value)


                    class AfiType(Entity):
                        """
                        AFI Family type
                        
                        .. attribute:: afi_family_type  (key)
                        
                        	AFI Family Type
                        	**type**\:  :py:class:`Lptsafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.Lptsafi>`
                        
                        .. attribute:: vrf_names
                        
                        	VRF list
                        	**type**\:  :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType, self).__init__()

                            self.yang_name = "afi-type"
                            self.yang_parent_name = "afi-types"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['afi_family_type']
                            self._child_classes = OrderedDict([("vrf-names", ("vrf_names", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames))])
                            self._leafs = OrderedDict([
                                ('afi_family_type', (YLeaf(YType.enumeration, 'afi-family-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'Lptsafi', '')])),
                            ])
                            self.afi_family_type = None

                            self.vrf_names = Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames()
                            self.vrf_names.parent = self
                            self._children_name_map["vrf_names"] = "vrf-names"
                            self._segment_path = lambda: "afi-type" + "[afi-family-type='" + str(self.afi_family_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType, ['afi_family_type'], name, value)


                        class VrfNames(Entity):
                            """
                            VRF list
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: list of  		 :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames, self).__init__()

                                self.yang_name = "vrf-names"
                                self.yang_parent_name = "afi-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("vrf-name", ("vrf_name", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName))])
                                self._leafs = OrderedDict()

                                self.vrf_name = YList(self)
                                self._segment_path = lambda: "vrf-names"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames, [], name, value)


                            class VrfName(Entity):
                                """
                                VRF name
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: acl_rate
                                
                                	pre\-ifib policer rate config commands
                                	**type**\: int
                                
                                	**range:** 0..100000
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName, self).__init__()

                                    self.yang_name = "vrf-name"
                                    self.yang_parent_name = "vrf-names"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('acl_rate', (YLeaf(YType.uint32, 'acl-rate'), ['int'])),
                                    ])
                                    self.vrf_name = None
                                    self.acl_rate = None
                                    self._segment_path = lambda: "vrf-name" + "[vrf-name='" + str(self.vrf_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName, ['vrf_name', 'acl_rate'], name, value)


        class Flows(Entity):
            """
            Table for Flows
            
            .. attribute:: flow
            
            	selected flow type
            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Lpts.Ipolicer.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "ipolicer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("flow", ("flow", Lpts.Ipolicer.Flows.Flow))])
                self._leafs = OrderedDict()

                self.flow = YList(self)
                self._segment_path = lambda: "flows"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Ipolicer.Flows, [], name, value)


            class Flow(Entity):
                """
                selected flow type
                
                .. attribute:: flow_type  (key)
                
                	LPTS Flow Type
                	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                
                .. attribute:: precedences
                
                	TOS Precedence value(s)
                	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow.Precedences>`
                
                .. attribute:: rate
                
                	Configured rate value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Lpts.Ipolicer.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['flow_type']
                    self._child_classes = OrderedDict([("precedences", ("precedences", Lpts.Ipolicer.Flows.Flow.Precedences))])
                    self._leafs = OrderedDict([
                        ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                    ])
                    self.flow_type = None
                    self.rate = None

                    self.precedences = Lpts.Ipolicer.Flows.Flow.Precedences()
                    self.precedences.parent = self
                    self._children_name_map["precedences"] = "precedences"
                    self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/flows/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Ipolicer.Flows.Flow, ['flow_type', 'rate'], name, value)


                class Precedences(Entity):
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
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Lpts.Ipolicer.Flows.Flow.Precedences, self).__init__()

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
                        self._perform_setattr(Lpts.Ipolicer.Flows.Flow.Precedences, ['precedence'], name, value)

    def clone_ptr(self):
        self._top_entity = Lpts()
        return self._top_entity

