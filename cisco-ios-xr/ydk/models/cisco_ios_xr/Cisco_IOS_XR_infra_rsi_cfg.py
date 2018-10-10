""" Cisco_IOS_XR_infra_rsi_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package configuration.

This module contains definitions
for the following management objects\:
  vrfs\: VRF configuration
  global\-af\: global af
  srlg\: srlg
  vrf\-groups\: vrf groups
  selective\-vrf\-download\: selective vrf download

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SrlgPriority(Enum):
    """
    SrlgPriority (Enum Class)

    Srlg priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: default = 2

    	Default

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    default = Enum.YLeaf(2, "default")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")


class VrfAddressFamily(Enum):
    """
    VrfAddressFamily (Enum Class)

    Vrf address family

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class VrfSubAddressFamily(Enum):
    """
    VrfSubAddressFamily (Enum Class)

    Vrf sub address family

    .. data:: unicast = 1

    	Unicast

    .. data:: multicast = 2

    	Multicast

    .. data:: flow_spec = 133

    	Flow spec

    """

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    flow_spec = Enum.YLeaf(133, "flow-spec")



class Vrfs(Entity):
    """
    VRF configuration
    
    .. attribute:: vrf
    
    	VRF configuration
    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Vrfs, self).__init__()
        self._top_entity = None

        self.yang_name = "vrfs"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf", ("vrf", Vrfs.Vrf))])
        self._leafs = OrderedDict()

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrfs"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vrfs, [], name, value)


    class Vrf(Entity):
        """
        VRF configuration
        
        .. attribute:: vrf_name  (key)
        
        	VRF name
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: vpn_id
        
        	VPN\-ID for the VRF
        	**type**\:  :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.VpnId>`
        
        	**presence node**\: True
        
        .. attribute:: fallback_vrf
        
        	Fallback VRF
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: remote_route_filter_disable
        
        	For disabling remote route filtering for this VRF on core\-facing card
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: create
        
        	VRF global configuration
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: mode_big
        
        	Configuration enable of big VRF
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: description
        
        	A textual description of the VRF
        	**type**\: str
        
        	**length:** 1..244
        
        .. attribute:: afs
        
        	VRF address family configuration
        	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs>`
        
        .. attribute:: bgp_global
        
        	BGP related VRF Global config
        	**type**\:  :py:class:`BgpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.BgpGlobal>`
        
        .. attribute:: multicast_host
        
        	Multicast host stack configuration
        	**type**\:  :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Vrfs.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "vrfs"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf_name']
            self._child_classes = OrderedDict([("vpn-id", ("vpn_id", Vrfs.Vrf.VpnId)), ("afs", ("afs", Vrfs.Vrf.Afs)), ("Cisco-IOS-XR-ipv4-bgp-cfg:bgp-global", ("bgp_global", Vrfs.Vrf.BgpGlobal)), ("Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host", ("multicast_host", Vrfs.Vrf.MulticastHost))])
            self._leafs = OrderedDict([
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ('fallback_vrf', (YLeaf(YType.str, 'fallback-vrf'), ['str'])),
                ('remote_route_filter_disable', (YLeaf(YType.empty, 'remote-route-filter-disable'), ['Empty'])),
                ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                ('mode_big', (YLeaf(YType.empty, 'mode-big'), ['Empty'])),
                ('description', (YLeaf(YType.str, 'description'), ['str'])),
            ])
            self.vrf_name = None
            self.fallback_vrf = None
            self.remote_route_filter_disable = None
            self.create = None
            self.mode_big = None
            self.description = None

            self.vpn_id = None
            self._children_name_map["vpn_id"] = "vpn-id"

            self.afs = Vrfs.Vrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"

            self.bgp_global = Vrfs.Vrf.BgpGlobal()
            self.bgp_global.parent = self
            self._children_name_map["bgp_global"] = "Cisco-IOS-XR-ipv4-bgp-cfg:bgp-global"

            self.multicast_host = Vrfs.Vrf.MulticastHost()
            self.multicast_host.parent = self
            self._children_name_map["multicast_host"] = "Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host"
            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrfs/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vrfs.Vrf, [u'vrf_name', u'fallback_vrf', u'remote_route_filter_disable', u'create', u'mode_big', u'description'], name, value)


        class VpnId(Entity):
            """
            VPN\-ID for the VRF
            
            .. attribute:: vpn_oui
            
            	OUI of VPNID OUI
            	**type**\: int
            
            	**range:** 0..16777215
            
            	**mandatory**\: True
            
            .. attribute:: vpn_index
            
            	Index of VPNID Index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Vrfs.Vrf.VpnId, self).__init__()

                self.yang_name = "vpn-id"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('vpn_oui', (YLeaf(YType.uint32, 'vpn-oui'), ['int'])),
                    ('vpn_index', (YLeaf(YType.uint32, 'vpn-index'), ['int'])),
                ])
                self.vpn_oui = None
                self.vpn_index = None
                self._segment_path = lambda: "vpn-id"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.VpnId, [u'vpn_oui', u'vpn_index'], name, value)


        class Afs(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af
            
            	VRF address family configuration
            	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Vrfs.Vrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("af", ("af", Vrfs.Vrf.Afs.Af))])
                self._leafs = OrderedDict()

                self.af = YList(self)
                self._segment_path = lambda: "afs"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.Afs, [], name, value)


            class Af(Entity):
                """
                VRF address family configuration
                
                .. attribute:: af_name  (key)
                
                	Address family
                	**type**\:  :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
                
                .. attribute:: saf_name  (key)
                
                	Sub\-Address family
                	**type**\:  :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
                
                .. attribute:: topology_name  (key)
                
                	Topology name
                	**type**\: str
                
                	**length:** 1..244
                
                .. attribute:: create
                
                	VRF configuration for a particular address family
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum_prefix
                
                	Set maximum prefix limits
                	**type**\:  :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.MaximumPrefix>`
                
                	**presence node**\: True
                
                .. attribute:: bgp
                
                	BGP AF VRF config
                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Vrfs.Vrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['af_name','saf_name','topology_name']
                    self._child_classes = OrderedDict([("Cisco-IOS-XR-ip-rib-cfg:maximum-prefix", ("maximum_prefix", Vrfs.Vrf.Afs.Af.MaximumPrefix)), ("Cisco-IOS-XR-ipv4-bgp-cfg:bgp", ("bgp", Vrfs.Vrf.Afs.Af.Bgp))])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamily', '')])),
                        ('saf_name', (YLeaf(YType.enumeration, 'saf-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamily', '')])),
                        ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                        ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                    ])
                    self.af_name = None
                    self.saf_name = None
                    self.topology_name = None
                    self.create = None

                    self.maximum_prefix = None
                    self._children_name_map["maximum_prefix"] = "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix"

                    self.bgp = Vrfs.Vrf.Afs.Af.Bgp()
                    self.bgp.parent = self
                    self._children_name_map["bgp"] = "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                    self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']" + "[saf-name='" + str(self.saf_name) + "']" + "[topology-name='" + str(self.topology_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.Afs.Af, [u'af_name', u'saf_name', u'topology_name', u'create'], name, value)


                class MaximumPrefix(Entity):
                    """
                    Set maximum prefix limits
                    
                    .. attribute:: prefix_limit
                    
                    	Set table's maximum prefix limit
                    	**type**\: int
                    
                    	**range:** 32..10000000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: mid_threshold
                    
                    	Mid\-threshold (% of maximum)
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2017-07-31'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__init__()

                        self.yang_name = "maximum-prefix"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('prefix_limit', (YLeaf(YType.uint32, 'prefix-limit'), ['int'])),
                            ('mid_threshold', (YLeaf(YType.uint32, 'mid-threshold'), ['int'])),
                        ])
                        self.prefix_limit = None
                        self.mid_threshold = None
                        self._segment_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrfs.Vrf.Afs.Af.MaximumPrefix, ['prefix_limit', 'mid_threshold'], name, value)


                class Bgp(Entity):
                    """
                    BGP AF VRF config
                    
                    .. attribute:: import_route_targets
                    
                    	Import Route targets
                    	**type**\:  :py:class:`ImportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets>`
                    
                    .. attribute:: export_route_targets
                    
                    	Export Route targets
                    	**type**\:  :py:class:`ExportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets>`
                    
                    .. attribute:: vrf_to_global_export_route_policy
                    
                    	Route policy for vrf to global export filtering
                    	**type**\:  :py:class:`VrfToGlobalExportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: export_vrf_options
                    
                    	Export VRF options
                    	**type**\:  :py:class:`ExportVrfOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions>`
                    
                    .. attribute:: global_to_vrf_import_route_policy
                    
                    	Route policy for global to vrf import filtering
                    	**type**\:  :py:class:`GlobalToVrfImportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: export_route_policy
                    
                    	Route policy for export filtering
                    	**type**\: str
                    
                    .. attribute:: import_route_policy
                    
                    	Route policy for import filtering
                    	**type**\: str
                    
                    .. attribute:: import_vrf_options
                    
                    	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(Vrfs.Vrf.Afs.Af.Bgp, self).__init__()

                        self.yang_name = "bgp"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("import-route-targets", ("import_route_targets", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets)), ("export-route-targets", ("export_route_targets", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets)), ("vrf-to-global-export-route-policy", ("vrf_to_global_export_route_policy", Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy)), ("export-vrf-options", ("export_vrf_options", Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions)), ("global-to-vrf-import-route-policy", ("global_to_vrf_import_route_policy", Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy))])
                        self._leafs = OrderedDict([
                            ('export_route_policy', (YLeaf(YType.str, 'export-route-policy'), ['str'])),
                            ('import_route_policy', (YLeaf(YType.str, 'import-route-policy'), ['str'])),
                            ('import_vrf_options', (YLeaf(YType.boolean, 'import-vrf-options'), ['bool'])),
                        ])
                        self.export_route_policy = None
                        self.import_route_policy = None
                        self.import_vrf_options = None

                        self.import_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets()
                        self.import_route_targets.parent = self
                        self._children_name_map["import_route_targets"] = "import-route-targets"

                        self.export_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets()
                        self.export_route_targets.parent = self
                        self._children_name_map["export_route_targets"] = "export-route-targets"

                        self.vrf_to_global_export_route_policy = None
                        self._children_name_map["vrf_to_global_export_route_policy"] = "vrf-to-global-export-route-policy"

                        self.export_vrf_options = Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions()
                        self.export_vrf_options.parent = self
                        self._children_name_map["export_vrf_options"] = "export-vrf-options"

                        self.global_to_vrf_import_route_policy = None
                        self._children_name_map["global_to_vrf_import_route_policy"] = "global-to-vrf-import-route-policy"
                        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp, ['export_route_policy', 'import_route_policy', 'import_vrf_options'], name, value)


                    class ImportRouteTargets(Entity):
                        """
                        Import Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets, self).__init__()

                            self.yang_name = "import-route-targets"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route-targets", ("route_targets", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets))])
                            self._leafs = OrderedDict()

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._segment_path = lambda: "import-route-targets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets, [], name, value)


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2018-01-18'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "import-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("route-target", ("route_target", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget))])
                                self._leafs = OrderedDict()

                                self.route_target = YList(self)
                                self._segment_path = lambda: "route-targets"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, [], name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  (key)
                                
                                	Type of RT
                                	**type**\:  :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of  		 :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_classes = OrderedDict([("as-or-four-byte-as", ("as_or_four_byte_as", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs)), ("ipv4-address", ("ipv4_address", Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTarget', '')])),
                                    ])
                                    self.type = None

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)
                                    self._segment_path = lambda: "route-target" + "[type='" + str(self.type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  (key)
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  (key)
                                    
                                    	AS number Index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  (key)
                                    
                                    	Stitching RT
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2018-01-18'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_','as_index','stitching_rt']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                            ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                                            ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                        ])
                                        self.as_xx = None
                                        self.as_ = None
                                        self.as_index = None
                                        self.stitching_rt = None
                                        self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + str(self.as_xx) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	IP address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  (key)
                                    
                                    	IP address Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  (key)
                                    
                                    	Stitching RT
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2018-01-18'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address','address_index','stitching_rt']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                            ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                        ])
                                        self.address = None
                                        self.address_index = None
                                        self.stitching_rt = None
                                        self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[address-index='" + str(self.address_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                    class ExportRouteTargets(Entity):
                        """
                        Export Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets, self).__init__()

                            self.yang_name = "export-route-targets"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route-targets", ("route_targets", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets))])
                            self._leafs = OrderedDict()

                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                            self.route_targets.parent = self
                            self._children_name_map["route_targets"] = "route-targets"
                            self._segment_path = lambda: "export-route-targets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets, [], name, value)


                        class RouteTargets(Entity):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2018-01-18'

                            def __init__(self):
                                super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__init__()

                                self.yang_name = "route-targets"
                                self.yang_parent_name = "export-route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("route-target", ("route_target", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget))])
                                self._leafs = OrderedDict()

                                self.route_target = YList(self)
                                self._segment_path = lambda: "route-targets"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, [], name, value)


                            class RouteTarget(Entity):
                                """
                                Route target
                                
                                .. attribute:: type  (key)
                                
                                	Type of RT
                                	**type**\:  :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of  		 :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-targets"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_classes = OrderedDict([("as-or-four-byte-as", ("as_or_four_byte_as", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs)), ("ipv4-address", ("ipv4_address", Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTarget', '')])),
                                    ])
                                    self.type = None

                                    self.as_or_four_byte_as = YList(self)
                                    self.ipv4_address = YList(self)
                                    self._segment_path = lambda: "route-target" + "[type='" + str(self.type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                                class AsOrFourByteAs(Entity):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  (key)
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  (key)
                                    
                                    	AS number Index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  (key)
                                    
                                    	Stitching RT
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2018-01-18'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                        self.yang_name = "as-or-four-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_','as_index','stitching_rt']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                            ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                                            ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                        ])
                                        self.as_xx = None
                                        self.as_ = None
                                        self.as_index = None
                                        self.stitching_rt = None
                                        self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + str(self.as_xx) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                                class Ipv4Address(Entity):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  (key)
                                    
                                    	IP address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  (key)
                                    
                                    	IP address Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  (key)
                                    
                                    	Stitching RT
                                    	**type**\: int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2018-01-18'

                                    def __init__(self):
                                        super(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                        self.yang_name = "ipv4-address"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['address','address_index','stitching_rt']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                            ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                        ])
                                        self.address = None
                                        self.address_index = None
                                        self.stitching_rt = None
                                        self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[address-index='" + str(self.address_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                    class VrfToGlobalExportRoutePolicy(Entity):
                        """
                        Route policy for vrf to global export filtering
                        
                        .. attribute:: route_policy_name
                        
                        	Vrf to global export route policy
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to Default VRF.FALSE Disable imported VPN paths to be exported to Default VRF
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__init__()

                            self.yang_name = "vrf-to-global-export-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ('allow_imported_vpn', (YLeaf(YType.boolean, 'allow-imported-vpn'), ['bool'])),
                            ])
                            self.route_policy_name = None
                            self.allow_imported_vpn = None
                            self._segment_path = lambda: "vrf-to-global-export-route-policy"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, ['route_policy_name', 'allow_imported_vpn'], name, value)


                    class ExportVrfOptions(Entity):
                        """
                        Export VRF options
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to non\-default VRFFALSE Disable imported VPN paths to be exported to non\-default VRF
                        	**type**\: bool
                        
                        .. attribute:: import_stitching_rt
                        
                        	TRUE Use stitchng RTs to import extranet pathsFALSE Use regular RTs to import extranet paths
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, self).__init__()

                            self.yang_name = "export-vrf-options"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('allow_imported_vpn', (YLeaf(YType.boolean, 'allow-imported-vpn'), ['bool'])),
                                ('import_stitching_rt', (YLeaf(YType.boolean, 'import-stitching-rt'), ['bool'])),
                            ])
                            self.allow_imported_vpn = None
                            self.import_stitching_rt = None
                            self._segment_path = lambda: "export-vrf-options"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions, ['allow_imported_vpn', 'import_stitching_rt'], name, value)


                    class GlobalToVrfImportRoutePolicy(Entity):
                        """
                        Route policy for global to vrf import filtering
                        
                        .. attribute:: route_policy_name
                        
                        	Global to vrf import route policy
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: advertise_as_vpn
                        
                        	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__init__()

                            self.yang_name = "global-to-vrf-import-route-policy"
                            self.yang_parent_name = "bgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ('advertise_as_vpn', (YLeaf(YType.boolean, 'advertise-as-vpn'), ['bool'])),
                            ])
                            self.route_policy_name = None
                            self.advertise_as_vpn = None
                            self._segment_path = lambda: "global-to-vrf-import-route-policy"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, ['route_policy_name', 'advertise_as_vpn'], name, value)


        class BgpGlobal(Entity):
            """
            BGP related VRF Global config
            
            .. attribute:: route_distinguisher
            
            	Route distinguisher
            	**type**\:  :py:class:`RouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.BgpGlobal.RouteDistinguisher>`
            
            

            """

            _prefix = 'ipv4-bgp-cfg'
            _revision = '2018-01-18'

            def __init__(self):
                super(Vrfs.Vrf.BgpGlobal, self).__init__()

                self.yang_name = "bgp-global"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("route-distinguisher", ("route_distinguisher", Vrfs.Vrf.BgpGlobal.RouteDistinguisher))])
                self._leafs = OrderedDict()

                self.route_distinguisher = Vrfs.Vrf.BgpGlobal.RouteDistinguisher()
                self.route_distinguisher.parent = self
                self._children_name_map["route_distinguisher"] = "route-distinguisher"
                self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp-global"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.BgpGlobal, [], name, value)


            class RouteDistinguisher(Entity):
                """
                Route distinguisher
                
                .. attribute:: type
                
                	Type of RD
                	**type**\:  :py:class:`BgpGlobalRouteDistinguisher <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpGlobalRouteDistinguisher>`
                
                .. attribute:: as_xx
                
                	AS number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: as_
                
                	AS number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: as_index
                
                	ASN Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address
                
                	IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_index
                
                	IP address index
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2018-01-18'

                def __init__(self):
                    super(Vrfs.Vrf.BgpGlobal.RouteDistinguisher, self).__init__()

                    self.yang_name = "route-distinguisher"
                    self.yang_parent_name = "bgp-global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpGlobalRouteDistinguisher', '')])),
                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                        ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                        ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                    ])
                    self.type = None
                    self.as_xx = None
                    self.as_ = None
                    self.as_index = None
                    self.address = None
                    self.address_index = None
                    self._segment_path = lambda: "route-distinguisher"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.BgpGlobal.RouteDistinguisher, ['type', 'as_xx', 'as_', 'as_index', 'address', 'address_index'], name, value)


        class MulticastHost(Entity):
            """
            Multicast host stack configuration
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 configuration
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv6>`
            
            

            """

            _prefix = 'ip-iarm-vrf-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vrfs.Vrf.MulticastHost, self).__init__()

                self.yang_name = "multicast-host"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Vrfs.Vrf.MulticastHost.Ipv4)), ("ipv6", ("ipv6", Vrfs.Vrf.MulticastHost.Ipv6))])
                self._leafs = OrderedDict()

                self.ipv4 = Vrfs.Vrf.MulticastHost.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"

                self.ipv6 = Vrfs.Vrf.MulticastHost.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._segment_path = lambda: "Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vrfs.Vrf.MulticastHost, [], name, value)


            class Ipv4(Entity):
                """
                IPv4 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "multicast-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = None
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.MulticastHost.Ipv4, ['interface'], name, value)


            class Ipv6(Entity):
                """
                IPv6 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vrfs.Vrf.MulticastHost.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "multicast-host"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ])
                    self.interface = None
                    self._segment_path = lambda: "ipv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vrfs.Vrf.MulticastHost.Ipv6, ['interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Vrfs()
        return self._top_entity

