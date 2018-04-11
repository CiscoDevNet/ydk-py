""" Cisco_IOS_XR_infra_xtc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package configuration.

This module contains definitions
for the following management objects\:
  pce\: PCE configuration data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PceDisjointPath(Enum):
    """
    PceDisjointPath (Enum Class)

    Pce disjoint path

    .. data:: link = 1

    	Link

    .. data:: node = 2

    	Node

    .. data:: srlg = 3

    	SRLG

    .. data:: srlg_node = 4

    	SRLG Node

    """

    link = Enum.YLeaf(1, "link")

    node = Enum.YLeaf(2, "node")

    srlg = Enum.YLeaf(3, "srlg")

    srlg_node = Enum.YLeaf(4, "srlg-node")


class PceExplicitPathHop(Enum):
    """
    PceExplicitPathHop (Enum Class)

    Pce explicit path hop

    .. data:: address = 1

    	Address

    .. data:: sid_node = 2

    	SID Node

    .. data:: sid_adjancency = 3

    	SID Adjacency

    .. data:: binding_sid = 4

    	Binding SID

    """

    address = Enum.YLeaf(1, "address")

    sid_node = Enum.YLeaf(2, "sid-node")

    sid_adjancency = Enum.YLeaf(3, "sid-adjancency")

    binding_sid = Enum.YLeaf(4, "binding-sid")



class Pce(Entity):
    """
    PCE configuration data
    
    .. attribute:: pcc_addresses
    
    	Path computation client configuration
    	**type**\:  :py:class:`PccAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses>`
    
    .. attribute:: logging
    
    	PCE logging configuration
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Logging>`
    
    .. attribute:: backoff
    
    	PCE backoff configuration
    	**type**\:  :py:class:`Backoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Backoff>`
    
    .. attribute:: state_syncs
    
    	Standby PCE configuration
    	**type**\:  :py:class:`StateSyncs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs>`
    
    .. attribute:: segment_routing
    
    	PCE segment\-routing configuration
    	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting>`
    
    .. attribute:: timers
    
    	PCE Timers configuration
    	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Timers>`
    
    .. attribute:: netconf
    
    	NETCONF configuration
    	**type**\:  :py:class:`Netconf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf>`
    
    .. attribute:: disjoint_path
    
    	Disjoint path configuration
    	**type**\:  :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath>`
    
    .. attribute:: explicit_paths
    
    	Explicit paths
    	**type**\:  :py:class:`ExplicitPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths>`
    
    .. attribute:: server_address
    
    	IPv4 address of PCE server
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: password
    
    	MD5 password
    	**type**\: str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: enable
    
    	True only
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-xtc-cfg'
    _revision = '2016-05-31'

    def __init__(self):
        super(Pce, self).__init__()
        self._top_entity = None

        self.yang_name = "pce"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("pcc-addresses", ("pcc_addresses", Pce.PccAddresses)), ("logging", ("logging", Pce.Logging)), ("backoff", ("backoff", Pce.Backoff)), ("state-syncs", ("state_syncs", Pce.StateSyncs)), ("segment-routing", ("segment_routing", Pce.SegmentRouting)), ("timers", ("timers", Pce.Timers)), ("netconf", ("netconf", Pce.Netconf)), ("disjoint-path", ("disjoint_path", Pce.DisjointPath)), ("explicit-paths", ("explicit_paths", Pce.ExplicitPaths))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('server_address', YLeaf(YType.str, 'server-address')),
            ('password', YLeaf(YType.str, 'password')),
            ('enable', YLeaf(YType.empty, 'enable')),
        ])
        self.server_address = None
        self.password = None
        self.enable = None

        self.pcc_addresses = Pce.PccAddresses()
        self.pcc_addresses.parent = self
        self._children_name_map["pcc_addresses"] = "pcc-addresses"
        self._children_yang_names.add("pcc-addresses")

        self.logging = Pce.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")

        self.backoff = Pce.Backoff()
        self.backoff.parent = self
        self._children_name_map["backoff"] = "backoff"
        self._children_yang_names.add("backoff")

        self.state_syncs = Pce.StateSyncs()
        self.state_syncs.parent = self
        self._children_name_map["state_syncs"] = "state-syncs"
        self._children_yang_names.add("state-syncs")

        self.segment_routing = Pce.SegmentRouting()
        self.segment_routing.parent = self
        self._children_name_map["segment_routing"] = "segment-routing"
        self._children_yang_names.add("segment-routing")

        self.timers = Pce.Timers()
        self.timers.parent = self
        self._children_name_map["timers"] = "timers"
        self._children_yang_names.add("timers")

        self.netconf = Pce.Netconf()
        self.netconf.parent = self
        self._children_name_map["netconf"] = "netconf"
        self._children_yang_names.add("netconf")

        self.disjoint_path = Pce.DisjointPath()
        self.disjoint_path.parent = self
        self._children_name_map["disjoint_path"] = "disjoint-path"
        self._children_yang_names.add("disjoint-path")

        self.explicit_paths = Pce.ExplicitPaths()
        self.explicit_paths.parent = self
        self._children_name_map["explicit_paths"] = "explicit-paths"
        self._children_yang_names.add("explicit-paths")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce"

    def __setattr__(self, name, value):
        self._perform_setattr(Pce, ['server_address', 'password', 'enable'], name, value)


    class PccAddresses(Entity):
        """
        Path computation client configuration
        
        .. attribute:: pcc_address
        
        	Path computation client address
        	**type**\: list of  		 :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.PccAddresses, self).__init__()

            self.yang_name = "pcc-addresses"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("pcc-address", ("pcc_address", Pce.PccAddresses.PccAddress))])
            self._leafs = OrderedDict()

            self.pcc_address = YList(self)
            self._segment_path = lambda: "pcc-addresses"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PccAddresses, [], name, value)


        class PccAddress(Entity):
            """
            Path computation client address
            
            .. attribute:: address  (key)
            
            	IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: lsp_names
            
            	MPLS label switched path
            	**type**\:  :py:class:`LspNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames>`
            
            .. attribute:: enable
            
            	True only
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.PccAddresses.PccAddress, self).__init__()

                self.yang_name = "pcc-address"
                self.yang_parent_name = "pcc-addresses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['address']
                self._child_container_classes = OrderedDict([("lsp-names", ("lsp_names", Pce.PccAddresses.PccAddress.LspNames))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', YLeaf(YType.str, 'address')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.address = None
                self.enable = None

                self.lsp_names = Pce.PccAddresses.PccAddress.LspNames()
                self.lsp_names.parent = self
                self._children_name_map["lsp_names"] = "lsp-names"
                self._children_yang_names.add("lsp-names")
                self._segment_path = lambda: "pcc-address" + "[address='" + str(self.address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/pcc-addresses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PccAddresses.PccAddress, ['address', 'enable'], name, value)


            class LspNames(Entity):
                """
                MPLS label switched path
                
                .. attribute:: lsp_name
                
                	MPLS label switched path
                	**type**\: list of  		 :py:class:`LspName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.PccAddresses.PccAddress.LspNames, self).__init__()

                    self.yang_name = "lsp-names"
                    self.yang_parent_name = "pcc-address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("lsp-name", ("lsp_name", Pce.PccAddresses.PccAddress.LspNames.LspName))])
                    self._leafs = OrderedDict()

                    self.lsp_name = YList(self)
                    self._segment_path = lambda: "lsp-names"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PccAddresses.PccAddress.LspNames, [], name, value)


                class LspName(Entity):
                    """
                    MPLS label switched path
                    
                    .. attribute:: name  (key)
                    
                    	LSP name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: rsvp_te
                    
                    	RSVP\-TE configuration
                    	**type**\:  :py:class:`RsvpTe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe>`
                    
                    .. attribute:: undelegate
                    
                    	Undelegate LSP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: explicit_path_name
                    
                    	Explicit\-path name
                    	**type**\: str
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        super(Pce.PccAddresses.PccAddress.LspNames.LspName, self).__init__()

                        self.yang_name = "lsp-name"
                        self.yang_parent_name = "lsp-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([("rsvp-te", ("rsvp_te", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('undelegate', YLeaf(YType.empty, 'undelegate')),
                            ('explicit_path_name', YLeaf(YType.str, 'explicit-path-name')),
                            ('enable', YLeaf(YType.empty, 'enable')),
                        ])
                        self.name = None
                        self.undelegate = None
                        self.explicit_path_name = None
                        self.enable = None

                        self.rsvp_te = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe()
                        self.rsvp_te.parent = self
                        self._children_name_map["rsvp_te"] = "rsvp-te"
                        self._children_yang_names.add("rsvp-te")
                        self._segment_path = lambda: "lsp-name" + "[name='" + str(self.name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PccAddresses.PccAddress.LspNames.LspName, ['name', 'undelegate', 'explicit_path_name', 'enable'], name, value)


                    class RsvpTe(Entity):
                        """
                        RSVP\-TE configuration
                        
                        .. attribute:: affinity
                        
                        	LSP Affinity
                        	**type**\:  :py:class:`Affinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity>`
                        
                        .. attribute:: priority
                        
                        	Tunnel Setup and Hold Priorities
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: fast_protect
                        
                        	Enable fast protection
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth configuration
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: enable
                        
                        	True only
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2016-05-31'

                        def __init__(self):
                            super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, self).__init__()

                            self.yang_name = "rsvp-te"
                            self.yang_parent_name = "lsp-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("affinity", ("affinity", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity)), ("priority", ("priority", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fast_protect', YLeaf(YType.empty, 'fast-protect')),
                                ('bandwidth', YLeaf(YType.int32, 'bandwidth')),
                                ('enable', YLeaf(YType.empty, 'enable')),
                            ])
                            self.fast_protect = None
                            self.bandwidth = None
                            self.enable = None

                            self.affinity = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity()
                            self.affinity.parent = self
                            self._children_name_map["affinity"] = "affinity"
                            self._children_yang_names.add("affinity")

                            self.priority = None
                            self._children_name_map["priority"] = "priority"
                            self._children_yang_names.add("priority")
                            self._segment_path = lambda: "rsvp-te"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, ['fast_protect', 'bandwidth', 'enable'], name, value)


                        class Affinity(Entity):
                            """
                            LSP Affinity
                            
                            .. attribute:: include_any
                            
                            	Include\-any affinity value
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: include_all
                            
                            	Include\-all affinity value
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: exclude_any
                            
                            	Exclude\-any affinity value
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, self).__init__()

                                self.yang_name = "affinity"
                                self.yang_parent_name = "rsvp-te"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('include_any', YLeaf(YType.str, 'include-any')),
                                    ('include_all', YLeaf(YType.str, 'include-all')),
                                    ('exclude_any', YLeaf(YType.str, 'exclude-any')),
                                ])
                                self.include_any = None
                                self.include_all = None
                                self.exclude_any = None
                                self._segment_path = lambda: "affinity"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, ['include_any', 'include_all', 'exclude_any'], name, value)


                        class Priority(Entity):
                            """
                            Tunnel Setup and Hold Priorities
                            
                            .. attribute:: setup_priority
                            
                            	Setup Priority
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            .. attribute:: hold_priority
                            
                            	Hold Priority
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2016-05-31'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "rsvp-te"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('setup_priority', YLeaf(YType.uint32, 'setup-priority')),
                                    ('hold_priority', YLeaf(YType.uint32, 'hold-priority')),
                                ])
                                self.setup_priority = None
                                self.hold_priority = None
                                self._segment_path = lambda: "priority"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, ['setup_priority', 'hold_priority'], name, value)


    class Logging(Entity):
        """
        PCE logging configuration
        
        .. attribute:: no_path
        
        	Logging NO\-PATH configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: pcerr
        
        	Logging of received PCErr messages
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: fallback
        
        	Logging fallback configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('no_path', YLeaf(YType.empty, 'no-path')),
                ('pcerr', YLeaf(YType.empty, 'pcerr')),
                ('fallback', YLeaf(YType.empty, 'fallback')),
            ])
            self.no_path = None
            self.pcerr = None
            self.fallback = None
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Logging, ['no_path', 'pcerr', 'fallback'], name, value)


    class Backoff(Entity):
        """
        PCE backoff configuration
        
        .. attribute:: ratio
        
        	Backoff common ratio configuration
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        .. attribute:: threshold
        
        	Backoff threshold configuration
        	**type**\: int
        
        	**range:** 0..3600
        
        	**default value**\: 0
        
        .. attribute:: difference
        
        	Backoff common difference configuration
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 2
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Backoff, self).__init__()

            self.yang_name = "backoff"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ratio', YLeaf(YType.uint32, 'ratio')),
                ('threshold', YLeaf(YType.uint32, 'threshold')),
                ('difference', YLeaf(YType.uint32, 'difference')),
            ])
            self.ratio = None
            self.threshold = None
            self.difference = None
            self._segment_path = lambda: "backoff"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Backoff, ['ratio', 'threshold', 'difference'], name, value)


    class StateSyncs(Entity):
        """
        Standby PCE configuration
        
        .. attribute:: state_sync
        
        	Standby PCE ipv4 address
        	**type**\: list of  		 :py:class:`StateSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs.StateSync>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.StateSyncs, self).__init__()

            self.yang_name = "state-syncs"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("state-sync", ("state_sync", Pce.StateSyncs.StateSync))])
            self._leafs = OrderedDict()

            self.state_sync = YList(self)
            self._segment_path = lambda: "state-syncs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.StateSyncs, [], name, value)


        class StateSync(Entity):
            """
            Standby PCE ipv4 address
            
            .. attribute:: address  (key)
            
            	IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.StateSyncs.StateSync, self).__init__()

                self.yang_name = "state-sync"
                self.yang_parent_name = "state-syncs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['address']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', YLeaf(YType.str, 'address')),
                ])
                self.address = None
                self._segment_path = lambda: "state-sync" + "[address='" + str(self.address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/state-syncs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.StateSyncs.StateSync, ['address'], name, value)


    class SegmentRouting(Entity):
        """
        PCE segment\-routing configuration
        
        .. attribute:: te_latency
        
        	Use te\-latency algorithm configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: strict_sid_only
        
        	Use strict\-sid\-only configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.SegmentRouting, self).__init__()

            self.yang_name = "segment-routing"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('te_latency', YLeaf(YType.empty, 'te-latency')),
                ('strict_sid_only', YLeaf(YType.empty, 'strict-sid-only')),
            ])
            self.te_latency = None
            self.strict_sid_only = None
            self._segment_path = lambda: "segment-routing"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.SegmentRouting, ['te_latency', 'strict_sid_only'], name, value)


    class Timers(Entity):
        """
        PCE Timers configuration
        
        .. attribute:: reoptimization_timer
        
        	Topology reoptimization timer configuration
        	**type**\: int
        
        	**range:** 10..3600
        
        	**units**\: second
        
        	**default value**\: 60
        
        .. attribute:: keepalive
        
        	Keepalive interval in seconds, zero to disable
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 30
        
        .. attribute:: minimum_peer_keepalive
        
        	Minimum acceptable peer proposed keepalive interval
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: second
        
        	**default value**\: 20
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Timers, self).__init__()

            self.yang_name = "timers"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('reoptimization_timer', YLeaf(YType.uint32, 'reoptimization-timer')),
                ('keepalive', YLeaf(YType.uint32, 'keepalive')),
                ('minimum_peer_keepalive', YLeaf(YType.uint32, 'minimum-peer-keepalive')),
            ])
            self.reoptimization_timer = None
            self.keepalive = None
            self.minimum_peer_keepalive = None
            self._segment_path = lambda: "timers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Timers, ['reoptimization_timer', 'keepalive', 'minimum_peer_keepalive'], name, value)


    class Netconf(Entity):
        """
        NETCONF configuration
        
        .. attribute:: netconf_ssh
        
        	NETCONF SSH configuration
        	**type**\:  :py:class:`NetconfSsh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf.NetconfSsh>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.Netconf, self).__init__()

            self.yang_name = "netconf"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("netconf-ssh", ("netconf_ssh", Pce.Netconf.NetconfSsh))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.netconf_ssh = Pce.Netconf.NetconfSsh()
            self.netconf_ssh.parent = self
            self._children_name_map["netconf_ssh"] = "netconf-ssh"
            self._children_yang_names.add("netconf-ssh")
            self._segment_path = lambda: "netconf"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()


        class NetconfSsh(Entity):
            """
            NETCONF SSH configuration
            
            .. attribute:: netconf_ssh_password
            
            	Password to use for NETCONF SSH connections
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: netconf_ssh_user
            
            	User name to use for NETCONF SSH connections
            	**type**\: str
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.Netconf.NetconfSsh, self).__init__()

                self.yang_name = "netconf-ssh"
                self.yang_parent_name = "netconf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('netconf_ssh_password', YLeaf(YType.str, 'netconf-ssh-password')),
                    ('netconf_ssh_user', YLeaf(YType.str, 'netconf-ssh-user')),
                ])
                self.netconf_ssh_password = None
                self.netconf_ssh_user = None
                self._segment_path = lambda: "netconf-ssh"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/netconf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.Netconf.NetconfSsh, ['netconf_ssh_password', 'netconf_ssh_user'], name, value)


    class DisjointPath(Entity):
        """
        Disjoint path configuration
        
        .. attribute:: groups
        
        	Association configuration
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups>`
        
        .. attribute:: enable
        
        	True only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.DisjointPath, self).__init__()

            self.yang_name = "disjoint-path"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("groups", ("groups", Pce.DisjointPath.Groups))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('enable', YLeaf(YType.empty, 'enable')),
            ])
            self.enable = None

            self.groups = Pce.DisjointPath.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")
            self._segment_path = lambda: "disjoint-path"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.DisjointPath, ['enable'], name, value)


        class Groups(Entity):
            """
            Association configuration
            
            .. attribute:: group
            
            	Association Group Configuration
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups.Group>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.DisjointPath.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "disjoint-path"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("group", ("group", Pce.DisjointPath.Groups.Group))])
                self._leafs = OrderedDict()

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.DisjointPath.Groups, [], name, value)


            class Group(Entity):
                """
                Association Group Configuration
                
                .. attribute:: group_id  (key)
                
                	Group ID
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: dp_type  (key)
                
                	Disjointness type
                	**type**\:  :py:class:`PceDisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceDisjointPath>`
                
                .. attribute:: sub_id  (key)
                
                	Sub group ID, 0 to unset
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: group_lsp_records
                
                	lsp pcc records container with in group
                	**type**\:  :py:class:`GroupLspRecords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups.Group.GroupLspRecords>`
                
                .. attribute:: strict
                
                	Disable Fallback
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.DisjointPath.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['group_id','dp_type','sub_id']
                    self._child_container_classes = OrderedDict([("group-lsp-records", ("group_lsp_records", Pce.DisjointPath.Groups.Group.GroupLspRecords))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('group_id', YLeaf(YType.uint32, 'group-id')),
                        ('dp_type', YLeaf(YType.enumeration, 'dp-type')),
                        ('sub_id', YLeaf(YType.uint32, 'sub-id')),
                        ('strict', YLeaf(YType.empty, 'strict')),
                        ('enable', YLeaf(YType.empty, 'enable')),
                    ])
                    self.group_id = None
                    self.dp_type = None
                    self.sub_id = None
                    self.strict = None
                    self.enable = None

                    self.group_lsp_records = Pce.DisjointPath.Groups.Group.GroupLspRecords()
                    self.group_lsp_records.parent = self
                    self._children_name_map["group_lsp_records"] = "group-lsp-records"
                    self._children_yang_names.add("group-lsp-records")
                    self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']" + "[dp-type='" + str(self.dp_type) + "']" + "[sub-id='" + str(self.sub_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.DisjointPath.Groups.Group, ['group_id', 'dp_type', 'sub_id', 'strict', 'enable'], name, value)


                class GroupLspRecords(Entity):
                    """
                    lsp pcc records container with in group
                    
                    .. attribute:: group_lsp_record
                    
                    	LSP first/second PCC record tuple containingIpAddr, LspName, DisjPath
                    	**type**\: list of  		 :py:class:`GroupLspRecord <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        super(Pce.DisjointPath.Groups.Group.GroupLspRecords, self).__init__()

                        self.yang_name = "group-lsp-records"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("group-lsp-record", ("group_lsp_record", Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord))])
                        self._leafs = OrderedDict()

                        self.group_lsp_record = YList(self)
                        self._segment_path = lambda: "group-lsp-records"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.DisjointPath.Groups.Group.GroupLspRecords, [], name, value)


                    class GroupLspRecord(Entity):
                        """
                        LSP first/second PCC record tuple
                        containingIpAddr, LspName, DisjPath
                        
                        .. attribute:: lsp_id  (key)
                        
                        	Lsp id
                        	**type**\: int
                        
                        	**range:** 1..2
                        
                        .. attribute:: ip_addr
                        
                        	IP address of PCC
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: lsp_name
                        
                        	Identifying name for LSP
                        	**type**\: str
                        
                        .. attribute:: disj_path
                        
                        	Set LSP to follow shortest\-path
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2016-05-31'

                        def __init__(self):
                            super(Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord, self).__init__()

                            self.yang_name = "group-lsp-record"
                            self.yang_parent_name = "group-lsp-records"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsp_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('lsp_id', YLeaf(YType.uint32, 'lsp-id')),
                                ('ip_addr', YLeaf(YType.str, 'ip-addr')),
                                ('lsp_name', YLeaf(YType.str, 'lsp-name')),
                                ('disj_path', YLeaf(YType.int32, 'disj-path')),
                            ])
                            self.lsp_id = None
                            self.ip_addr = None
                            self.lsp_name = None
                            self.disj_path = None
                            self._segment_path = lambda: "group-lsp-record" + "[lsp-id='" + str(self.lsp_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord, ['lsp_id', 'ip_addr', 'lsp_name', 'disj_path'], name, value)


    class ExplicitPaths(Entity):
        """
        Explicit paths
        
        .. attribute:: explicit_path
        
        	Explicit\-path configuration
        	**type**\: list of  		 :py:class:`ExplicitPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2016-05-31'

        def __init__(self):
            super(Pce.ExplicitPaths, self).__init__()

            self.yang_name = "explicit-paths"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("explicit-path", ("explicit_path", Pce.ExplicitPaths.ExplicitPath))])
            self._leafs = OrderedDict()

            self.explicit_path = YList(self)
            self._segment_path = lambda: "explicit-paths"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.ExplicitPaths, [], name, value)


        class ExplicitPath(Entity):
            """
            Explicit\-path configuration
            
            .. attribute:: name  (key)
            
            	Explicit\-path name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: path_hops
            
            	Path Hops
            	**type**\:  :py:class:`PathHops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops>`
            
            .. attribute:: enable
            
            	True only
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2016-05-31'

            def __init__(self):
                super(Pce.ExplicitPaths.ExplicitPath, self).__init__()

                self.yang_name = "explicit-path"
                self.yang_parent_name = "explicit-paths"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("path-hops", ("path_hops", Pce.ExplicitPaths.ExplicitPath.PathHops))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                ])
                self.name = None
                self.enable = None

                self.path_hops = Pce.ExplicitPaths.ExplicitPath.PathHops()
                self.path_hops.parent = self
                self._children_name_map["path_hops"] = "path-hops"
                self._children_yang_names.add("path-hops")
                self._segment_path = lambda: "explicit-path" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/explicit-paths/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.ExplicitPaths.ExplicitPath, ['name', 'enable'], name, value)


            class PathHops(Entity):
                """
                Path Hops
                
                .. attribute:: path_hop
                
                	Explicit path hop configuration
                	**type**\: list of  		 :py:class:`PathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2016-05-31'

                def __init__(self):
                    super(Pce.ExplicitPaths.ExplicitPath.PathHops, self).__init__()

                    self.yang_name = "path-hops"
                    self.yang_parent_name = "explicit-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("path-hop", ("path_hop", Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop))])
                    self._leafs = OrderedDict()

                    self.path_hop = YList(self)
                    self._segment_path = lambda: "path-hops"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.ExplicitPaths.ExplicitPath.PathHops, [], name, value)


                class PathHop(Entity):
                    """
                    Explicit path hop configuration
                    
                    .. attribute:: index  (key)
                    
                    	Hop Index
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: hop_type
                    
                    	Path hop type
                    	**type**\:  :py:class:`PceExplicitPathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceExplicitPathHop>`
                    
                    .. attribute:: address
                    
                    	IPv4 Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    .. attribute:: remote_address
                    
                    	Remote IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**default value**\: 0.0.0.0
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..1048575
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2016-05-31'

                    def __init__(self):
                        super(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, self).__init__()

                        self.yang_name = "path-hop"
                        self.yang_parent_name = "path-hops"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('index', YLeaf(YType.uint32, 'index')),
                            ('hop_type', YLeaf(YType.enumeration, 'hop-type')),
                            ('address', YLeaf(YType.str, 'address')),
                            ('remote_address', YLeaf(YType.str, 'remote-address')),
                            ('mpls_label', YLeaf(YType.uint32, 'mpls-label')),
                        ])
                        self.index = None
                        self.hop_type = None
                        self.address = None
                        self.remote_address = None
                        self.mpls_label = None
                        self._segment_path = lambda: "path-hop" + "[index='" + str(self.index) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, ['index', 'hop_type', 'address', 'remote_address', 'mpls_label'], name, value)

    def clone_ptr(self):
        self._top_entity = Pce()
        return self._top_entity

