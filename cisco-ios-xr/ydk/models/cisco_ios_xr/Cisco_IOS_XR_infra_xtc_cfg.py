""" Cisco_IOS_XR_infra_xtc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package configuration.

This module contains definitions
for the following management objects\:
  pce\: PCE configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PceBindingSid(Enum):
    """
    PceBindingSid (Enum Class)

    Pce binding sid

    .. data:: mpls_label_specified = 1

    	Use specified BSID MPLS label

    .. data:: mpls_label_any = 2

    	Allocate BSID MPLS label

    """

    mpls_label_specified = Enum.YLeaf(1, "mpls-label-specified")

    mpls_label_any = Enum.YLeaf(2, "mpls-label-any")


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


class PceEndPoint(Enum):
    """
    PceEndPoint (Enum Class)

    Pce end point

    .. data:: end_point_type_ipv4 = 1

    	IPv4 endpoint address

    .. data:: end_point_type_ipv6 = 2

    	IPv6 endpoint address

    """

    end_point_type_ipv4 = Enum.YLeaf(1, "end-point-type-ipv4")

    end_point_type_ipv6 = Enum.YLeaf(2, "end-point-type-ipv6")


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


class PceMetric(Enum):
    """
    PceMetric (Enum Class)

    Pce metric

    .. data:: igp = 1

    	IGP metric type

    .. data:: te = 2

    	TE metric type

    """

    igp = Enum.YLeaf(1, "igp")

    te = Enum.YLeaf(2, "te")


class PcePath(Enum):
    """
    PcePath (Enum Class)

    Pce path

    .. data:: explicit = 1

    	Explicit

    .. data:: dynamic = 2

    	Dynamic

    """

    explicit = Enum.YLeaf(1, "explicit")

    dynamic = Enum.YLeaf(2, "dynamic")


class PcePathHop(Enum):
    """
    PcePathHop (Enum Class)

    Pce path hop

    .. data:: mpls = 1

    	Segment-routing MPLS

    .. data:: srv6 = 2

    	Segment-routing v6

    """

    mpls = Enum.YLeaf(1, "mpls")

    srv6 = Enum.YLeaf(2, "srv6")


class PceSegment(Enum):
    """
    PceSegment (Enum Class)

    Pce segment

    .. data:: ipv4_address = 1

    	IPv4 Address

    .. data:: mpls_label = 3

    	MPLS Label

    """

    ipv4_address = Enum.YLeaf(1, "ipv4-address")

    mpls_label = Enum.YLeaf(3, "mpls-label")


class PcerestAuthentication(Enum):
    """
    PcerestAuthentication (Enum Class)

    Pcerest authentication

    .. data:: basic = 1

    	Basic HTTP auth

    .. data:: digest = 2

    	MD5-Digest HTTP auth

    """

    basic = Enum.YLeaf(1, "basic")

    digest = Enum.YLeaf(2, "digest")



class Pce(Entity):
    """
    PCE configuration data
    
    .. attribute:: ipv6_state_syncs
    
    	Standby IPv6 PCE configuration
    	**type**\:  :py:class:`Ipv6StateSyncs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Ipv6StateSyncs>`
    
    .. attribute:: pcc_addresses
    
    	Path computation client configuration
    	**type**\:  :py:class:`PccAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses>`
    
    .. attribute:: logging
    
    	PCE logging configuration
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Logging>`
    
    .. attribute:: backoff
    
    	PCE backoff configuration
    	**type**\:  :py:class:`Backoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Backoff>`
    
    	**presence node**\: True
    
    .. attribute:: rest
    
    	REST configuration
    	**type**\:  :py:class:`Rest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Rest>`
    
    	**presence node**\: True
    
    .. attribute:: state_syncs
    
    	Standby IPv4 PCE configuration
    	**type**\:  :py:class:`StateSyncs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs>`
    
    .. attribute:: segment_routing
    
    	PCE segment\-routing configuration
    	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting>`
    
    .. attribute:: timers
    
    	PCE Timers configuration
    	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Timers>`
    
    	**presence node**\: True
    
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
    
    .. attribute:: ipv6_server_address
    
    	IPv6 address of PCE server
    	**type**\: str
    
    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: password
    
    	MD5 password
    	**type**\: str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: enable
    
    	True only
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-xtc-cfg'
    _revision = '2018-07-02'

    def __init__(self):
        super(Pce, self).__init__()
        self._top_entity = None

        self.yang_name = "pce"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv6-state-syncs", ("ipv6_state_syncs", Pce.Ipv6StateSyncs)), ("pcc-addresses", ("pcc_addresses", Pce.PccAddresses)), ("logging", ("logging", Pce.Logging)), ("backoff", ("backoff", Pce.Backoff)), ("rest", ("rest", Pce.Rest)), ("state-syncs", ("state_syncs", Pce.StateSyncs)), ("segment-routing", ("segment_routing", Pce.SegmentRouting)), ("timers", ("timers", Pce.Timers)), ("netconf", ("netconf", Pce.Netconf)), ("disjoint-path", ("disjoint_path", Pce.DisjointPath)), ("explicit-paths", ("explicit_paths", Pce.ExplicitPaths))])
        self._leafs = OrderedDict([
            ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
            ('ipv6_server_address', (YLeaf(YType.str, 'ipv6-server-address'), ['str'])),
            ('password', (YLeaf(YType.str, 'password'), ['str'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.server_address = None
        self.ipv6_server_address = None
        self.password = None
        self.enable = None

        self.ipv6_state_syncs = Pce.Ipv6StateSyncs()
        self.ipv6_state_syncs.parent = self
        self._children_name_map["ipv6_state_syncs"] = "ipv6-state-syncs"

        self.pcc_addresses = Pce.PccAddresses()
        self.pcc_addresses.parent = self
        self._children_name_map["pcc_addresses"] = "pcc-addresses"

        self.logging = Pce.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"

        self.backoff = None
        self._children_name_map["backoff"] = "backoff"

        self.rest = None
        self._children_name_map["rest"] = "rest"

        self.state_syncs = Pce.StateSyncs()
        self.state_syncs.parent = self
        self._children_name_map["state_syncs"] = "state-syncs"

        self.segment_routing = Pce.SegmentRouting()
        self.segment_routing.parent = self
        self._children_name_map["segment_routing"] = "segment-routing"

        self.timers = None
        self._children_name_map["timers"] = "timers"

        self.netconf = Pce.Netconf()
        self.netconf.parent = self
        self._children_name_map["netconf"] = "netconf"

        self.disjoint_path = Pce.DisjointPath()
        self.disjoint_path.parent = self
        self._children_name_map["disjoint_path"] = "disjoint-path"

        self.explicit_paths = Pce.ExplicitPaths()
        self.explicit_paths.parent = self
        self._children_name_map["explicit_paths"] = "explicit-paths"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pce, ['server_address', 'ipv6_server_address', 'password', 'enable'], name, value)


    class Ipv6StateSyncs(Entity):
        """
        Standby IPv6 PCE configuration
        
        .. attribute:: ipv6_state_sync
        
        	Standby PCE ipv6 address
        	**type**\: list of  		 :py:class:`Ipv6StateSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Ipv6StateSyncs.Ipv6StateSync>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Ipv6StateSyncs, self).__init__()

            self.yang_name = "ipv6-state-syncs"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6-state-sync", ("ipv6_state_sync", Pce.Ipv6StateSyncs.Ipv6StateSync))])
            self._leafs = OrderedDict()

            self.ipv6_state_sync = YList(self)
            self._segment_path = lambda: "ipv6-state-syncs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Ipv6StateSyncs, [], name, value)


        class Ipv6StateSync(Entity):
            """
            Standby PCE ipv6 address
            
            .. attribute:: address  (key)
            
            	IPv6 address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.Ipv6StateSyncs.Ipv6StateSync, self).__init__()

                self.yang_name = "ipv6-state-sync"
                self.yang_parent_name = "ipv6-state-syncs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['address']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ])
                self.address = None
                self._segment_path = lambda: "ipv6-state-sync" + "[address='" + str(self.address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/ipv6-state-syncs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.Ipv6StateSyncs.Ipv6StateSync, ['address'], name, value)


    class PccAddresses(Entity):
        """
        Path computation client configuration
        
        .. attribute:: pcc_address
        
        	Path computation client address
        	**type**\: list of  		 :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.PccAddresses.PccAddress>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.PccAddresses, self).__init__()

            self.yang_name = "pcc-addresses"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pcc-address", ("pcc_address", Pce.PccAddresses.PccAddress))])
            self._leafs = OrderedDict()

            self.pcc_address = YList(self)
            self._segment_path = lambda: "pcc-addresses"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.PccAddresses.PccAddress, self).__init__()

                self.yang_name = "pcc-address"
                self.yang_parent_name = "pcc-addresses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['address']
                self._child_classes = OrderedDict([("lsp-names", ("lsp_names", Pce.PccAddresses.PccAddress.LspNames))])
                self._leafs = OrderedDict([
                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.address = None
                self.enable = None

                self.lsp_names = Pce.PccAddresses.PccAddress.LspNames()
                self.lsp_names.parent = self
                self._children_name_map["lsp_names"] = "lsp-names"
                self._segment_path = lambda: "pcc-address" + "[address='" + str(self.address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/pcc-addresses/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.PccAddresses.PccAddress.LspNames, self).__init__()

                    self.yang_name = "lsp-names"
                    self.yang_parent_name = "pcc-address"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-name", ("lsp_name", Pce.PccAddresses.PccAddress.LspNames.LspName))])
                    self._leafs = OrderedDict()

                    self.lsp_name = YList(self)
                    self._segment_path = lambda: "lsp-names"
                    self._is_frozen = True

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
                    
                    	**presence node**\: True
                    
                    .. attribute:: undelegate
                    
                    	Undelegate LSP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: explicit_path_name
                    
                    	Explicit\-path name
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.PccAddresses.PccAddress.LspNames.LspName, self).__init__()

                        self.yang_name = "lsp-name"
                        self.yang_parent_name = "lsp-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("rsvp-te", ("rsvp_te", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('undelegate', (YLeaf(YType.empty, 'undelegate'), ['Empty'])),
                            ('explicit_path_name', (YLeaf(YType.str, 'explicit-path-name'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.name = None
                        self.undelegate = None
                        self.explicit_path_name = None
                        self.enable = None

                        self.rsvp_te = None
                        self._children_name_map["rsvp_te"] = "rsvp-te"
                        self._segment_path = lambda: "lsp-name" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

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
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: enable
                        
                        	True only
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2018-07-02'

                        def __init__(self):
                            super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe, self).__init__()

                            self.yang_name = "rsvp-te"
                            self.yang_parent_name = "lsp-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("affinity", ("affinity", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity)), ("priority", ("priority", Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('fast_protect', (YLeaf(YType.empty, 'fast-protect'), ['Empty'])),
                                ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.fast_protect = None
                            self.bandwidth = None
                            self.enable = None

                            self.affinity = Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity()
                            self.affinity.parent = self
                            self._children_name_map["affinity"] = "affinity"

                            self.priority = None
                            self._children_name_map["priority"] = "priority"
                            self._segment_path = lambda: "rsvp-te"
                            self._is_frozen = True

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
                            _revision = '2018-07-02'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity, self).__init__()

                                self.yang_name = "affinity"
                                self.yang_parent_name = "rsvp-te"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('include_any', (YLeaf(YType.str, 'include-any'), ['str'])),
                                    ('include_all', (YLeaf(YType.str, 'include-all'), ['str'])),
                                    ('exclude_any', (YLeaf(YType.str, 'exclude-any'), ['str'])),
                                ])
                                self.include_any = None
                                self.include_all = None
                                self.exclude_any = None
                                self._segment_path = lambda: "affinity"
                                self._is_frozen = True

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
                            _revision = '2018-07-02'

                            def __init__(self):
                                super(Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "rsvp-te"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('setup_priority', (YLeaf(YType.uint32, 'setup-priority'), ['int'])),
                                    ('hold_priority', (YLeaf(YType.uint32, 'hold-priority'), ['int'])),
                                ])
                                self.setup_priority = None
                                self.hold_priority = None
                                self._segment_path = lambda: "priority"
                                self._is_frozen = True

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
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('no_path', (YLeaf(YType.empty, 'no-path'), ['Empty'])),
                ('pcerr', (YLeaf(YType.empty, 'pcerr'), ['Empty'])),
                ('fallback', (YLeaf(YType.empty, 'fallback'), ['Empty'])),
            ])
            self.no_path = None
            self.pcerr = None
            self.fallback = None
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Backoff, self).__init__()

            self.yang_name = "backoff"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('ratio', (YLeaf(YType.uint32, 'ratio'), ['int'])),
                ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                ('difference', (YLeaf(YType.uint32, 'difference'), ['int'])),
            ])
            self.ratio = None
            self.threshold = None
            self.difference = None
            self._segment_path = lambda: "backoff"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Backoff, ['ratio', 'threshold', 'difference'], name, value)


    class Rest(Entity):
        """
        REST configuration
        
        .. attribute:: rest_users
        
        	REST authorized users configuration
        	**type**\:  :py:class:`RestUsers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Rest.RestUsers>`
        
        .. attribute:: rest_authentication
        
        	REST authentication type
        	**type**\:  :py:class:`PcerestAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PcerestAuthentication>`
        
        	**mandatory**\: True
        
        .. attribute:: enable
        
        	True only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Rest, self).__init__()

            self.yang_name = "rest"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rest-users", ("rest_users", Pce.Rest.RestUsers))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('rest_authentication', (YLeaf(YType.enumeration, 'rest-authentication'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PcerestAuthentication', '')])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.rest_authentication = None
            self.enable = None

            self.rest_users = Pce.Rest.RestUsers()
            self.rest_users.parent = self
            self._children_name_map["rest_users"] = "rest-users"
            self._segment_path = lambda: "rest"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Rest, ['rest_authentication', 'enable'], name, value)


        class RestUsers(Entity):
            """
            REST authorized users configuration
            
            .. attribute:: rest_user
            
            	REST authorized user
            	**type**\: list of  		 :py:class:`RestUser <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Rest.RestUsers.RestUser>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.Rest.RestUsers, self).__init__()

                self.yang_name = "rest-users"
                self.yang_parent_name = "rest"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rest-user", ("rest_user", Pce.Rest.RestUsers.RestUser))])
                self._leafs = OrderedDict()

                self.rest_user = YList(self)
                self._segment_path = lambda: "rest-users"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/rest/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.Rest.RestUsers, [], name, value)


            class RestUser(Entity):
                """
                REST authorized user
                
                .. attribute:: name  (key)
                
                	User name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rest_user_password
                
                	REST user password configuration
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                	**mandatory**\: True
                
                .. attribute:: enable
                
                	True only
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.Rest.RestUsers.RestUser, self).__init__()

                    self.yang_name = "rest-user"
                    self.yang_parent_name = "rest-users"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('rest_user_password', (YLeaf(YType.str, 'rest-user-password'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.name = None
                    self.rest_user_password = None
                    self.enable = None
                    self._segment_path = lambda: "rest-user" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/rest/rest-users/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.Rest.RestUsers.RestUser, ['name', 'rest_user_password', 'enable'], name, value)


    class StateSyncs(Entity):
        """
        Standby IPv4 PCE configuration
        
        .. attribute:: state_sync
        
        	Standby PCE ipv4 address
        	**type**\: list of  		 :py:class:`StateSync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.StateSyncs.StateSync>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.StateSyncs, self).__init__()

            self.yang_name = "state-syncs"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("state-sync", ("state_sync", Pce.StateSyncs.StateSync))])
            self._leafs = OrderedDict()

            self.state_sync = YList(self)
            self._segment_path = lambda: "state-syncs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.StateSyncs.StateSync, self).__init__()

                self.yang_name = "state-sync"
                self.yang_parent_name = "state-syncs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['address']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                ])
                self.address = None
                self._segment_path = lambda: "state-sync" + "[address='" + str(self.address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/state-syncs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.StateSyncs.StateSync, ['address'], name, value)


    class SegmentRouting(Entity):
        """
        PCE segment\-routing configuration
        
        .. attribute:: traffic_engineering
        
        	Traffic Engineering configuration data
        	**type**\:  :py:class:`TrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering>`
        
        .. attribute:: te_latency
        
        	Use te\-latency algorithm configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: strict_sid_only
        
        	Use strict\-sid\-only configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.SegmentRouting, self).__init__()

            self.yang_name = "segment-routing"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("traffic-engineering", ("traffic_engineering", Pce.SegmentRouting.TrafficEngineering))])
            self._leafs = OrderedDict([
                ('te_latency', (YLeaf(YType.empty, 'te-latency'), ['Empty'])),
                ('strict_sid_only', (YLeaf(YType.empty, 'strict-sid-only'), ['Empty'])),
            ])
            self.te_latency = None
            self.strict_sid_only = None

            self.traffic_engineering = Pce.SegmentRouting.TrafficEngineering()
            self.traffic_engineering.parent = self
            self._children_name_map["traffic_engineering"] = "traffic-engineering"
            self._segment_path = lambda: "segment-routing"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.SegmentRouting, ['te_latency', 'strict_sid_only'], name, value)


        class TrafficEngineering(Entity):
            """
            Traffic Engineering configuration data
            
            .. attribute:: affinity_bits
            
            	Affinity Bit\-map
            	**type**\:  :py:class:`AffinityBits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.AffinityBits>`
            
            .. attribute:: peers
            
            	Peer configuration
            	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers>`
            
            .. attribute:: segments
            
            	Segment\-lists configuration
            	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Segments>`
            
            .. attribute:: enable
            
            	True only
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-xtc-cfg'
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.SegmentRouting.TrafficEngineering, self).__init__()

                self.yang_name = "traffic-engineering"
                self.yang_parent_name = "segment-routing"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("affinity-bits", ("affinity_bits", Pce.SegmentRouting.TrafficEngineering.AffinityBits)), ("peers", ("peers", Pce.SegmentRouting.TrafficEngineering.Peers)), ("segments", ("segments", Pce.SegmentRouting.TrafficEngineering.Segments))])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None

                self.affinity_bits = Pce.SegmentRouting.TrafficEngineering.AffinityBits()
                self.affinity_bits.parent = self
                self._children_name_map["affinity_bits"] = "affinity-bits"

                self.peers = Pce.SegmentRouting.TrafficEngineering.Peers()
                self.peers.parent = self
                self._children_name_map["peers"] = "peers"

                self.segments = Pce.SegmentRouting.TrafficEngineering.Segments()
                self.segments.parent = self
                self._children_name_map["segments"] = "segments"
                self._segment_path = lambda: "traffic-engineering"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.SegmentRouting.TrafficEngineering, ['enable'], name, value)


            class AffinityBits(Entity):
                """
                Affinity Bit\-map
                
                .. attribute:: affinity_bit
                
                	Affinity Bit
                	**type**\: list of  		 :py:class:`AffinityBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.AffinityBits.AffinityBit>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.SegmentRouting.TrafficEngineering.AffinityBits, self).__init__()

                    self.yang_name = "affinity-bits"
                    self.yang_parent_name = "traffic-engineering"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("affinity-bit", ("affinity_bit", Pce.SegmentRouting.TrafficEngineering.AffinityBits.AffinityBit))])
                    self._leafs = OrderedDict()

                    self.affinity_bit = YList(self)
                    self._segment_path = lambda: "affinity-bits"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.AffinityBits, [], name, value)


                class AffinityBit(Entity):
                    """
                    Affinity Bit
                    
                    .. attribute:: color_name  (key)
                    
                    	Color Name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: bit
                    
                    	The bit
                    	**type**\: int
                    
                    	**range:** 0..31
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.SegmentRouting.TrafficEngineering.AffinityBits.AffinityBit, self).__init__()

                        self.yang_name = "affinity-bit"
                        self.yang_parent_name = "affinity-bits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['color_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('color_name', (YLeaf(YType.str, 'color-name'), ['str'])),
                            ('bit', (YLeaf(YType.uint32, 'bit'), ['int'])),
                        ])
                        self.color_name = None
                        self.bit = None
                        self._segment_path = lambda: "affinity-bit" + "[color-name='" + str(self.color_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/affinity-bits/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.AffinityBits.AffinityBit, ['color_name', 'bit'], name, value)


            class Peers(Entity):
                """
                Peer configuration
                
                .. attribute:: peer
                
                	Peer configuration
                	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.SegmentRouting.TrafficEngineering.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "traffic-engineering"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer", ("peer", Pce.SegmentRouting.TrafficEngineering.Peers.Peer))])
                    self._leafs = OrderedDict()

                    self.peer = YList(self)
                    self._segment_path = lambda: "peers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers, [], name, value)


                class Peer(Entity):
                    """
                    Peer configuration
                    
                    .. attribute:: peer_addr  (key)
                    
                    	Peer address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: policies
                    
                    	Policy configuration
                    	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies>`
                    
                    .. attribute:: enable
                    
                    	True only
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['peer_addr']
                        self._child_classes = OrderedDict([("policies", ("policies", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies))])
                        self._leafs = OrderedDict([
                            ('peer_addr', (YLeaf(YType.str, 'peer-addr'), ['str','str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.peer_addr = None
                        self.enable = None

                        self.policies = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies()
                        self.policies.parent = self
                        self._children_name_map["policies"] = "policies"
                        self._segment_path = lambda: "peer" + "[peer-addr='" + str(self.peer_addr) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/peers/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer, ['peer_addr', 'enable'], name, value)


                    class Policies(Entity):
                        """
                        Policy configuration
                        
                        .. attribute:: policy
                        
                        	Policy configuration
                        	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy>`
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2018-07-02'

                        def __init__(self):
                            super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies, self).__init__()

                            self.yang_name = "policies"
                            self.yang_parent_name = "peer"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("policy", ("policy", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy))])
                            self._leafs = OrderedDict()

                            self.policy = YList(self)
                            self._segment_path = lambda: "policies"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies, [], name, value)


                        class Policy(Entity):
                            """
                            Policy configuration
                            
                            .. attribute:: policy_name  (key)
                            
                            	Policy name
                            	**type**\: str
                            
                            	**length:** 1..128
                            
                            .. attribute:: binding_sid
                            
                            	Binding Segment ID
                            	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.BindingSid>`
                            
                            .. attribute:: color_endpoint
                            
                            	Color and Endpoint
                            	**type**\:  :py:class:`ColorEndpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.ColorEndpoint>`
                            
                            .. attribute:: candidate_paths
                            
                            	Policy candidate\-paths configuration
                            	**type**\:  :py:class:`CandidatePaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths>`
                            
                            .. attribute:: enable
                            
                            	True only
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: shutdown
                            
                            	Administratively shutdown policy
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2018-07-02'

                            def __init__(self):
                                super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy, self).__init__()

                                self.yang_name = "policy"
                                self.yang_parent_name = "policies"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['policy_name']
                                self._child_classes = OrderedDict([("binding-sid", ("binding_sid", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.BindingSid)), ("color-endpoint", ("color_endpoint", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.ColorEndpoint)), ("candidate-paths", ("candidate_paths", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths))])
                                self._leafs = OrderedDict([
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ('shutdown', (YLeaf(YType.empty, 'shutdown'), ['Empty'])),
                                ])
                                self.policy_name = None
                                self.enable = None
                                self.shutdown = None

                                self.binding_sid = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.BindingSid()
                                self.binding_sid.parent = self
                                self._children_name_map["binding_sid"] = "binding-sid"

                                self.color_endpoint = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.ColorEndpoint()
                                self.color_endpoint.parent = self
                                self._children_name_map["color_endpoint"] = "color-endpoint"

                                self.candidate_paths = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths()
                                self.candidate_paths.parent = self
                                self._children_name_map["candidate_paths"] = "candidate-paths"
                                self._segment_path = lambda: "policy" + "[policy-name='" + str(self.policy_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy, ['policy_name', 'enable', 'shutdown'], name, value)


                            class BindingSid(Entity):
                                """
                                Binding Segment ID
                                
                                .. attribute:: binding_sid_type
                                
                                	Binding SID type
                                	**type**\:  :py:class:`PceBindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceBindingSid>`
                                
                                .. attribute:: mpls_label
                                
                                	MPLS Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                

                                """

                                _prefix = 'infra-xtc-cfg'
                                _revision = '2018-07-02'

                                def __init__(self):
                                    super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.BindingSid, self).__init__()

                                    self.yang_name = "binding-sid"
                                    self.yang_parent_name = "policy"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('binding_sid_type', (YLeaf(YType.enumeration, 'binding-sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceBindingSid', '')])),
                                        ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                                    ])
                                    self.binding_sid_type = None
                                    self.mpls_label = None
                                    self._segment_path = lambda: "binding-sid"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.BindingSid, ['binding_sid_type', 'mpls_label'], name, value)


                            class ColorEndpoint(Entity):
                                """
                                Color and Endpoint
                                
                                .. attribute:: color
                                
                                	Color
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: end_point_type
                                
                                	End point type
                                	**type**\:  :py:class:`PceEndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceEndPoint>`
                                
                                .. attribute:: end_point_address
                                
                                	End point address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-cfg'
                                _revision = '2018-07-02'

                                def __init__(self):
                                    super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.ColorEndpoint, self).__init__()

                                    self.yang_name = "color-endpoint"
                                    self.yang_parent_name = "policy"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                                        ('end_point_type', (YLeaf(YType.enumeration, 'end-point-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceEndPoint', '')])),
                                        ('end_point_address', (YLeaf(YType.str, 'end-point-address'), ['str','str'])),
                                    ])
                                    self.color = None
                                    self.end_point_type = None
                                    self.end_point_address = None
                                    self._segment_path = lambda: "color-endpoint"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.ColorEndpoint, ['color', 'end_point_type', 'end_point_address'], name, value)


                            class CandidatePaths(Entity):
                                """
                                Policy candidate\-paths configuration
                                
                                .. attribute:: affinity_rules
                                
                                	Affinity rule table
                                	**type**\:  :py:class:`AffinityRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules>`
                                
                                .. attribute:: preferences
                                
                                	Policy path\-option preference table
                                	**type**\:  :py:class:`Preferences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences>`
                                
                                .. attribute:: enable
                                
                                	True only
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'infra-xtc-cfg'
                                _revision = '2018-07-02'

                                def __init__(self):
                                    super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths, self).__init__()

                                    self.yang_name = "candidate-paths"
                                    self.yang_parent_name = "policy"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("affinity-rules", ("affinity_rules", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules)), ("preferences", ("preferences", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences))])
                                    self._leafs = OrderedDict([
                                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ])
                                    self.enable = None

                                    self.affinity_rules = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules()
                                    self.affinity_rules.parent = self
                                    self._children_name_map["affinity_rules"] = "affinity-rules"

                                    self.preferences = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences()
                                    self.preferences.parent = self
                                    self._children_name_map["preferences"] = "preferences"
                                    self._segment_path = lambda: "candidate-paths"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths, ['enable'], name, value)


                                class AffinityRules(Entity):
                                    """
                                    Affinity rule table
                                    
                                    .. attribute:: affinity_rule
                                    
                                    	Affinity rule
                                    	**type**\: list of  		 :py:class:`AffinityRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules.AffinityRule>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-cfg'
                                    _revision = '2018-07-02'

                                    def __init__(self):
                                        super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules, self).__init__()

                                        self.yang_name = "affinity-rules"
                                        self.yang_parent_name = "candidate-paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("affinity-rule", ("affinity_rule", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules.AffinityRule))])
                                        self._leafs = OrderedDict()

                                        self.affinity_rule = YList(self)
                                        self._segment_path = lambda: "affinity-rules"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules, [], name, value)


                                    class AffinityRule(Entity):
                                        """
                                        Affinity rule
                                        
                                        .. attribute:: rule  (key)
                                        
                                        	affinity rule
                                        	**type**\: int
                                        
                                        	**range:** 0..2
                                        
                                        .. attribute:: aff_value  (key)
                                        
                                        	affinity value
                                        	**type**\: str
                                        
                                        	**length:** 1..32
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-cfg'
                                        _revision = '2018-07-02'

                                        def __init__(self):
                                            super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules.AffinityRule, self).__init__()

                                            self.yang_name = "affinity-rule"
                                            self.yang_parent_name = "affinity-rules"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['rule','aff_value']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rule', (YLeaf(YType.uint32, 'rule'), ['int'])),
                                                ('aff_value', (YLeaf(YType.str, 'aff-value'), ['str'])),
                                            ])
                                            self.rule = None
                                            self.aff_value = None
                                            self._segment_path = lambda: "affinity-rule" + "[rule='" + str(self.rule) + "']" + "[aff-value='" + str(self.aff_value) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.AffinityRules.AffinityRule, ['rule', 'aff_value'], name, value)


                                class Preferences(Entity):
                                    """
                                    Policy path\-option preference table
                                    
                                    .. attribute:: preference
                                    
                                    	Policy path\-option preference entry
                                    	**type**\: list of  		 :py:class:`Preference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference>`
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-cfg'
                                    _revision = '2018-07-02'

                                    def __init__(self):
                                        super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences, self).__init__()

                                        self.yang_name = "preferences"
                                        self.yang_parent_name = "candidate-paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("preference", ("preference", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference))])
                                        self._leafs = OrderedDict()

                                        self.preference = YList(self)
                                        self._segment_path = lambda: "preferences"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences, [], name, value)


                                    class Preference(Entity):
                                        """
                                        Policy path\-option preference entry
                                        
                                        .. attribute:: path_index  (key)
                                        
                                        	Path\-option preference
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: path_infos
                                        
                                        	Policy path\-option preference configuration
                                        	**type**\:  :py:class:`PathInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos>`
                                        
                                        .. attribute:: enable
                                        
                                        	True only
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'infra-xtc-cfg'
                                        _revision = '2018-07-02'

                                        def __init__(self):
                                            super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference, self).__init__()

                                            self.yang_name = "preference"
                                            self.yang_parent_name = "preferences"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['path_index']
                                            self._child_classes = OrderedDict([("path-infos", ("path_infos", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos))])
                                            self._leafs = OrderedDict([
                                                ('path_index', (YLeaf(YType.uint32, 'path-index'), ['int'])),
                                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                            ])
                                            self.path_index = None
                                            self.enable = None

                                            self.path_infos = Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos()
                                            self.path_infos.parent = self
                                            self._children_name_map["path_infos"] = "path-infos"
                                            self._segment_path = lambda: "preference" + "[path-index='" + str(self.path_index) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference, ['path_index', 'enable'], name, value)


                                        class PathInfos(Entity):
                                            """
                                            Policy path\-option preference
                                            configuration
                                            
                                            .. attribute:: path_info
                                            
                                            	Policy configuration
                                            	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo>`
                                            
                                            

                                            """

                                            _prefix = 'infra-xtc-cfg'
                                            _revision = '2018-07-02'

                                            def __init__(self):
                                                super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, self).__init__()

                                                self.yang_name = "path-infos"
                                                self.yang_parent_name = "preference"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("path-info", ("path_info", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo))])
                                                self._leafs = OrderedDict()

                                                self.path_info = YList(self)
                                                self._segment_path = lambda: "path-infos"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos, [], name, value)


                                            class PathInfo(Entity):
                                                """
                                                Policy configuration
                                                
                                                .. attribute:: type  (key)
                                                
                                                	Path\-option type
                                                	**type**\:  :py:class:`PcePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PcePath>`
                                                
                                                .. attribute:: hop_type  (key)
                                                
                                                	Type of dynamic path to be computed
                                                	**type**\:  :py:class:`PcePathHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PcePathHop>`
                                                
                                                .. attribute:: segment_list_name  (key)
                                                
                                                	Segment\-list name
                                                	**type**\: str
                                                
                                                	**length:** 1..128
                                                
                                                .. attribute:: metric
                                                
                                                	Metric configuration, valid only for dynamic path\-options
                                                	**type**\:  :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric>`
                                                
                                                	**presence node**\: True
                                                
                                                .. attribute:: enable
                                                
                                                	True only
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                

                                                """

                                                _prefix = 'infra-xtc-cfg'
                                                _revision = '2018-07-02'

                                                def __init__(self):
                                                    super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, self).__init__()

                                                    self.yang_name = "path-info"
                                                    self.yang_parent_name = "path-infos"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['type','hop_type','segment_list_name']
                                                    self._child_classes = OrderedDict([("metric", ("metric", Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric))])
                                                    self._leafs = OrderedDict([
                                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PcePath', '')])),
                                                        ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PcePathHop', '')])),
                                                        ('segment_list_name', (YLeaf(YType.str, 'segment-list-name'), ['str'])),
                                                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                                    ])
                                                    self.type = None
                                                    self.hop_type = None
                                                    self.segment_list_name = None
                                                    self.enable = None

                                                    self.metric = None
                                                    self._children_name_map["metric"] = "metric"
                                                    self._segment_path = lambda: "path-info" + "[type='" + str(self.type) + "']" + "[hop-type='" + str(self.hop_type) + "']" + "[segment-list-name='" + str(self.segment_list_name) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo, ['type', 'hop_type', 'segment_list_name', 'enable'], name, value)


                                                class Metric(Entity):
                                                    """
                                                    Metric configuration, valid only for
                                                    dynamic path\-options
                                                    
                                                    .. attribute:: metric_type
                                                    
                                                    	Metric type
                                                    	**type**\:  :py:class:`PceMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceMetric>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    

                                                    This class is a :ref:`presence class<presence-class>`

                                                    """

                                                    _prefix = 'infra-xtc-cfg'
                                                    _revision = '2018-07-02'

                                                    def __init__(self):
                                                        super(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, self).__init__()

                                                        self.yang_name = "metric"
                                                        self.yang_parent_name = "path-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self.is_presence_container = True
                                                        self._leafs = OrderedDict([
                                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceMetric', '')])),
                                                        ])
                                                        self.metric_type = None
                                                        self._segment_path = lambda: "metric"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Peers.Peer.Policies.Policy.CandidatePaths.Preferences.Preference.PathInfos.PathInfo.Metric, ['metric_type'], name, value)


            class Segments(Entity):
                """
                Segment\-lists configuration
                
                .. attribute:: segment
                
                	Segment\-list configuration
                	**type**\: list of  		 :py:class:`Segment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Segments.Segment>`
                
                

                """

                _prefix = 'infra-xtc-cfg'
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.SegmentRouting.TrafficEngineering.Segments, self).__init__()

                    self.yang_name = "segments"
                    self.yang_parent_name = "traffic-engineering"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("segment", ("segment", Pce.SegmentRouting.TrafficEngineering.Segments.Segment))])
                    self._leafs = OrderedDict()

                    self.segment = YList(self)
                    self._segment_path = lambda: "segments"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Segments, [], name, value)


                class Segment(Entity):
                    """
                    Segment\-list configuration
                    
                    .. attribute:: path_name  (key)
                    
                    	Segment\-list name
                    	**type**\: str
                    
                    	**length:** 1..128
                    
                    .. attribute:: segments
                    
                    	Segments/hops configuration for given Segment\-list
                    	**type**\:  :py:class:`Segments_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_>`
                    
                    

                    """

                    _prefix = 'infra-xtc-cfg'
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.SegmentRouting.TrafficEngineering.Segments.Segment, self).__init__()

                        self.yang_name = "segment"
                        self.yang_parent_name = "segments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['path_name']
                        self._child_classes = OrderedDict([("segments", ("segments", Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_))])
                        self._leafs = OrderedDict([
                            ('path_name', (YLeaf(YType.str, 'path-name'), ['str'])),
                        ])
                        self.path_name = None

                        self.segments = Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_()
                        self.segments.parent = self
                        self._children_name_map["segments"] = "segments"
                        self._segment_path = lambda: "segment" + "[path-name='" + str(self.path_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/segment-routing/traffic-engineering/segments/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Segments.Segment, ['path_name'], name, value)


                    class Segments_(Entity):
                        """
                        Segments/hops configuration for given
                        Segment\-list
                        
                        .. attribute:: segment
                        
                        	Configure Segment/hop at the index
                        	**type**\: list of  		 :py:class:`Segment_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_.Segment_>`
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2018-07-02'

                        def __init__(self):
                            super(Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_, self).__init__()

                            self.yang_name = "segments"
                            self.yang_parent_name = "segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("segment", ("segment", Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_.Segment_))])
                            self._leafs = OrderedDict()

                            self.segment = YList(self)
                            self._segment_path = lambda: "segments"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_, [], name, value)


                        class Segment_(Entity):
                            """
                            Configure Segment/hop at the index
                            
                            .. attribute:: segment_index  (key)
                            
                            	Segment index
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: segment_type
                            
                            	Segment/hop type
                            	**type**\:  :py:class:`PceSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.PceSegment>`
                            
                            .. attribute:: address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mpls_label
                            
                            	MPLS Label
                            	**type**\: int
                            
                            	**range:** 0..1048575
                            
                            

                            """

                            _prefix = 'infra-xtc-cfg'
                            _revision = '2018-07-02'

                            def __init__(self):
                                super(Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_.Segment_, self).__init__()

                                self.yang_name = "segment"
                                self.yang_parent_name = "segments"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['segment_index']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('segment_index', (YLeaf(YType.uint32, 'segment-index'), ['int'])),
                                    ('segment_type', (YLeaf(YType.enumeration, 'segment-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceSegment', '')])),
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                                ])
                                self.segment_index = None
                                self.segment_type = None
                                self.address = None
                                self.mpls_label = None
                                self._segment_path = lambda: "segment" + "[segment-index='" + str(self.segment_index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.SegmentRouting.TrafficEngineering.Segments.Segment.Segments_.Segment_, ['segment_index', 'segment_type', 'address', 'mpls_label'], name, value)


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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Timers, self).__init__()

            self.yang_name = "timers"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('reoptimization_timer', (YLeaf(YType.uint32, 'reoptimization-timer'), ['int'])),
                ('keepalive', (YLeaf(YType.uint32, 'keepalive'), ['int'])),
                ('minimum_peer_keepalive', (YLeaf(YType.uint32, 'minimum-peer-keepalive'), ['int'])),
            ])
            self.reoptimization_timer = None
            self.keepalive = None
            self.minimum_peer_keepalive = None
            self._segment_path = lambda: "timers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Timers, ['reoptimization_timer', 'keepalive', 'minimum_peer_keepalive'], name, value)


    class Netconf(Entity):
        """
        NETCONF configuration
        
        .. attribute:: netconf_ssh
        
        	NETCONF SSH configuration
        	**type**\:  :py:class:`NetconfSsh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg.Pce.Netconf.NetconfSsh>`
        
        .. attribute:: enable
        
        	True only
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-xtc-cfg'
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.Netconf, self).__init__()

            self.yang_name = "netconf"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("netconf-ssh", ("netconf_ssh", Pce.Netconf.NetconfSsh))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.netconf_ssh = Pce.Netconf.NetconfSsh()
            self.netconf_ssh.parent = self
            self._children_name_map["netconf_ssh"] = "netconf-ssh"
            self._segment_path = lambda: "netconf"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Netconf, ['enable'], name, value)


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
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.Netconf.NetconfSsh, self).__init__()

                self.yang_name = "netconf-ssh"
                self.yang_parent_name = "netconf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('netconf_ssh_password', (YLeaf(YType.str, 'netconf-ssh-password'), ['str'])),
                    ('netconf_ssh_user', (YLeaf(YType.str, 'netconf-ssh-user'), ['str'])),
                ])
                self.netconf_ssh_password = None
                self.netconf_ssh_user = None
                self._segment_path = lambda: "netconf-ssh"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/netconf/%s" % self._segment_path()
                self._is_frozen = True

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
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.DisjointPath, self).__init__()

            self.yang_name = "disjoint-path"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("groups", ("groups", Pce.DisjointPath.Groups))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.groups = Pce.DisjointPath.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._segment_path = lambda: "disjoint-path"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.DisjointPath.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "disjoint-path"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("group", ("group", Pce.DisjointPath.Groups.Group))])
                self._leafs = OrderedDict()

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.DisjointPath.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['group_id','dp_type','sub_id']
                    self._child_classes = OrderedDict([("group-lsp-records", ("group_lsp_records", Pce.DisjointPath.Groups.Group.GroupLspRecords))])
                    self._leafs = OrderedDict([
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                        ('dp_type', (YLeaf(YType.enumeration, 'dp-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceDisjointPath', '')])),
                        ('sub_id', (YLeaf(YType.uint32, 'sub-id'), ['int'])),
                        ('strict', (YLeaf(YType.empty, 'strict'), ['Empty'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.group_id = None
                    self.dp_type = None
                    self.sub_id = None
                    self.strict = None
                    self.enable = None

                    self.group_lsp_records = Pce.DisjointPath.Groups.Group.GroupLspRecords()
                    self.group_lsp_records.parent = self
                    self._children_name_map["group_lsp_records"] = "group-lsp-records"
                    self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']" + "[dp-type='" + str(self.dp_type) + "']" + "[sub-id='" + str(self.sub_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/disjoint-path/groups/%s" % self._segment_path()
                    self._is_frozen = True

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
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.DisjointPath.Groups.Group.GroupLspRecords, self).__init__()

                        self.yang_name = "group-lsp-records"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("group-lsp-record", ("group_lsp_record", Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord))])
                        self._leafs = OrderedDict()

                        self.group_lsp_record = YList(self)
                        self._segment_path = lambda: "group-lsp-records"
                        self._is_frozen = True

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
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-cfg'
                        _revision = '2018-07-02'

                        def __init__(self):
                            super(Pce.DisjointPath.Groups.Group.GroupLspRecords.GroupLspRecord, self).__init__()

                            self.yang_name = "group-lsp-record"
                            self.yang_parent_name = "group-lsp-records"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsp_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('lsp_id', (YLeaf(YType.uint32, 'lsp-id'), ['int'])),
                                ('ip_addr', (YLeaf(YType.str, 'ip-addr'), ['str'])),
                                ('lsp_name', (YLeaf(YType.str, 'lsp-name'), ['str'])),
                                ('disj_path', (YLeaf(YType.uint32, 'disj-path'), ['int'])),
                            ])
                            self.lsp_id = None
                            self.ip_addr = None
                            self.lsp_name = None
                            self.disj_path = None
                            self._segment_path = lambda: "group-lsp-record" + "[lsp-id='" + str(self.lsp_id) + "']"
                            self._is_frozen = True

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
        _revision = '2018-07-02'

        def __init__(self):
            super(Pce.ExplicitPaths, self).__init__()

            self.yang_name = "explicit-paths"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("explicit-path", ("explicit_path", Pce.ExplicitPaths.ExplicitPath))])
            self._leafs = OrderedDict()

            self.explicit_path = YList(self)
            self._segment_path = lambda: "explicit-paths"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/%s" % self._segment_path()
            self._is_frozen = True

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
            _revision = '2018-07-02'

            def __init__(self):
                super(Pce.ExplicitPaths.ExplicitPath, self).__init__()

                self.yang_name = "explicit-path"
                self.yang_parent_name = "explicit-paths"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("path-hops", ("path_hops", Pce.ExplicitPaths.ExplicitPath.PathHops))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.name = None
                self.enable = None

                self.path_hops = Pce.ExplicitPaths.ExplicitPath.PathHops()
                self.path_hops.parent = self
                self._children_name_map["path_hops"] = "path-hops"
                self._segment_path = lambda: "explicit-path" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-cfg:pce/explicit-paths/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2018-07-02'

                def __init__(self):
                    super(Pce.ExplicitPaths.ExplicitPath.PathHops, self).__init__()

                    self.yang_name = "path-hops"
                    self.yang_parent_name = "explicit-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("path-hop", ("path_hop", Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop))])
                    self._leafs = OrderedDict()

                    self.path_hop = YList(self)
                    self._segment_path = lambda: "path-hops"
                    self._is_frozen = True

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
                    _revision = '2018-07-02'

                    def __init__(self):
                        super(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, self).__init__()

                        self.yang_name = "path-hop"
                        self.yang_parent_name = "path-hops"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                            ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceExplicitPathHop', '')])),
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('remote_address', (YLeaf(YType.str, 'remote-address'), ['str'])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                        ])
                        self.index = None
                        self.hop_type = None
                        self.address = None
                        self.remote_address = None
                        self.mpls_label = None
                        self._segment_path = lambda: "path-hop" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop, ['index', 'hop_type', 'address', 'remote_address', 'mpls_label'], name, value)

    def clone_ptr(self):
        self._top_entity = Pce()
        return self._top_entity