class GlobalAf(Entity):
    """
    global af
    
    .. attribute:: afs
    
    	VRF address family configuration
    	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(GlobalAf, self).__init__()
        self._top_entity = None

        self.yang_name = "global-af"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("afs", ("afs", GlobalAf.Afs))])
        self._leafs = OrderedDict()

        self.afs = GlobalAf.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(GlobalAf, [], name, value)


    class Afs(Entity):
        """
        VRF address family configuration
        
        .. attribute:: af
        
        	VRF address family configuration
        	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(GlobalAf.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "global-af"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("af", ("af", GlobalAf.Afs.Af))])
            self._leafs = OrderedDict()

            self.af = YList(self)
            self._segment_path = lambda: "afs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(GlobalAf.Afs, [], name, value)


        class Af(Entity):
            """
            VRF address family configuration
            
            .. attribute:: af_name  (key)
            
            	Address family
            	**type**\:  :py:class:`VrfAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamily>`
            
            .. attribute:: saf_name  (key)
            
            	Sub\-Address family
            	**type**\:  :py:class:`VrfSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamily>`
            
            .. attribute:: topology_name  (key)
            
            	Topology name
            	**type**\: str
            
            	**length:** 1..244
            
            .. attribute:: create
            
            	VRF configuration for a particular address family
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum_prefix
            
            	Set maximum prefix limits
            	**type**\:  :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.MaximumPrefix>`
            
            	**presence node**\: True
            
            .. attribute:: bgp
            
            	BGP AF VRF config
            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(GlobalAf.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af_name','saf_name','topology_name']
                self._child_classes = OrderedDict([("Cisco-IOS-XR-ip-rib-cfg:maximum-prefix", ("maximum_prefix", GlobalAf.Afs.Af.MaximumPrefix)), ("Cisco-IOS-XR-ipv4-bgp-cfg:bgp", ("bgp", GlobalAf.Afs.Af.Bgp))])
                self._leafs = OrderedDict([
                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamily', '')])),
                    ('saf_name', (YLeaf(YType.enumeration, 'saf-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamily', '')])),
                    ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                    ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                ])
                self.af_name = None
                self.saf_name = None
                self.topology_name = None
                self.create = None

                self.maximum_prefix = None
                self._children_name_map["maximum_prefix"] = "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix"

                self.bgp = GlobalAf.Afs.Af.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']" + "[saf-name='" + str(self.saf_name) + "']" + "[topology-name='" + str(self.topology_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:global-af/afs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(GlobalAf.Afs.Af, [u'af_name', u'saf_name', u'topology_name', u'create'], name, value)


            class MaximumPrefix(Entity):
                """
                Set maximum prefix limits
                
                .. attribute:: prefix_limit
                
                	Set table's maximum prefix limit
                	**type**\: int
                
                	**range:** 32..10000000
                
                	**mandatory**\: True
                
                .. attribute:: mid_threshold
                
                	Mid\-threshold (% of maximum)
                	**type**\: int
                
                	**range:** 1..100
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ip-rib-cfg'
                _revision = '2017-07-31'

                def __init__(self):
                    super(GlobalAf.Afs.Af.MaximumPrefix, self).__init__()

                    self.yang_name = "maximum-prefix"
                    self.yang_parent_name = "af"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('prefix_limit', (YLeaf(YType.uint32, 'prefix-limit'), ['int'])),
                        ('mid_threshold', (YLeaf(YType.uint32, 'mid-threshold'), ['int'])),
                    ])
                    self.prefix_limit = None
                    self.mid_threshold = None
                    self._segment_path = lambda: "Cisco-IOS-XR-ip-rib-cfg:maximum-prefix"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalAf.Afs.Af.MaximumPrefix, ['prefix_limit', 'mid_threshold'], name, value)


            class Bgp(Entity):
                """
                BGP AF VRF config
                
                .. attribute:: import_route_targets
                
                	Import Route targets
                	**type**\:  :py:class:`ImportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ImportRouteTargets>`
                
                .. attribute:: export_route_targets
                
                	Export Route targets
                	**type**\:  :py:class:`ExportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportRouteTargets>`
                
                .. attribute:: vrf_to_global_export_route_policy
                
                	Route policy for vrf to global export filtering
                	**type**\:  :py:class:`VrfToGlobalExportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy>`
                
                	**presence node**\: True
                
                .. attribute:: export_vrf_options
                
                	Export VRF options
                	**type**\:  :py:class:`ExportVrfOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportVrfOptions>`
                
                .. attribute:: global_to_vrf_import_route_policy
                
                	Route policy for global to vrf import filtering
                	**type**\:  :py:class:`GlobalToVrfImportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy>`
                
                	**presence node**\: True
                
                .. attribute:: export_route_policy
                
                	Route policy for export filtering
                	**type**\: str
                
                .. attribute:: import_route_policy
                
                	Route policy for import filtering
                	**type**\: str
                
                .. attribute:: import_vrf_options
                
                	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                	**type**\: bool
                
                

                """

                _prefix = 'ipv4-bgp-cfg'
                _revision = '2018-01-18'

                def __init__(self):
                    super(GlobalAf.Afs.Af.Bgp, self).__init__()

                    self.yang_name = "bgp"
                    self.yang_parent_name = "af"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("import-route-targets", ("import_route_targets", GlobalAf.Afs.Af.Bgp.ImportRouteTargets)), ("export-route-targets", ("export_route_targets", GlobalAf.Afs.Af.Bgp.ExportRouteTargets)), ("vrf-to-global-export-route-policy", ("vrf_to_global_export_route_policy", GlobalAf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy)), ("export-vrf-options", ("export_vrf_options", GlobalAf.Afs.Af.Bgp.ExportVrfOptions)), ("global-to-vrf-import-route-policy", ("global_to_vrf_import_route_policy", GlobalAf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy))])
                    self._leafs = OrderedDict([
                        ('export_route_policy', (YLeaf(YType.str, 'export-route-policy'), ['str'])),
                        ('import_route_policy', (YLeaf(YType.str, 'import-route-policy'), ['str'])),
                        ('import_vrf_options', (YLeaf(YType.boolean, 'import-vrf-options'), ['bool'])),
                    ])
                    self.export_route_policy = None
                    self.import_route_policy = None
                    self.import_vrf_options = None

                    self.import_route_targets = GlobalAf.Afs.Af.Bgp.ImportRouteTargets()
                    self.import_route_targets.parent = self
                    self._children_name_map["import_route_targets"] = "import-route-targets"

                    self.export_route_targets = GlobalAf.Afs.Af.Bgp.ExportRouteTargets()
                    self.export_route_targets.parent = self
                    self._children_name_map["export_route_targets"] = "export-route-targets"

                    self.vrf_to_global_export_route_policy = None
                    self._children_name_map["vrf_to_global_export_route_policy"] = "vrf-to-global-export-route-policy"

                    self.export_vrf_options = GlobalAf.Afs.Af.Bgp.ExportVrfOptions()
                    self.export_vrf_options.parent = self
                    self._children_name_map["export_vrf_options"] = "export-vrf-options"

                    self.global_to_vrf_import_route_policy = None
                    self._children_name_map["global_to_vrf_import_route_policy"] = "global-to-vrf-import-route-policy"
                    self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-cfg:bgp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(GlobalAf.Afs.Af.Bgp, ['export_route_policy', 'import_route_policy', 'import_vrf_options'], name, value)


                class ImportRouteTargets(Entity):
                    """
                    Import Route targets
                    
                    .. attribute:: route_targets
                    
                    	Route target table
                    	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(GlobalAf.Afs.Af.Bgp.ImportRouteTargets, self).__init__()

                        self.yang_name = "import-route-targets"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("route-targets", ("route_targets", GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets))])
                        self._leafs = OrderedDict()

                        self.route_targets = GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                        self.route_targets.parent = self
                        self._children_name_map["route_targets"] = "route-targets"
                        self._segment_path = lambda: "import-route-targets"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalAf.Afs.Af.Bgp.ImportRouteTargets, [], name, value)


                    class RouteTargets(Entity):
                        """
                        Route target table
                        
                        .. attribute:: route_target
                        
                        	Route target
                        	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, self).__init__()

                            self.yang_name = "route-targets"
                            self.yang_parent_name = "import-route-targets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route-target", ("route_target", GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget))])
                            self._leafs = OrderedDict()

                            self.route_target = YList(self)
                            self._segment_path = lambda: "route-targets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets, [], name, value)


                        class RouteTarget(Entity):
                            """
                            Route target
                            
                            .. attribute:: type  (key)
                            
                            	Type of RT
                            	**type**\:  :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                            
                            .. attribute:: as_or_four_byte_as
                            
                            	as or four byte as
                            	**type**\: list of  		 :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                            
                            .. attribute:: ipv4_address
                            
                            	ipv4 address
                            	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2018-01-18'

                            def __init__(self):
                                super(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['type']
                                self._child_classes = OrderedDict([("as-or-four-byte-as", ("as_or_four_byte_as", GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs)), ("ipv4-address", ("ipv4_address", GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTarget', '')])),
                                ])
                                self.type = None

                                self.as_or_four_byte_as = YList(self)
                                self.ipv4_address = YList(self)
                                self._segment_path = lambda: "route-target" + "[type='" + str(self.type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                            class AsOrFourByteAs(Entity):
                                """
                                as or four byte as
                                
                                .. attribute:: as_xx  (key)
                                
                                	AS number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: as_  (key)
                                
                                	AS number
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index  (key)
                                
                                	AS number Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: stitching_rt  (key)
                                
                                	Stitching RT
                                	**type**\: int
                                
                                	**range:** 0..1
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                    self.yang_name = "as-or-four-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','as_','as_index','stitching_rt']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                        ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                                        ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                    ])
                                    self.as_xx = None
                                    self.as_ = None
                                    self.as_index = None
                                    self.stitching_rt = None
                                    self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + str(self.as_xx) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                            class Ipv4Address(Entity):
                                """
                                ipv4 address
                                
                                .. attribute:: address  (key)
                                
                                	IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: address_index  (key)
                                
                                	IP address Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: stitching_rt  (key)
                                
                                	Stitching RT
                                	**type**\: int
                                
                                	**range:** 0..1
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                    self.yang_name = "ipv4-address"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address','address_index','stitching_rt']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                        ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                    ])
                                    self.address = None
                                    self.address_index = None
                                    self.stitching_rt = None
                                    self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[address-index='" + str(self.address_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalAf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                class ExportRouteTargets(Entity):
                    """
                    Export Route targets
                    
                    .. attribute:: route_targets
                    
                    	Route target table
                    	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(GlobalAf.Afs.Af.Bgp.ExportRouteTargets, self).__init__()

                        self.yang_name = "export-route-targets"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("route-targets", ("route_targets", GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets))])
                        self._leafs = OrderedDict()

                        self.route_targets = GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                        self.route_targets.parent = self
                        self._children_name_map["route_targets"] = "route-targets"
                        self._segment_path = lambda: "export-route-targets"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportRouteTargets, [], name, value)


                    class RouteTargets(Entity):
                        """
                        Route target table
                        
                        .. attribute:: route_target
                        
                        	Route target
                        	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2018-01-18'

                        def __init__(self):
                            super(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, self).__init__()

                            self.yang_name = "route-targets"
                            self.yang_parent_name = "export-route-targets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route-target", ("route_target", GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget))])
                            self._leafs = OrderedDict()

                            self.route_target = YList(self)
                            self._segment_path = lambda: "route-targets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets, [], name, value)


                        class RouteTarget(Entity):
                            """
                            Route target
                            
                            .. attribute:: type  (key)
                            
                            	Type of RT
                            	**type**\:  :py:class:`BgpVrfRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTarget>`
                            
                            .. attribute:: as_or_four_byte_as
                            
                            	as or four byte as
                            	**type**\: list of  		 :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                            
                            .. attribute:: ipv4_address
                            
                            	ipv4 address
                            	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2018-01-18'

                            def __init__(self):
                                super(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['type']
                                self._child_classes = OrderedDict([("as-or-four-byte-as", ("as_or_four_byte_as", GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs)), ("ipv4-address", ("ipv4_address", GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTarget', '')])),
                                ])
                                self.type = None

                                self.as_or_four_byte_as = YList(self)
                                self.ipv4_address = YList(self)
                                self._segment_path = lambda: "route-target" + "[type='" + str(self.type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget, ['type'], name, value)


                            class AsOrFourByteAs(Entity):
                                """
                                as or four byte as
                                
                                .. attribute:: as_xx  (key)
                                
                                	AS number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: as_  (key)
                                
                                	AS number
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: as_index  (key)
                                
                                	AS number Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: stitching_rt  (key)
                                
                                	Stitching RT
                                	**type**\: int
                                
                                	**range:** 0..1
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, self).__init__()

                                    self.yang_name = "as-or-four-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','as_','as_index','stitching_rt']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                        ('as_index', (YLeaf(YType.uint32, 'as-index'), ['int'])),
                                        ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                    ])
                                    self.as_xx = None
                                    self.as_ = None
                                    self.as_index = None
                                    self.stitching_rt = None
                                    self._segment_path = lambda: "as-or-four-byte-as" + "[as-xx='" + str(self.as_xx) + "']" + "[as='" + str(self.as_) + "']" + "[as-index='" + str(self.as_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs, ['as_xx', 'as_', 'as_index', 'stitching_rt'], name, value)


                            class Ipv4Address(Entity):
                                """
                                ipv4 address
                                
                                .. attribute:: address  (key)
                                
                                	IP address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: address_index  (key)
                                
                                	IP address Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: stitching_rt  (key)
                                
                                	Stitching RT
                                	**type**\: int
                                
                                	**range:** 0..1
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2018-01-18'

                                def __init__(self):
                                    super(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, self).__init__()

                                    self.yang_name = "ipv4-address"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address','address_index','stitching_rt']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                        ('stitching_rt', (YLeaf(YType.uint32, 'stitching-rt'), ['int'])),
                                    ])
                                    self.address = None
                                    self.address_index = None
                                    self.stitching_rt = None
                                    self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']" + "[address-index='" + str(self.address_index) + "']" + "[stitching-rt='" + str(self.stitching_rt) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address, ['address', 'address_index', 'stitching_rt'], name, value)


                class VrfToGlobalExportRoutePolicy(Entity):
                    """
                    Route policy for vrf to global export filtering
                    
                    .. attribute:: route_policy_name
                    
                    	Vrf to global export route policy
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: allow_imported_vpn
                    
                    	TRUE Enable imported VPN paths to be exported to Default VRF.FALSE Disable imported VPN paths to be exported to Default VRF
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(GlobalAf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, self).__init__()

                        self.yang_name = "vrf-to-global-export-route-policy"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('allow_imported_vpn', (YLeaf(YType.boolean, 'allow-imported-vpn'), ['bool'])),
                        ])
                        self.route_policy_name = None
                        self.allow_imported_vpn = None
                        self._segment_path = lambda: "vrf-to-global-export-route-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalAf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy, ['route_policy_name', 'allow_imported_vpn'], name, value)


                class ExportVrfOptions(Entity):
                    """
                    Export VRF options
                    
                    .. attribute:: allow_imported_vpn
                    
                    	TRUE Enable imported VPN paths to be exported to non\-default VRFFALSE Disable imported VPN paths to be exported to non\-default VRF
                    	**type**\: bool
                    
                    .. attribute:: import_stitching_rt
                    
                    	TRUE Use stitchng RTs to import extranet pathsFALSE Use regular RTs to import extranet paths
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(GlobalAf.Afs.Af.Bgp.ExportVrfOptions, self).__init__()

                        self.yang_name = "export-vrf-options"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_imported_vpn', (YLeaf(YType.boolean, 'allow-imported-vpn'), ['bool'])),
                            ('import_stitching_rt', (YLeaf(YType.boolean, 'import-stitching-rt'), ['bool'])),
                        ])
                        self.allow_imported_vpn = None
                        self.import_stitching_rt = None
                        self._segment_path = lambda: "export-vrf-options"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalAf.Afs.Af.Bgp.ExportVrfOptions, ['allow_imported_vpn', 'import_stitching_rt'], name, value)


                class GlobalToVrfImportRoutePolicy(Entity):
                    """
                    Route policy for global to vrf import filtering
                    
                    .. attribute:: route_policy_name
                    
                    	Global to vrf import route policy
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: advertise_as_vpn
                    
                    	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2018-01-18'

                    def __init__(self):
                        super(GlobalAf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, self).__init__()

                        self.yang_name = "global-to-vrf-import-route-policy"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                            ('advertise_as_vpn', (YLeaf(YType.boolean, 'advertise-as-vpn'), ['bool'])),
                        ])
                        self.route_policy_name = None
                        self.advertise_as_vpn = None
                        self._segment_path = lambda: "global-to-vrf-import-route-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(GlobalAf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy, ['route_policy_name', 'advertise_as_vpn'], name, value)

    def clone_ptr(self):
        self._top_entity = GlobalAf()
        return self._top_entity

class Srlg(Entity):
    """
    srlg
    
    .. attribute:: interfaces
    
    	Set of interfaces configured with SRLG
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces>`
    
    .. attribute:: srlg_names
    
    	Set of SRLG name configuration
    	**type**\:  :py:class:`SrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames>`
    
    .. attribute:: groups
    
    	Set of groups configured with SRLG
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups>`
    
    .. attribute:: inherit_nodes
    
    	Set of inherit nodes configured with SRLG
    	**type**\:  :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes>`
    
    .. attribute:: enable
    
    	Enable SRLG
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", Srlg.Interfaces)), ("srlg-names", ("srlg_names", Srlg.SrlgNames)), ("groups", ("groups", Srlg.Groups)), ("inherit-nodes", ("inherit_nodes", Srlg.InheritNodes))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.interfaces = Srlg.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.srlg_names = Srlg.SrlgNames()
        self.srlg_names.parent = self
        self._children_name_map["srlg_names"] = "srlg-names"

        self.groups = Srlg.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.inherit_nodes = Srlg.InheritNodes()
        self.inherit_nodes.parent = self
        self._children_name_map["inherit_nodes"] = "inherit-nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Srlg, [u'enable'], name, value)


    class Interfaces(Entity):
        """
        Set of interfaces configured with SRLG
        
        .. attribute:: interface
        
        	Interface configurations
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Srlg.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Interface configurations
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: include_optical
            
            	Include optical configuration for an interface
            	**type**\:  :py:class:`IncludeOptical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.IncludeOptical>`
            
            .. attribute:: interface_group
            
            	Group configuration for an interface
            	**type**\:  :py:class:`InterfaceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup>`
            
            .. attribute:: values
            
            	SRLG Value configuration for an interface
            	**type**\:  :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values>`
            
            .. attribute:: interface_srlg_names
            
            	SRLG Name configuration for an interface
            	**type**\:  :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames>`
            
            .. attribute:: enable
            
            	Enable SRLG interface
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("include-optical", ("include_optical", Srlg.Interfaces.Interface.IncludeOptical)), ("interface-group", ("interface_group", Srlg.Interfaces.Interface.InterfaceGroup)), ("values", ("values", Srlg.Interfaces.Interface.Values)), ("interface-srlg-names", ("interface_srlg_names", Srlg.Interfaces.Interface.InterfaceSrlgNames))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.interface_name = None
                self.enable = None

                self.include_optical = Srlg.Interfaces.Interface.IncludeOptical()
                self.include_optical.parent = self
                self._children_name_map["include_optical"] = "include-optical"

                self.interface_group = Srlg.Interfaces.Interface.InterfaceGroup()
                self.interface_group.parent = self
                self._children_name_map["interface_group"] = "interface-group"

                self.values = Srlg.Interfaces.Interface.Values()
                self.values.parent = self
                self._children_name_map["values"] = "values"

                self.interface_srlg_names = Srlg.Interfaces.Interface.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Interfaces.Interface, [u'interface_name', u'enable'], name, value)


            class IncludeOptical(Entity):
                """
                Include optical configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface include optical
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: priority
                
                	Priority for optical domain values
                	**type**\:  :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                
                	**default value**\: default
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.IncludeOptical, self).__init__()

                    self.yang_name = "include-optical"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriority', '')])),
                    ])
                    self.enable = None
                    self.priority = None
                    self._segment_path = lambda: "include-optical"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.IncludeOptical, [u'enable', u'priority'], name, value)


            class InterfaceGroup(Entity):
                """
                Group configuration for an interface
                
                .. attribute:: group_names
                
                	Set of group name under an interface
                	**type**\:  :py:class:`GroupNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames>`
                
                .. attribute:: enable
                
                	Enable SRLG interface group submode
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceGroup, self).__init__()

                    self.yang_name = "interface-group"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group-names", ("group_names", Srlg.Interfaces.Interface.InterfaceGroup.GroupNames))])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.group_names = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames()
                    self.group_names.parent = self
                    self._children_name_map["group_names"] = "group-names"
                    self._segment_path = lambda: "interface-group"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup, [u'enable'], name, value)


                class GroupNames(Entity):
                    """
                    Set of group name under an interface
                    
                    .. attribute:: group_name
                    
                    	Group name included under interface
                    	**type**\: list of  		 :py:class:`GroupName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName>`
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, self).__init__()

                        self.yang_name = "group-names"
                        self.yang_parent_name = "interface-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("group-name", ("group_name", Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName))])
                        self._leafs = OrderedDict()

                        self.group_name = YList(self)
                        self._segment_path = lambda: "group-names"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames, [], name, value)


                    class GroupName(Entity):
                        """
                        Group name included under interface
                        
                        .. attribute:: group_name_index  (key)
                        
                        	Group name index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: group_name
                        
                        	Group name
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: srlg_priority
                        
                        	SRLG priority
                        	**type**\:  :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                        
                        	**default value**\: default
                        
                        

                        """

                        _prefix = 'infra-rsi-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, self).__init__()

                            self.yang_name = "group-name"
                            self.yang_parent_name = "group-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_name_index']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_name_index', (YLeaf(YType.uint32, 'group-name-index'), ['int'])),
                                ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                                ('srlg_priority', (YLeaf(YType.enumeration, 'srlg-priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriority', '')])),
                            ])
                            self.group_name_index = None
                            self.group_name = None
                            self.srlg_priority = None
                            self._segment_path = lambda: "group-name" + "[group-name-index='" + str(self.group_name_index) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName, [u'group_name_index', u'group_name', u'srlg_priority'], name, value)


            class Values(Entity):
                """
                SRLG Value configuration for an interface
                
                .. attribute:: value
                
                	SRLG value data
                	**type**\: list of  		 :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values.Value>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.Values, self).__init__()

                    self.yang_name = "values"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("value", ("value", Srlg.Interfaces.Interface.Values.Value))])
                    self._leafs = OrderedDict()

                    self.value = YList(self)
                    self._segment_path = lambda: "values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.Values, [], name, value)


                class Value(Entity):
                    """
                    SRLG value data
                    
                    .. attribute:: srlg_index  (key)
                    
                    	SRLG index
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:  :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.Values.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('srlg_index', (YLeaf(YType.uint32, 'srlg-index'), ['int'])),
                            ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                            ('srlg_priority', (YLeaf(YType.enumeration, 'srlg-priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriority', '')])),
                        ])
                        self.srlg_index = None
                        self.srlg_value = None
                        self.srlg_priority = None
                        self._segment_path = lambda: "value" + "[srlg-index='" + str(self.srlg_index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.Values.Value, [u'srlg_index', u'srlg_value', u'srlg_priority'], name, value)


            class InterfaceSrlgNames(Entity):
                """
                SRLG Name configuration for an interface
                
                .. attribute:: interface_srlg_name
                
                	SRLG name data
                	**type**\: list of  		 :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Interfaces.Interface.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-srlg-name", ("interface_srlg_name", Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName))])
                    self._leafs = OrderedDict()

                    self.interface_srlg_name = YList(self)
                    self._segment_path = lambda: "interface-srlg-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Interfaces.Interface.InterfaceSrlgNames, [], name, value)


                class InterfaceSrlgName(Entity):
                    """
                    SRLG name data
                    
                    .. attribute:: srlg_name  (key)
                    
                    	SRLG name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                        ])
                        self.srlg_name = None
                        self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + str(self.srlg_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName, [u'srlg_name'], name, value)


    class SrlgNames(Entity):
        """
        Set of SRLG name configuration
        
        .. attribute:: srlg_name
        
        	SRLG name configuration
        	**type**\: list of  		 :py:class:`SrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames.SrlgName>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.SrlgNames, self).__init__()

            self.yang_name = "srlg-names"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("srlg-name", ("srlg_name", Srlg.SrlgNames.SrlgName))])
            self._leafs = OrderedDict()

            self.srlg_name = YList(self)
            self._segment_path = lambda: "srlg-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.SrlgNames, [], name, value)


        class SrlgName(Entity):
            """
            SRLG name configuration
            
            .. attribute:: srlg_name  (key)
            
            	SRLG name
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.SrlgNames.SrlgName, self).__init__()

                self.yang_name = "srlg-name"
                self.yang_parent_name = "srlg-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['srlg_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                    ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                ])
                self.srlg_name = None
                self.srlg_value = None
                self._segment_path = lambda: "srlg-name" + "[srlg-name='" + str(self.srlg_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/srlg-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.SrlgNames.SrlgName, [u'srlg_name', u'srlg_value'], name, value)


    class Groups(Entity):
        """
        Set of groups configured with SRLG
        
        .. attribute:: group
        
        	Group configurations
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", Srlg.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Groups, [], name, value)


        class Group(Entity):
            """
            Group configurations
            
            .. attribute:: group_name  (key)
            
            	Group name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: group_values
            
            	Set of SRLG values configured under a group
            	**type**\:  :py:class:`GroupValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues>`
            
            .. attribute:: enable
            
            	Enable SRLG group
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_name']
                self._child_classes = OrderedDict([("group-values", ("group_values", Srlg.Groups.Group.GroupValues))])
                self._leafs = OrderedDict([
                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.group_name = None
                self.enable = None

                self.group_values = Srlg.Groups.Group.GroupValues()
                self.group_values.parent = self
                self._children_name_map["group_values"] = "group-values"
                self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Groups.Group, [u'group_name', u'enable'], name, value)


            class GroupValues(Entity):
                """
                Set of SRLG values configured under a group
                
                .. attribute:: group_value
                
                	Group SRLG values with attribute
                	**type**\: list of  		 :py:class:`GroupValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues.GroupValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.Groups.Group.GroupValues, self).__init__()

                    self.yang_name = "group-values"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group-value", ("group_value", Srlg.Groups.Group.GroupValues.GroupValue))])
                    self._leafs = OrderedDict()

                    self.group_value = YList(self)
                    self._segment_path = lambda: "group-values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Groups.Group.GroupValues, [], name, value)


                class GroupValue(Entity):
                    """
                    Group SRLG values with attribute
                    
                    .. attribute:: srlg_index  (key)
                    
                    	SRLG index
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:  :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.Groups.Group.GroupValues.GroupValue, self).__init__()

                        self.yang_name = "group-value"
                        self.yang_parent_name = "group-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('srlg_index', (YLeaf(YType.uint32, 'srlg-index'), ['int'])),
                            ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                            ('srlg_priority', (YLeaf(YType.enumeration, 'srlg-priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriority', '')])),
                        ])
                        self.srlg_index = None
                        self.srlg_value = None
                        self.srlg_priority = None
                        self._segment_path = lambda: "group-value" + "[srlg-index='" + str(self.srlg_index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Groups.Group.GroupValues.GroupValue, [u'srlg_index', u'srlg_value', u'srlg_priority'], name, value)


    class InheritNodes(Entity):
        """
        Set of inherit nodes configured with SRLG
        
        .. attribute:: inherit_node
        
        	Inherit node configurations
        	**type**\: list of  		 :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Srlg.InheritNodes, self).__init__()

            self.yang_name = "inherit-nodes"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("inherit-node", ("inherit_node", Srlg.InheritNodes.InheritNode))])
            self._leafs = OrderedDict()

            self.inherit_node = YList(self)
            self._segment_path = lambda: "inherit-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InheritNodes, [], name, value)


        class InheritNode(Entity):
            """
            Inherit node configurations
            
            .. attribute:: inherit_node_name  (key)
            
            	The inherit node name
            	**type**\: str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: inherit_node_values
            
            	Set of SRLG values configured under an inherit node
            	**type**\:  :py:class:`InheritNodeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues>`
            
            .. attribute:: enable
            
            	Enable SRLG inherit node
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Srlg.InheritNodes.InheritNode, self).__init__()

                self.yang_name = "inherit-node"
                self.yang_parent_name = "inherit-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['inherit_node_name']
                self._child_classes = OrderedDict([("inherit-node-values", ("inherit_node_values", Srlg.InheritNodes.InheritNode.InheritNodeValues))])
                self._leafs = OrderedDict([
                    ('inherit_node_name', (YLeaf(YType.str, 'inherit-node-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.inherit_node_name = None
                self.enable = None

                self.inherit_node_values = Srlg.InheritNodes.InheritNode.InheritNodeValues()
                self.inherit_node_values.parent = self
                self._children_name_map["inherit_node_values"] = "inherit-node-values"
                self._segment_path = lambda: "inherit-node" + "[inherit-node-name='" + str(self.inherit_node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:srlg/inherit-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InheritNodes.InheritNode, [u'inherit_node_name', u'enable'], name, value)


            class InheritNodeValues(Entity):
                """
                Set of SRLG values configured under an inherit
                node
                
                .. attribute:: inherit_node_value
                
                	Inherit node SRLG value with attributes
                	**type**\: list of  		 :py:class:`InheritNodeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Srlg.InheritNodes.InheritNode.InheritNodeValues, self).__init__()

                    self.yang_name = "inherit-node-values"
                    self.yang_parent_name = "inherit-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inherit-node-value", ("inherit_node_value", Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue))])
                    self._leafs = OrderedDict()

                    self.inherit_node_value = YList(self)
                    self._segment_path = lambda: "inherit-node-values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InheritNodes.InheritNode.InheritNodeValues, [], name, value)


                class InheritNodeValue(Entity):
                    """
                    Inherit node SRLG value with attributes
                    
                    .. attribute:: srlg_index  (key)
                    
                    	SRLG index
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:  :py:class:`SrlgPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriority>`
                    
                    	**default value**\: default
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, self).__init__()

                        self.yang_name = "inherit-node-value"
                        self.yang_parent_name = "inherit-node-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('srlg_index', (YLeaf(YType.uint32, 'srlg-index'), ['int'])),
                            ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                            ('srlg_priority', (YLeaf(YType.enumeration, 'srlg-priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriority', '')])),
                        ])
                        self.srlg_index = None
                        self.srlg_value = None
                        self.srlg_priority = None
                        self._segment_path = lambda: "inherit-node-value" + "[srlg-index='" + str(self.srlg_index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue, [u'srlg_index', u'srlg_value', u'srlg_priority'], name, value)

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

class VrfGroups(Entity):
    """
    vrf groups
    
    .. attribute:: vrf_group
    
    	VRF group configuration
    	**type**\: list of  		 :py:class:`VrfGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(VrfGroups, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-groups"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf-group", ("vrf_group", VrfGroups.VrfGroup))])
        self._leafs = OrderedDict()

        self.vrf_group = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VrfGroups, [], name, value)


    class VrfGroup(Entity):
        """
        VRF group configuration
        
        .. attribute:: vrf_group_name  (key)
        
        	VRF group name
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: vrfs
        
        	Set of VRFs configured under a VRF group
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs>`
        
        .. attribute:: enable
        
        	Enable VRF group
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(VrfGroups.VrfGroup, self).__init__()

            self.yang_name = "vrf-group"
            self.yang_parent_name = "vrf-groups"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf_group_name']
            self._child_classes = OrderedDict([("vrfs", ("vrfs", VrfGroups.VrfGroup.Vrfs))])
            self._leafs = OrderedDict([
                ('vrf_group_name', (YLeaf(YType.str, 'vrf-group-name'), ['str'])),
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.vrf_group_name = None
            self.enable = None

            self.vrfs = VrfGroups.VrfGroup.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._segment_path = lambda: "vrf-group" + "[vrf-group-name='" + str(self.vrf_group_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:vrf-groups/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VrfGroups.VrfGroup, [u'vrf_group_name', u'enable'], name, value)


        class Vrfs(Entity):
            """
            Set of VRFs configured under a VRF group
            
            .. attribute:: vrf
            
            	VRF configuration
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(VrfGroups.VrfGroup.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "vrf-group"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", VrfGroups.VrfGroup.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VrfGroups.VrfGroup.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                VRF configuration
                
                .. attribute:: vrf_name  (key)
                
                	VRF name
                	**type**\: str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(VrfGroups.VrfGroup.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.vrf_name = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VrfGroups.VrfGroup.Vrfs.Vrf, [u'vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = VrfGroups()
        return self._top_entity

class SelectiveVrfDownload(Entity):
    """
    selective vrf download
    
    .. attribute:: disable
    
    	Disable selective VRF download
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
        ])
        self.disable = None
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SelectiveVrfDownload, [u'disable'], name, value)

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

