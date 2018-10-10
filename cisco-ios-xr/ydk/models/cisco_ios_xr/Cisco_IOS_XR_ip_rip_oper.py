""" Cisco_IOS_XR_ip_rip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package operational data.

This module contains definitions
for the following management objects\:
  rip\: RIP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InterfaceState(Enum):
    """
    InterfaceState (Enum Class)

    Interface state

    .. data:: interface_none = 0

    	Interface does not exist

    .. data:: interface_down = 1

    	Interface exists but IP is down

    .. data:: interface_up = 2

    	Interface exists and IP is up

    .. data:: interface_unknown = 3

    	Unknown state

    """

    interface_none = Enum.YLeaf(0, "interface-none")

    interface_down = Enum.YLeaf(1, "interface-down")

    interface_up = Enum.YLeaf(2, "interface-up")

    interface_unknown = Enum.YLeaf(3, "interface-unknown")


class RipRouteOrigin(Enum):
    """
    RipRouteOrigin (Enum Class)

    Rip route origin

    .. data:: rip_rt_org_runover = 0

    	configured 'network'

    .. data:: rip_rt_org_redist = 1

    	redistributed

    .. data:: rip_rt_org_auto_summary = 2

    	auto summary

    .. data:: rip_rt_org_rip = 3

    	learned via RIP

    .. data:: rip_rt_org_intsummary = 4

    	interface summary-address

    .. data:: rip_rt_org_unused = 5

    	route stay in for triggered rip

    """

    rip_rt_org_runover = Enum.YLeaf(0, "rip-rt-org-runover")

    rip_rt_org_redist = Enum.YLeaf(1, "rip-rt-org-redist")

    rip_rt_org_auto_summary = Enum.YLeaf(2, "rip-rt-org-auto-summary")

    rip_rt_org_rip = Enum.YLeaf(3, "rip-rt-org-rip")

    rip_rt_org_intsummary = Enum.YLeaf(4, "rip-rt-org-intsummary")

    rip_rt_org_unused = Enum.YLeaf(5, "rip-rt-org-unused")



class Rip(Entity):
    """
    RIP operational data
    
    .. attribute:: vrfs
    
    	VRF related operational data
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs>`
    
    .. attribute:: protocol
    
    	Protocol operational data
    	**type**\:  :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol>`
    
    .. attribute:: default_vrf
    
    	RIP operational data for Default VRF
    	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf>`
    
    

    """

    _prefix = 'ip-rip-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rip, self).__init__()
        self._top_entity = None

        self.yang_name = "rip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rip-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Rip.Vrfs)), ("protocol", ("protocol", Rip.Protocol)), ("default-vrf", ("default_vrf", Rip.DefaultVrf))])
        self._leafs = OrderedDict()

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.protocol = Rip.Protocol()
        self.protocol.parent = self
        self._children_name_map["protocol"] = "protocol"

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Rip, [], name, value)


    class Vrfs(Entity):
        """
        VRF related operational data
        
        .. attribute:: vrf
        
        	Operational data for a particular VRF
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Rip.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Operational data for a particular VRF
            
            .. attribute:: vrf_name  (key)
            
            	Name of the VRF
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes>`
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Configuration>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Statistics>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("routes", ("routes", Rip.Vrfs.Vrf.Routes)), ("configuration", ("configuration", Rip.Vrfs.Vrf.Configuration)), ("statistics", ("statistics", Rip.Vrfs.Vrf.Statistics)), ("interfaces", ("interfaces", Rip.Vrfs.Vrf.Interfaces)), ("global", ("global_", Rip.Vrfs.Vrf.Global))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.routes = Rip.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"

                self.configuration = Rip.Vrfs.Vrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"

                self.statistics = Rip.Vrfs.Vrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.global_ = Rip.Vrfs.Vrf.Global()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.Vrfs.Vrf, ['vrf_name'], name, value)


            class Routes(Entity):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("route", ("route", Rip.Vrfs.Vrf.Routes.Route))])
                    self._leafs = OrderedDict()

                    self.route = YList(self)
                    self._segment_path = lambda: "routes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Routes, [], name, value)


                class Route(Entity):
                    """
                    A route in the RIP database
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\: bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\: bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:  :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\: bool
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Routes.Route.Paths>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("paths", ("paths", Rip.Vrfs.Vrf.Routes.Route.Paths))])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length_xr', (YLeaf(YType.uint32, 'prefix-length-xr'), ['int'])),
                            ('distance', (YLeaf(YType.uint16, 'distance'), ['int'])),
                            ('bgp_count', (YLeaf(YType.uint16, 'bgp-count'), ['int'])),
                            ('route_type', (YLeaf(YType.uint16, 'route-type'), ['int'])),
                            ('route_summary', (YLeaf(YType.boolean, 'route-summary'), ['bool'])),
                            ('route_tag', (YLeaf(YType.uint16, 'route-tag'), ['int'])),
                            ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                            ('attributes', (YLeaf(YType.uint32, 'attributes'), ['int'])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('path_origin', (YLeaf(YType.enumeration, 'path-origin'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOrigin', '')])),
                            ('hold_down', (YLeaf(YType.boolean, 'hold-down'), ['bool'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.destination_address = None
                        self.prefix_length_xr = None
                        self.distance = None
                        self.bgp_count = None
                        self.route_type = None
                        self.route_summary = None
                        self.route_tag = None
                        self.version = None
                        self.attributes = None
                        self.active = None
                        self.path_origin = None
                        self.hold_down = None

                        self.paths = YList(self)
                        self._segment_path = lambda: "route"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Routes.Route, ['prefix', 'prefix_length', 'destination_address', 'prefix_length_xr', 'distance', 'bgp_count', 'route_type', 'route_summary', 'route_tag', 'version', 'attributes', 'active', 'path_origin', 'hold_down'], name, value)


                    class Paths(Entity):
                        """
                        The paths for this route
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Routes.Route.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('uptime', (YLeaf(YType.uint32, 'uptime'), ['int'])),
                                ('is_permanent', (YLeaf(YType.boolean, 'is-permanent'), ['bool'])),
                            ])
                            self.source_address = None
                            self.next_hop_address = None
                            self.metric = None
                            self.tag = None
                            self.interface = None
                            self.uptime = None
                            self.is_permanent = None
                            self._segment_path = lambda: "paths"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Routes.Route.Paths, ['source_address', 'next_hop_address', 'metric', 'tag', 'interface', 'uptime', 'is_permanent'], name, value)


            class Configuration(Entity):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\: bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\: bool
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\: bool
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\: bool
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\: bool
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\: bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\: bool
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('vr_fised_socket', (YLeaf(YType.boolean, 'vr-fised-socket'), ['bool'])),
                        ('rip_version', (YLeaf(YType.int32, 'rip-version'), ['int'])),
                        ('default_metric', (YLeaf(YType.uint8, 'default-metric'), ['int'])),
                        ('maximum_paths', (YLeaf(YType.uint8, 'maximum-paths'), ['int'])),
                        ('auto_summarize', (YLeaf(YType.boolean, 'auto-summarize'), ['bool'])),
                        ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                        ('flash_threshold', (YLeaf(YType.uint8, 'flash-threshold'), ['int'])),
                        ('input_q_length', (YLeaf(YType.uint16, 'input-q-length'), ['int'])),
                        ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                        ('validation_indicator', (YLeaf(YType.boolean, 'validation-indicator'), ['bool'])),
                        ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                        ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                        ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                        ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                        ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('nsf_status', (YLeaf(YType.boolean, 'nsf-status'), ['bool'])),
                        ('nsf_life_time', (YLeaf(YType.uint32, 'nsf-life-time'), ['int'])),
                    ])
                    self.active = None
                    self.vr_fised_socket = None
                    self.rip_version = None
                    self.default_metric = None
                    self.maximum_paths = None
                    self.auto_summarize = None
                    self.multicast_address = None
                    self.flash_threshold = None
                    self.input_q_length = None
                    self.triggered_rip = None
                    self.validation_indicator = None
                    self.update_timer = None
                    self.next_update_time = None
                    self.invalid_timer = None
                    self.hold_down_timer = None
                    self.flush_timer = None
                    self.oom_flags = None
                    self.nsf_status = None
                    self.nsf_life_time = None
                    self._segment_path = lambda: "configuration"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Configuration, ['active', 'vr_fised_socket', 'rip_version', 'default_metric', 'maximum_paths', 'auto_summarize', 'multicast_address', 'flash_threshold', 'input_q_length', 'triggered_rip', 'validation_indicator', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'oom_flags', 'nsf_status', 'nsf_life_time'], name, value)


            class Statistics(Entity):
                """
                RIP statistics information
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                        ('discarded_packets', (YLeaf(YType.uint32, 'discarded-packets'), ['int'])),
                        ('discarded_routes', (YLeaf(YType.uint32, 'discarded-routes'), ['int'])),
                        ('standby_packets_received', (YLeaf(YType.uint32, 'standby-packets-received'), ['int'])),
                        ('sent_messages', (YLeaf(YType.uint32, 'sent-messages'), ['int'])),
                        ('sent_message_failures', (YLeaf(YType.uint32, 'sent-message-failures'), ['int'])),
                        ('query_responses', (YLeaf(YType.uint32, 'query-responses'), ['int'])),
                        ('periodic_updates', (YLeaf(YType.uint32, 'periodic-updates'), ['int'])),
                        ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                        ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                        ('route_malloc_failures', (YLeaf(YType.uint32, 'route-malloc-failures'), ['int'])),
                        ('path_malloc_failures', (YLeaf(YType.uint32, 'path-malloc-failures'), ['int'])),
                        ('rib_updates', (YLeaf(YType.uint32, 'rib-updates'), ['int'])),
                    ])
                    self.received_packets = None
                    self.discarded_packets = None
                    self.discarded_routes = None
                    self.standby_packets_received = None
                    self.sent_messages = None
                    self.sent_message_failures = None
                    self.query_responses = None
                    self.periodic_updates = None
                    self.route_count = None
                    self.path_count = None
                    self.route_malloc_failures = None
                    self.path_malloc_failures = None
                    self.rib_updates = None
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Statistics, ['received_packets', 'discarded_packets', 'discarded_routes', 'standby_packets_received', 'sent_messages', 'sent_message_failures', 'query_responses', 'periodic_updates', 'route_count', 'path_count', 'route_malloc_failures', 'path_malloc_failures', 'rib_updates'], name, value)


            class Interfaces(Entity):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Rip.Vrfs.Vrf.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\: bool
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\: bool
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\: bool
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\: bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\: bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\: bool
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\: str
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\: bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\: bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of  		 :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of  		 :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("rip-summary", ("rip_summary", Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary)), ("rip-peer", ("rip_peer", Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                            ('rip_enabled', (YLeaf(YType.boolean, 'rip-enabled'), ['bool'])),
                            ('is_passive_interface', (YLeaf(YType.boolean, 'is-passive-interface'), ['bool'])),
                            ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                            ('accept_metric', (YLeaf(YType.boolean, 'accept-metric'), ['bool'])),
                            ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                            ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('metric_cost', (YLeaf(YType.uint32, 'metric-cost'), ['int'])),
                            ('split_horizon', (YLeaf(YType.boolean, 'split-horizon'), ['bool'])),
                            ('poison_horizon', (YLeaf(YType.boolean, 'poison-horizon'), ['bool'])),
                            ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('join_status', (YLeaf(YType.boolean, 'join-status'), ['bool'])),
                            ('lpts_state', (YLeaf(YType.boolean, 'lpts-state'), ['bool'])),
                            ('auth_mode', (YLeaf(YType.uint32, 'auth-mode'), ['int'])),
                            ('auth_keychain', (YLeaf(YType.str, 'auth-keychain'), ['str'])),
                            ('send_auth_key_exists', (YLeaf(YType.boolean, 'send-auth-key-exists'), ['bool'])),
                            ('auth_key_md5', (YLeaf(YType.boolean, 'auth-key-md5'), ['bool'])),
                            ('auth_key_send_id', (YLeaf(YType.uint64, 'auth-key-send-id'), ['int'])),
                            ('total_pkt_recvd', (YLeaf(YType.uint32, 'total-pkt-recvd'), ['int'])),
                            ('pkt_drop_wrong_kc', (YLeaf(YType.uint32, 'pkt-drop-wrong-kc'), ['int'])),
                            ('pkt_drop_no_auth', (YLeaf(YType.uint32, 'pkt-drop-no-auth'), ['int'])),
                            ('pkt_drop_invalid_auth', (YLeaf(YType.uint32, 'pkt-drop-invalid-auth'), ['int'])),
                            ('pkt_accepted_valid_auth', (YLeaf(YType.uint32, 'pkt-accepted-valid-auth'), ['int'])),
                        ])
                        self.interface_name = None
                        self.interface = None
                        self.if_handle = None
                        self.rip_enabled = None
                        self.is_passive_interface = None
                        self.multicast_address = None
                        self.accept_metric = None
                        self.send_version = None
                        self.receive_version = None
                        self.state = None
                        self.destination_address = None
                        self.prefix_length = None
                        self.metric_cost = None
                        self.split_horizon = None
                        self.poison_horizon = None
                        self.triggered_rip = None
                        self.neighbor_address = None
                        self.oom_flags = None
                        self.join_status = None
                        self.lpts_state = None
                        self.auth_mode = None
                        self.auth_keychain = None
                        self.send_auth_key_exists = None
                        self.auth_key_md5 = None
                        self.auth_key_send_id = None
                        self.total_pkt_recvd = None
                        self.pkt_drop_wrong_kc = None
                        self.pkt_drop_no_auth = None
                        self.pkt_drop_invalid_auth = None
                        self.pkt_accepted_valid_auth = None

                        self.rip_summary = YList(self)
                        self.rip_peer = YList(self)
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface, ['interface_name', 'interface', 'if_handle', 'rip_enabled', 'is_passive_interface', 'multicast_address', 'accept_metric', 'send_version', 'receive_version', 'state', 'destination_address', 'prefix_length', 'metric_cost', 'split_horizon', 'poison_horizon', 'triggered_rip', 'neighbor_address', 'oom_flags', 'join_status', 'lpts_state', 'auth_mode', 'auth_keychain', 'send_auth_key_exists', 'auth_key_md5', 'auth_key_send_id', 'total_pkt_recvd', 'pkt_drop_wrong_kc', 'pkt_drop_no_auth', 'pkt_drop_invalid_auth', 'pkt_accepted_valid_auth'], name, value)


                    class RipSummary(Entity):
                        """
                        User defined summary addresses
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary, self).__init__()

                            self.yang_name = "rip-summary"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                ('metric', (YLeaf(YType.int32, 'metric'), ['int'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.next_hop_address = None
                            self.metric = None
                            self._segment_path = lambda: "rip-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary, ['prefix', 'prefix_length', 'next_hop_address', 'metric'], name, value)


                    class RipPeer(Entity):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, self).__init__()

                            self.yang_name = "rip-peer"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_uptime', (YLeaf(YType.uint32, 'peer-uptime'), ['int'])),
                                ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str'])),
                                ('peer_version', (YLeaf(YType.uint8, 'peer-version'), ['int'])),
                                ('discarded_peer_packets', (YLeaf(YType.uint32, 'discarded-peer-packets'), ['int'])),
                                ('discarded_peer_routes', (YLeaf(YType.uint32, 'discarded-peer-routes'), ['int'])),
                            ])
                            self.peer_uptime = None
                            self.peer_address = None
                            self.peer_version = None
                            self.discarded_peer_packets = None
                            self.discarded_peer_routes = None
                            self._segment_path = lambda: "rip-peer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


            class Global(Entity):
                """
                Global Information 
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global.VrfSummary>`
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global.InterfaceSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Global, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf-summary", ("vrf_summary", Rip.Vrfs.Vrf.Global.VrfSummary)), ("interface-summary", ("interface_summary", Rip.Vrfs.Vrf.Global.InterfaceSummary))])
                    self._leafs = OrderedDict()

                    self.vrf_summary = Rip.Vrfs.Vrf.Global.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"

                    self.interface_summary = YList(self)
                    self._segment_path = lambda: "global"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Global, [], name, value)


                class VrfSummary(Entity):
                    """
                    VRF summary data
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\: bool
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Global.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                            ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                            ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                            ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                            ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                            ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                            ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                            ('interface_configured_count', (YLeaf(YType.uint32, 'interface-configured-count'), ['int'])),
                            ('active_interface_count', (YLeaf(YType.uint32, 'active-interface-count'), ['int'])),
                        ])
                        self.vrf_name = None
                        self.active = None
                        self.oom_flags = None
                        self.route_count = None
                        self.path_count = None
                        self.update_timer = None
                        self.next_update_time = None
                        self.invalid_timer = None
                        self.hold_down_timer = None
                        self.flush_timer = None
                        self.interface_configured_count = None
                        self.active_interface_count = None
                        self._segment_path = lambda: "vrf-summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Global.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


                class InterfaceSummary(Entity):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Vrfs.Vrf.Global.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                            ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                            ('neighbor_count', (YLeaf(YType.uint32, 'neighbor-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.enabled = None
                        self.state = None
                        self.destination_address = None
                        self.prefix_length = None
                        self.oom_flags = None
                        self.send_version = None
                        self.receive_version = None
                        self.neighbor_count = None
                        self._segment_path = lambda: "interface-summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Global.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)


    class Protocol(Entity):
        """
        Protocol operational data
        
        .. attribute:: process
        
        	RIP global process 
        	**type**\:  :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process>`
        
        .. attribute:: default_vrf
        
        	RIP operational data for Default VRF
        	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.Protocol, self).__init__()

            self.yang_name = "protocol"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("process", ("process", Rip.Protocol.Process)), ("default-vrf", ("default_vrf", Rip.Protocol.DefaultVrf))])
            self._leafs = OrderedDict()

            self.process = Rip.Protocol.Process()
            self.process.parent = self
            self._children_name_map["process"] = "process"

            self.default_vrf = Rip.Protocol.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._segment_path = lambda: "protocol"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.Protocol, [], name, value)


        class Process(Entity):
            """
            RIP global process 
            
            .. attribute:: vrf_config_count
            
            	Number of VRFs configured
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_active_count
            
            	Number of active VRFs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: socket_descriptor
            
            	Socket descriptior
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: current_oom_state
            
            	Current OOM state
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrf_summary
            
            	List of VRFs configured
            	**type**\: list of  		 :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.Process.VrfSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Protocol.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "protocol"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf-summary", ("vrf_summary", Rip.Protocol.Process.VrfSummary))])
                self._leafs = OrderedDict([
                    ('vrf_config_count', (YLeaf(YType.uint32, 'vrf-config-count'), ['int'])),
                    ('vrf_active_count', (YLeaf(YType.uint32, 'vrf-active-count'), ['int'])),
                    ('socket_descriptor', (YLeaf(YType.int32, 'socket-descriptor'), ['int'])),
                    ('current_oom_state', (YLeaf(YType.int32, 'current-oom-state'), ['int'])),
                    ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                    ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                ])
                self.vrf_config_count = None
                self.vrf_active_count = None
                self.socket_descriptor = None
                self.current_oom_state = None
                self.route_count = None
                self.path_count = None

                self.vrf_summary = YList(self)
                self._segment_path = lambda: "process"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.Protocol.Process, ['vrf_config_count', 'vrf_active_count', 'socket_descriptor', 'current_oom_state', 'route_count', 'path_count'], name, value)


            class VrfSummary(Entity):
                """
                List of VRFs configured
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\: str
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\: bool
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.Process.VrfSummary, self).__init__()

                    self.yang_name = "vrf-summary"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                        ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                        ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                        ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                        ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                        ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                        ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                        ('interface_configured_count', (YLeaf(YType.uint32, 'interface-configured-count'), ['int'])),
                        ('active_interface_count', (YLeaf(YType.uint32, 'active-interface-count'), ['int'])),
                    ])
                    self.vrf_name = None
                    self.active = None
                    self.oom_flags = None
                    self.route_count = None
                    self.path_count = None
                    self.update_timer = None
                    self.next_update_time = None
                    self.invalid_timer = None
                    self.hold_down_timer = None
                    self.flush_timer = None
                    self.interface_configured_count = None
                    self.active_interface_count = None
                    self._segment_path = lambda: "vrf-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/process/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.Process.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


        class DefaultVrf(Entity):
            """
            RIP operational data for Default VRF
            
            .. attribute:: routes
            
            	RIP route database
            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes>`
            
            .. attribute:: configuration
            
            	RIP global configuration
            	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Configuration>`
            
            .. attribute:: statistics
            
            	RIP statistics information
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Statistics>`
            
            .. attribute:: interfaces
            
            	RIP interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces>`
            
            .. attribute:: global_
            
            	Global Information 
            	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Protocol.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "protocol"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("routes", ("routes", Rip.Protocol.DefaultVrf.Routes)), ("configuration", ("configuration", Rip.Protocol.DefaultVrf.Configuration)), ("statistics", ("statistics", Rip.Protocol.DefaultVrf.Statistics)), ("interfaces", ("interfaces", Rip.Protocol.DefaultVrf.Interfaces)), ("global", ("global_", Rip.Protocol.DefaultVrf.Global))])
                self._leafs = OrderedDict()

                self.routes = Rip.Protocol.DefaultVrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"

                self.configuration = Rip.Protocol.DefaultVrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"

                self.statistics = Rip.Protocol.DefaultVrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.interfaces = Rip.Protocol.DefaultVrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.global_ = Rip.Protocol.DefaultVrf.Global()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._segment_path = lambda: "default-vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.Protocol.DefaultVrf, [], name, value)


            class Routes(Entity):
                """
                RIP route database
                
                .. attribute:: route
                
                	A route in the RIP database
                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Routes, self).__init__()

                    self.yang_name = "routes"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("route", ("route", Rip.Protocol.DefaultVrf.Routes.Route))])
                    self._leafs = OrderedDict()

                    self.route = YList(self)
                    self._segment_path = lambda: "routes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Routes, [], name, value)


                class Route(Entity):
                    """
                    A route in the RIP database
                    
                    .. attribute:: prefix
                    
                    	Network prefix
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: destination_address
                    
                    	Destination IP Address for this route
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length_xr
                    
                    	Prefix length of IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: distance
                    
                    	Route administrative distance
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: bgp_count
                    
                    	Hop count for this route
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_type
                    
                    	Type of this route
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: route_summary
                    
                    	Summary route placeholder indicator
                    	**type**\: bool
                    
                    .. attribute:: route_tag
                    
                    	Generic route information
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	RIB supplied version number
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: attributes
                    
                    	RIB supplied route attributes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active
                    
                    	Active route indicator
                    	**type**\: bool
                    
                    .. attribute:: path_origin
                    
                    	Where this route was learnt
                    	**type**\:  :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                    
                    .. attribute:: hold_down
                    
                    	Indicates whether route is in holddown
                    	**type**\: bool
                    
                    .. attribute:: paths
                    
                    	The paths for this route
                    	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Routes.Route.Paths>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Routes.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "routes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("paths", ("paths", Rip.Protocol.DefaultVrf.Routes.Route.Paths))])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length_xr', (YLeaf(YType.uint32, 'prefix-length-xr'), ['int'])),
                            ('distance', (YLeaf(YType.uint16, 'distance'), ['int'])),
                            ('bgp_count', (YLeaf(YType.uint16, 'bgp-count'), ['int'])),
                            ('route_type', (YLeaf(YType.uint16, 'route-type'), ['int'])),
                            ('route_summary', (YLeaf(YType.boolean, 'route-summary'), ['bool'])),
                            ('route_tag', (YLeaf(YType.uint16, 'route-tag'), ['int'])),
                            ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                            ('attributes', (YLeaf(YType.uint32, 'attributes'), ['int'])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('path_origin', (YLeaf(YType.enumeration, 'path-origin'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOrigin', '')])),
                            ('hold_down', (YLeaf(YType.boolean, 'hold-down'), ['bool'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.destination_address = None
                        self.prefix_length_xr = None
                        self.distance = None
                        self.bgp_count = None
                        self.route_type = None
                        self.route_summary = None
                        self.route_tag = None
                        self.version = None
                        self.attributes = None
                        self.active = None
                        self.path_origin = None
                        self.hold_down = None

                        self.paths = YList(self)
                        self._segment_path = lambda: "route"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Routes.Route, ['prefix', 'prefix_length', 'destination_address', 'prefix_length_xr', 'distance', 'bgp_count', 'route_type', 'route_summary', 'route_tag', 'version', 'attributes', 'active', 'path_origin', 'hold_down'], name, value)


                    class Paths(Entity):
                        """
                        The paths for this route
                        
                        .. attribute:: source_address
                        
                        	Source address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: next_hop_address
                        
                        	Next hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: tag
                        
                        	Tag
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: interface
                        
                        	Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: uptime
                        
                        	Up time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_permanent
                        
                        	Permanent indicator
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Routes.Route.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "route"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('uptime', (YLeaf(YType.uint32, 'uptime'), ['int'])),
                                ('is_permanent', (YLeaf(YType.boolean, 'is-permanent'), ['bool'])),
                            ])
                            self.source_address = None
                            self.next_hop_address = None
                            self.metric = None
                            self.tag = None
                            self.interface = None
                            self.uptime = None
                            self.is_permanent = None
                            self._segment_path = lambda: "paths"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/route/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Protocol.DefaultVrf.Routes.Route.Paths, ['source_address', 'next_hop_address', 'metric', 'tag', 'interface', 'uptime', 'is_permanent'], name, value)


            class Configuration(Entity):
                """
                RIP global configuration
                
                .. attribute:: active
                
                	VRF active indicator
                	**type**\: bool
                
                .. attribute:: vr_fised_socket
                
                	VRF added to socket indicator
                	**type**\: bool
                
                .. attribute:: rip_version
                
                	Version of RIP configured
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: default_metric
                
                	Default metric for RIP routes
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: maximum_paths
                
                	Maximum number of paths a route can have
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: auto_summarize
                
                	Auto\-summarization indicator
                	**type**\: bool
                
                .. attribute:: multicast_address
                
                	Use broadcast/multicast address indicator
                	**type**\: bool
                
                .. attribute:: flash_threshold
                
                	Flash update threshold
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: input_q_length
                
                	Length of the input queue
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\: bool
                
                .. attribute:: validation_indicator
                
                	Incoming packet source validation indicator
                	**type**\: bool
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsf_status
                
                	NSF Enable status
                	**type**\: bool
                
                .. attribute:: nsf_life_time
                
                	NSF life time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('vr_fised_socket', (YLeaf(YType.boolean, 'vr-fised-socket'), ['bool'])),
                        ('rip_version', (YLeaf(YType.int32, 'rip-version'), ['int'])),
                        ('default_metric', (YLeaf(YType.uint8, 'default-metric'), ['int'])),
                        ('maximum_paths', (YLeaf(YType.uint8, 'maximum-paths'), ['int'])),
                        ('auto_summarize', (YLeaf(YType.boolean, 'auto-summarize'), ['bool'])),
                        ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                        ('flash_threshold', (YLeaf(YType.uint8, 'flash-threshold'), ['int'])),
                        ('input_q_length', (YLeaf(YType.uint16, 'input-q-length'), ['int'])),
                        ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                        ('validation_indicator', (YLeaf(YType.boolean, 'validation-indicator'), ['bool'])),
                        ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                        ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                        ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                        ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                        ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('nsf_status', (YLeaf(YType.boolean, 'nsf-status'), ['bool'])),
                        ('nsf_life_time', (YLeaf(YType.uint32, 'nsf-life-time'), ['int'])),
                    ])
                    self.active = None
                    self.vr_fised_socket = None
                    self.rip_version = None
                    self.default_metric = None
                    self.maximum_paths = None
                    self.auto_summarize = None
                    self.multicast_address = None
                    self.flash_threshold = None
                    self.input_q_length = None
                    self.triggered_rip = None
                    self.validation_indicator = None
                    self.update_timer = None
                    self.next_update_time = None
                    self.invalid_timer = None
                    self.hold_down_timer = None
                    self.flush_timer = None
                    self.oom_flags = None
                    self.nsf_status = None
                    self.nsf_life_time = None
                    self._segment_path = lambda: "configuration"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Configuration, ['active', 'vr_fised_socket', 'rip_version', 'default_metric', 'maximum_paths', 'auto_summarize', 'multicast_address', 'flash_threshold', 'input_q_length', 'triggered_rip', 'validation_indicator', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'oom_flags', 'nsf_status', 'nsf_life_time'], name, value)


            class Statistics(Entity):
                """
                RIP statistics information
                
                .. attribute:: received_packets
                
                	Total packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_packets
                
                	Total discarded packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: discarded_routes
                
                	Total discarded routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_packets_received
                
                	Packets rx in SRP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_messages
                
                	Number of messages sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_message_failures
                
                	Number of message send failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: query_responses
                
                	Number of RIP queries responded to
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: periodic_updates
                
                	Number of periodic RIP updates
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_malloc_failures
                
                	Number of failures to allocate memory for a route
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_malloc_failures
                
                	Number of failures to allocate memory for a path
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rib_updates
                
                	Number of route updates to RIB made by RIP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                        ('discarded_packets', (YLeaf(YType.uint32, 'discarded-packets'), ['int'])),
                        ('discarded_routes', (YLeaf(YType.uint32, 'discarded-routes'), ['int'])),
                        ('standby_packets_received', (YLeaf(YType.uint32, 'standby-packets-received'), ['int'])),
                        ('sent_messages', (YLeaf(YType.uint32, 'sent-messages'), ['int'])),
                        ('sent_message_failures', (YLeaf(YType.uint32, 'sent-message-failures'), ['int'])),
                        ('query_responses', (YLeaf(YType.uint32, 'query-responses'), ['int'])),
                        ('periodic_updates', (YLeaf(YType.uint32, 'periodic-updates'), ['int'])),
                        ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                        ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                        ('route_malloc_failures', (YLeaf(YType.uint32, 'route-malloc-failures'), ['int'])),
                        ('path_malloc_failures', (YLeaf(YType.uint32, 'path-malloc-failures'), ['int'])),
                        ('rib_updates', (YLeaf(YType.uint32, 'rib-updates'), ['int'])),
                    ])
                    self.received_packets = None
                    self.discarded_packets = None
                    self.discarded_routes = None
                    self.standby_packets_received = None
                    self.sent_messages = None
                    self.sent_message_failures = None
                    self.query_responses = None
                    self.periodic_updates = None
                    self.route_count = None
                    self.path_count = None
                    self.route_malloc_failures = None
                    self.path_malloc_failures = None
                    self.rib_updates = None
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Statistics, ['received_packets', 'discarded_packets', 'discarded_routes', 'standby_packets_received', 'sent_messages', 'sent_message_failures', 'query_responses', 'periodic_updates', 'route_count', 'path_count', 'route_malloc_failures', 'path_malloc_failures', 'rib_updates'], name, value)


            class Interfaces(Entity):
                """
                RIP interfaces
                
                .. attribute:: interface
                
                	Information about a particular RIP interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Rip.Protocol.DefaultVrf.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: rip_enabled
                    
                    	Whether RIP is enabled on this interface
                    	**type**\: bool
                    
                    .. attribute:: is_passive_interface
                    
                    	Passive interface indicator
                    	**type**\: bool
                    
                    .. attribute:: multicast_address
                    
                    	Use broadcast address for v2 packets
                    	**type**\: bool
                    
                    .. attribute:: accept_metric
                    
                    	Accept routes of metric 0 indicator
                    	**type**\: bool
                    
                    .. attribute:: send_version
                    
                    	Versions that the interface is sending
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	Versions that the interface will recieve
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	Current state of the interface
                    	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: destination_address
                    
                    	IP Address of this interface
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of the IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: metric_cost
                    
                    	Cost added to routes through this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: split_horizon
                    
                    	Split horizon enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: poison_horizon
                    
                    	Poisoned reverse enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: triggered_rip
                    
                    	Triggered RIP enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: neighbor_address
                    
                    	Interface's triggered RIP neighbor
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: oom_flags
                    
                    	Out\-of\-memory status flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_status
                    
                    	Multicast group join status
                    	**type**\: bool
                    
                    .. attribute:: lpts_state
                    
                    	LPTSState
                    	**type**\: bool
                    
                    .. attribute:: auth_mode
                    
                    	Authentication Mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_keychain
                    
                    	Authentication Keychain Name
                    	**type**\: str
                    
                    .. attribute:: send_auth_key_exists
                    
                    	Authentication send key exists
                    	**type**\: bool
                    
                    .. attribute:: auth_key_md5
                    
                    	Authentication key programmed with MD5 algorithm
                    	**type**\: bool
                    
                    .. attribute:: auth_key_send_id
                    
                    	Current active Send Authentication Key Id
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_pkt_recvd
                    
                    	Total packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_wrong_kc
                    
                    	Packets dropped due to wrong keychain configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_no_auth
                    
                    	Packets dropped due to missing authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_drop_invalid_auth
                    
                    	Packets dropped due to invalid authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pkt_accepted_valid_auth
                    
                    	Packets accepted with valid authentication data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rip_summary
                    
                    	User defined summary addresses
                    	**type**\: list of  		 :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary>`
                    
                    .. attribute:: rip_peer
                    
                    	Neighbors on this interface
                    	**type**\: list of  		 :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer>`
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("rip-summary", ("rip_summary", Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary)), ("rip-peer", ("rip_peer", Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                            ('rip_enabled', (YLeaf(YType.boolean, 'rip-enabled'), ['bool'])),
                            ('is_passive_interface', (YLeaf(YType.boolean, 'is-passive-interface'), ['bool'])),
                            ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                            ('accept_metric', (YLeaf(YType.boolean, 'accept-metric'), ['bool'])),
                            ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                            ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('metric_cost', (YLeaf(YType.uint32, 'metric-cost'), ['int'])),
                            ('split_horizon', (YLeaf(YType.boolean, 'split-horizon'), ['bool'])),
                            ('poison_horizon', (YLeaf(YType.boolean, 'poison-horizon'), ['bool'])),
                            ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('join_status', (YLeaf(YType.boolean, 'join-status'), ['bool'])),
                            ('lpts_state', (YLeaf(YType.boolean, 'lpts-state'), ['bool'])),
                            ('auth_mode', (YLeaf(YType.uint32, 'auth-mode'), ['int'])),
                            ('auth_keychain', (YLeaf(YType.str, 'auth-keychain'), ['str'])),
                            ('send_auth_key_exists', (YLeaf(YType.boolean, 'send-auth-key-exists'), ['bool'])),
                            ('auth_key_md5', (YLeaf(YType.boolean, 'auth-key-md5'), ['bool'])),
                            ('auth_key_send_id', (YLeaf(YType.uint64, 'auth-key-send-id'), ['int'])),
                            ('total_pkt_recvd', (YLeaf(YType.uint32, 'total-pkt-recvd'), ['int'])),
                            ('pkt_drop_wrong_kc', (YLeaf(YType.uint32, 'pkt-drop-wrong-kc'), ['int'])),
                            ('pkt_drop_no_auth', (YLeaf(YType.uint32, 'pkt-drop-no-auth'), ['int'])),
                            ('pkt_drop_invalid_auth', (YLeaf(YType.uint32, 'pkt-drop-invalid-auth'), ['int'])),
                            ('pkt_accepted_valid_auth', (YLeaf(YType.uint32, 'pkt-accepted-valid-auth'), ['int'])),
                        ])
                        self.interface_name = None
                        self.interface = None
                        self.if_handle = None
                        self.rip_enabled = None
                        self.is_passive_interface = None
                        self.multicast_address = None
                        self.accept_metric = None
                        self.send_version = None
                        self.receive_version = None
                        self.state = None
                        self.destination_address = None
                        self.prefix_length = None
                        self.metric_cost = None
                        self.split_horizon = None
                        self.poison_horizon = None
                        self.triggered_rip = None
                        self.neighbor_address = None
                        self.oom_flags = None
                        self.join_status = None
                        self.lpts_state = None
                        self.auth_mode = None
                        self.auth_keychain = None
                        self.send_auth_key_exists = None
                        self.auth_key_md5 = None
                        self.auth_key_send_id = None
                        self.total_pkt_recvd = None
                        self.pkt_drop_wrong_kc = None
                        self.pkt_drop_no_auth = None
                        self.pkt_drop_invalid_auth = None
                        self.pkt_accepted_valid_auth = None

                        self.rip_summary = YList(self)
                        self.rip_peer = YList(self)
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces.Interface, ['interface_name', 'interface', 'if_handle', 'rip_enabled', 'is_passive_interface', 'multicast_address', 'accept_metric', 'send_version', 'receive_version', 'state', 'destination_address', 'prefix_length', 'metric_cost', 'split_horizon', 'poison_horizon', 'triggered_rip', 'neighbor_address', 'oom_flags', 'join_status', 'lpts_state', 'auth_mode', 'auth_keychain', 'send_auth_key_exists', 'auth_key_md5', 'auth_key_send_id', 'total_pkt_recvd', 'pkt_drop_wrong_kc', 'pkt_drop_no_auth', 'pkt_drop_invalid_auth', 'pkt_accepted_valid_auth'], name, value)


                    class RipSummary(Entity):
                        """
                        User defined summary addresses
                        
                        .. attribute:: prefix
                        
                        	Summary address prefix
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Summary address prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_address
                        
                        	Summary address next hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: metric
                        
                        	Summary metric
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary, self).__init__()

                            self.yang_name = "rip-summary"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                ('metric', (YLeaf(YType.int32, 'metric'), ['int'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.next_hop_address = None
                            self.metric = None
                            self._segment_path = lambda: "rip-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary, ['prefix', 'prefix_length', 'next_hop_address', 'metric'], name, value)


                    class RipPeer(Entity):
                        """
                        Neighbors on this interface
                        
                        .. attribute:: peer_uptime
                        
                        	Uptime of this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_address
                        
                        	IP Address of this peer
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: peer_version
                        
                        	RIP version for this peer
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: discarded_peer_packets
                        
                        	Discarded packets from this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: discarded_peer_routes
                        
                        	Discarded routes from this peer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-rip-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, self).__init__()

                            self.yang_name = "rip-peer"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_uptime', (YLeaf(YType.uint32, 'peer-uptime'), ['int'])),
                                ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str'])),
                                ('peer_version', (YLeaf(YType.uint8, 'peer-version'), ['int'])),
                                ('discarded_peer_packets', (YLeaf(YType.uint32, 'discarded-peer-packets'), ['int'])),
                                ('discarded_peer_routes', (YLeaf(YType.uint32, 'discarded-peer-routes'), ['int'])),
                            ])
                            self.peer_uptime = None
                            self.peer_address = None
                            self.peer_version = None
                            self.discarded_peer_packets = None
                            self.discarded_peer_routes = None
                            self._segment_path = lambda: "rip-peer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


            class Global(Entity):
                """
                Global Information 
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global.VrfSummary>`
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global.InterfaceSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Global, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf-summary", ("vrf_summary", Rip.Protocol.DefaultVrf.Global.VrfSummary)), ("interface-summary", ("interface_summary", Rip.Protocol.DefaultVrf.Global.InterfaceSummary))])
                    self._leafs = OrderedDict()

                    self.vrf_summary = Rip.Protocol.DefaultVrf.Global.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"

                    self.interface_summary = YList(self)
                    self._segment_path = lambda: "global"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Global, [], name, value)


                class VrfSummary(Entity):
                    """
                    VRF summary data
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name
                    	**type**\: str
                    
                    .. attribute:: active
                    
                    	VRF Active indicator
                    	**type**\: bool
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_count
                    
                    	Number of routes allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_count
                    
                    	Number of paths allocated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_timer
                    
                    	Update timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_update_time
                    
                    	Time left for next update
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_timer
                    
                    	Invalid timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_down_timer
                    
                    	Holddown timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flush_timer
                    
                    	Flush timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_configured_count
                    
                    	Number of interfaces configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: active_interface_count
                    
                    	Number of active interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Global.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                            ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                            ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                            ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                            ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                            ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                            ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                            ('interface_configured_count', (YLeaf(YType.uint32, 'interface-configured-count'), ['int'])),
                            ('active_interface_count', (YLeaf(YType.uint32, 'active-interface-count'), ['int'])),
                        ])
                        self.vrf_name = None
                        self.active = None
                        self.oom_flags = None
                        self.route_count = None
                        self.path_count = None
                        self.update_timer = None
                        self.next_update_time = None
                        self.invalid_timer = None
                        self.hold_down_timer = None
                        self.flush_timer = None
                        self.interface_configured_count = None
                        self.active_interface_count = None
                        self._segment_path = lambda: "vrf-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Global.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


                class InterfaceSummary(Entity):
                    """
                    List of Interfaces configured
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: enabled
                    
                    	RIP enabled indicator
                    	**type**\: bool
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                    
                    .. attribute:: destination_address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length of IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oom_flags
                    
                    	Current OOM flags
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_version
                    
                    	RIP versions this interface sends out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_version
                    
                    	RIP versions this interface will receive
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: neighbor_count
                    
                    	Number of neighbors seen
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.Protocol.DefaultVrf.Global.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                            ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                            ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                            ('neighbor_count', (YLeaf(YType.uint32, 'neighbor-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.enabled = None
                        self.state = None
                        self.destination_address = None
                        self.prefix_length = None
                        self.oom_flags = None
                        self.send_version = None
                        self.receive_version = None
                        self.neighbor_count = None
                        self._segment_path = lambda: "interface-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Global.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)


    class DefaultVrf(Entity):
        """
        RIP operational data for Default VRF
        
        .. attribute:: routes
        
        	RIP route database
        	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes>`
        
        .. attribute:: configuration
        
        	RIP global configuration
        	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Configuration>`
        
        .. attribute:: statistics
        
        	RIP statistics information
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Statistics>`
        
        .. attribute:: interfaces
        
        	RIP interfaces
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces>`
        
        .. attribute:: global_
        
        	Global Information 
        	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("routes", ("routes", Rip.DefaultVrf.Routes)), ("configuration", ("configuration", Rip.DefaultVrf.Configuration)), ("statistics", ("statistics", Rip.DefaultVrf.Statistics)), ("interfaces", ("interfaces", Rip.DefaultVrf.Interfaces)), ("global", ("global_", Rip.DefaultVrf.Global))])
            self._leafs = OrderedDict()

            self.routes = Rip.DefaultVrf.Routes()
            self.routes.parent = self
            self._children_name_map["routes"] = "routes"

            self.configuration = Rip.DefaultVrf.Configuration()
            self.configuration.parent = self
            self._children_name_map["configuration"] = "configuration"

            self.statistics = Rip.DefaultVrf.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.global_ = Rip.DefaultVrf.Global()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.DefaultVrf, [], name, value)


        class Routes(Entity):
            """
            RIP route database
            
            .. attribute:: route
            
            	A route in the RIP database
            	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Routes, self).__init__()

                self.yang_name = "routes"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("route", ("route", Rip.DefaultVrf.Routes.Route))])
                self._leafs = OrderedDict()

                self.route = YList(self)
                self._segment_path = lambda: "routes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Routes, [], name, value)


            class Route(Entity):
                """
                A route in the RIP database
                
                .. attribute:: prefix
                
                	Network prefix
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..32
                
                .. attribute:: destination_address
                
                	Destination IP Address for this route
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length_xr
                
                	Prefix length of IP address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: distance
                
                	Route administrative distance
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: bgp_count
                
                	Hop count for this route
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: route_type
                
                	Type of this route
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: route_summary
                
                	Summary route placeholder indicator
                	**type**\: bool
                
                .. attribute:: route_tag
                
                	Generic route information
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: version
                
                	RIB supplied version number
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: attributes
                
                	RIB supplied route attributes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: active
                
                	Active route indicator
                	**type**\: bool
                
                .. attribute:: path_origin
                
                	Where this route was learnt
                	**type**\:  :py:class:`RipRouteOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.RipRouteOrigin>`
                
                .. attribute:: hold_down
                
                	Indicates whether route is in holddown
                	**type**\: bool
                
                .. attribute:: paths
                
                	The paths for this route
                	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Routes.Route.Paths>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Routes.Route, self).__init__()

                    self.yang_name = "route"
                    self.yang_parent_name = "routes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("paths", ("paths", Rip.DefaultVrf.Routes.Route.Paths))])
                    self._leafs = OrderedDict([
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                        ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                        ('prefix_length_xr', (YLeaf(YType.uint32, 'prefix-length-xr'), ['int'])),
                        ('distance', (YLeaf(YType.uint16, 'distance'), ['int'])),
                        ('bgp_count', (YLeaf(YType.uint16, 'bgp-count'), ['int'])),
                        ('route_type', (YLeaf(YType.uint16, 'route-type'), ['int'])),
                        ('route_summary', (YLeaf(YType.boolean, 'route-summary'), ['bool'])),
                        ('route_tag', (YLeaf(YType.uint16, 'route-tag'), ['int'])),
                        ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                        ('attributes', (YLeaf(YType.uint32, 'attributes'), ['int'])),
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('path_origin', (YLeaf(YType.enumeration, 'path-origin'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOrigin', '')])),
                        ('hold_down', (YLeaf(YType.boolean, 'hold-down'), ['bool'])),
                    ])
                    self.prefix = None
                    self.prefix_length = None
                    self.destination_address = None
                    self.prefix_length_xr = None
                    self.distance = None
                    self.bgp_count = None
                    self.route_type = None
                    self.route_summary = None
                    self.route_tag = None
                    self.version = None
                    self.attributes = None
                    self.active = None
                    self.path_origin = None
                    self.hold_down = None

                    self.paths = YList(self)
                    self._segment_path = lambda: "route"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Routes.Route, ['prefix', 'prefix_length', 'destination_address', 'prefix_length_xr', 'distance', 'bgp_count', 'route_type', 'route_summary', 'route_tag', 'version', 'attributes', 'active', 'path_origin', 'hold_down'], name, value)


                class Paths(Entity):
                    """
                    The paths for this route
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: next_hop_address
                    
                    	Next hop address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: metric
                    
                    	Metric
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: tag
                    
                    	Tag
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: uptime
                    
                    	Up time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_permanent
                    
                    	Permanent indicator
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Routes.Route.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "route"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                            ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                            ('tag', (YLeaf(YType.uint16, 'tag'), ['int'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('uptime', (YLeaf(YType.uint32, 'uptime'), ['int'])),
                            ('is_permanent', (YLeaf(YType.boolean, 'is-permanent'), ['bool'])),
                        ])
                        self.source_address = None
                        self.next_hop_address = None
                        self.metric = None
                        self.tag = None
                        self.interface = None
                        self.uptime = None
                        self.is_permanent = None
                        self._segment_path = lambda: "paths"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/route/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Routes.Route.Paths, ['source_address', 'next_hop_address', 'metric', 'tag', 'interface', 'uptime', 'is_permanent'], name, value)


        class Configuration(Entity):
            """
            RIP global configuration
            
            .. attribute:: active
            
            	VRF active indicator
            	**type**\: bool
            
            .. attribute:: vr_fised_socket
            
            	VRF added to socket indicator
            	**type**\: bool
            
            .. attribute:: rip_version
            
            	Version of RIP configured
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: default_metric
            
            	Default metric for RIP routes
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: maximum_paths
            
            	Maximum number of paths a route can have
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: auto_summarize
            
            	Auto\-summarization indicator
            	**type**\: bool
            
            .. attribute:: multicast_address
            
            	Use broadcast/multicast address indicator
            	**type**\: bool
            
            .. attribute:: flash_threshold
            
            	Flash update threshold
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: input_q_length
            
            	Length of the input queue
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: triggered_rip
            
            	Triggered RIP enabled indicator
            	**type**\: bool
            
            .. attribute:: validation_indicator
            
            	Incoming packet source validation indicator
            	**type**\: bool
            
            .. attribute:: update_timer
            
            	Update timer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: next_update_time
            
            	Time left for next update
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: invalid_timer
            
            	Invalid timer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: hold_down_timer
            
            	Holddown timer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: flush_timer
            
            	Flush timer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: oom_flags
            
            	Out\-of\-memory status flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsf_status
            
            	NSF Enable status
            	**type**\: bool
            
            .. attribute:: nsf_life_time
            
            	NSF life time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Configuration, self).__init__()

                self.yang_name = "configuration"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                    ('vr_fised_socket', (YLeaf(YType.boolean, 'vr-fised-socket'), ['bool'])),
                    ('rip_version', (YLeaf(YType.int32, 'rip-version'), ['int'])),
                    ('default_metric', (YLeaf(YType.uint8, 'default-metric'), ['int'])),
                    ('maximum_paths', (YLeaf(YType.uint8, 'maximum-paths'), ['int'])),
                    ('auto_summarize', (YLeaf(YType.boolean, 'auto-summarize'), ['bool'])),
                    ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                    ('flash_threshold', (YLeaf(YType.uint8, 'flash-threshold'), ['int'])),
                    ('input_q_length', (YLeaf(YType.uint16, 'input-q-length'), ['int'])),
                    ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                    ('validation_indicator', (YLeaf(YType.boolean, 'validation-indicator'), ['bool'])),
                    ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                    ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                    ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                    ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                    ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                    ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                    ('nsf_status', (YLeaf(YType.boolean, 'nsf-status'), ['bool'])),
                    ('nsf_life_time', (YLeaf(YType.uint32, 'nsf-life-time'), ['int'])),
                ])
                self.active = None
                self.vr_fised_socket = None
                self.rip_version = None
                self.default_metric = None
                self.maximum_paths = None
                self.auto_summarize = None
                self.multicast_address = None
                self.flash_threshold = None
                self.input_q_length = None
                self.triggered_rip = None
                self.validation_indicator = None
                self.update_timer = None
                self.next_update_time = None
                self.invalid_timer = None
                self.hold_down_timer = None
                self.flush_timer = None
                self.oom_flags = None
                self.nsf_status = None
                self.nsf_life_time = None
                self._segment_path = lambda: "configuration"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Configuration, ['active', 'vr_fised_socket', 'rip_version', 'default_metric', 'maximum_paths', 'auto_summarize', 'multicast_address', 'flash_threshold', 'input_q_length', 'triggered_rip', 'validation_indicator', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'oom_flags', 'nsf_status', 'nsf_life_time'], name, value)


        class Statistics(Entity):
            """
            RIP statistics information
            
            .. attribute:: received_packets
            
            	Total packets received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: discarded_packets
            
            	Total discarded packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: discarded_routes
            
            	Total discarded routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: standby_packets_received
            
            	Packets rx in SRP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_messages
            
            	Number of messages sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sent_message_failures
            
            	Number of message send failures
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: query_responses
            
            	Number of RIP queries responded to
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: periodic_updates
            
            	Number of periodic RIP updates
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_count
            
            	Number of routes allocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_count
            
            	Number of paths allocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: route_malloc_failures
            
            	Number of failures to allocate memory for a route
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: path_malloc_failures
            
            	Number of failures to allocate memory for a path
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rib_updates
            
            	Number of route updates to RIB made by RIP
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('received_packets', (YLeaf(YType.uint32, 'received-packets'), ['int'])),
                    ('discarded_packets', (YLeaf(YType.uint32, 'discarded-packets'), ['int'])),
                    ('discarded_routes', (YLeaf(YType.uint32, 'discarded-routes'), ['int'])),
                    ('standby_packets_received', (YLeaf(YType.uint32, 'standby-packets-received'), ['int'])),
                    ('sent_messages', (YLeaf(YType.uint32, 'sent-messages'), ['int'])),
                    ('sent_message_failures', (YLeaf(YType.uint32, 'sent-message-failures'), ['int'])),
                    ('query_responses', (YLeaf(YType.uint32, 'query-responses'), ['int'])),
                    ('periodic_updates', (YLeaf(YType.uint32, 'periodic-updates'), ['int'])),
                    ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                    ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                    ('route_malloc_failures', (YLeaf(YType.uint32, 'route-malloc-failures'), ['int'])),
                    ('path_malloc_failures', (YLeaf(YType.uint32, 'path-malloc-failures'), ['int'])),
                    ('rib_updates', (YLeaf(YType.uint32, 'rib-updates'), ['int'])),
                ])
                self.received_packets = None
                self.discarded_packets = None
                self.discarded_routes = None
                self.standby_packets_received = None
                self.sent_messages = None
                self.sent_message_failures = None
                self.query_responses = None
                self.periodic_updates = None
                self.route_count = None
                self.path_count = None
                self.route_malloc_failures = None
                self.path_malloc_failures = None
                self.rib_updates = None
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Statistics, ['received_packets', 'discarded_packets', 'discarded_routes', 'standby_packets_received', 'sent_messages', 'sent_message_failures', 'query_responses', 'periodic_updates', 'route_count', 'path_count', 'route_malloc_failures', 'path_malloc_failures', 'rib_updates'], name, value)


        class Interfaces(Entity):
            """
            RIP interfaces
            
            .. attribute:: interface
            
            	Information about a particular RIP interface
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Rip.DefaultVrf.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Information about a particular RIP interface
                
                .. attribute:: interface_name  (key)
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface
                
                	Interface name
                	**type**\: str
                
                .. attribute:: if_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: rip_enabled
                
                	Whether RIP is enabled on this interface
                	**type**\: bool
                
                .. attribute:: is_passive_interface
                
                	Passive interface indicator
                	**type**\: bool
                
                .. attribute:: multicast_address
                
                	Use broadcast address for v2 packets
                	**type**\: bool
                
                .. attribute:: accept_metric
                
                	Accept routes of metric 0 indicator
                	**type**\: bool
                
                .. attribute:: send_version
                
                	Versions that the interface is sending
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	Versions that the interface will recieve
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	Current state of the interface
                	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                
                .. attribute:: destination_address
                
                	IP Address of this interface
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	Prefix length of the IP address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: metric_cost
                
                	Cost added to routes through this interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: split_horizon
                
                	Split horizon enabled indicator
                	**type**\: bool
                
                .. attribute:: poison_horizon
                
                	Poisoned reverse enabled indicator
                	**type**\: bool
                
                .. attribute:: triggered_rip
                
                	Triggered RIP enabled indicator
                	**type**\: bool
                
                .. attribute:: neighbor_address
                
                	Interface's triggered RIP neighbor
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: oom_flags
                
                	Out\-of\-memory status flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: join_status
                
                	Multicast group join status
                	**type**\: bool
                
                .. attribute:: lpts_state
                
                	LPTSState
                	**type**\: bool
                
                .. attribute:: auth_mode
                
                	Authentication Mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_keychain
                
                	Authentication Keychain Name
                	**type**\: str
                
                .. attribute:: send_auth_key_exists
                
                	Authentication send key exists
                	**type**\: bool
                
                .. attribute:: auth_key_md5
                
                	Authentication key programmed with MD5 algorithm
                	**type**\: bool
                
                .. attribute:: auth_key_send_id
                
                	Current active Send Authentication Key Id
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_pkt_recvd
                
                	Total packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_wrong_kc
                
                	Packets dropped due to wrong keychain configured
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_no_auth
                
                	Packets dropped due to missing authentication data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_drop_invalid_auth
                
                	Packets dropped due to invalid authentication data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pkt_accepted_valid_auth
                
                	Packets accepted with valid authentication data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rip_summary
                
                	User defined summary addresses
                	**type**\: list of  		 :py:class:`RipSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipSummary>`
                
                .. attribute:: rip_peer
                
                	Neighbors on this interface
                	**type**\: list of  		 :py:class:`RipPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Interfaces.Interface.RipPeer>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("rip-summary", ("rip_summary", Rip.DefaultVrf.Interfaces.Interface.RipSummary)), ("rip-peer", ("rip_peer", Rip.DefaultVrf.Interfaces.Interface.RipPeer))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                        ('rip_enabled', (YLeaf(YType.boolean, 'rip-enabled'), ['bool'])),
                        ('is_passive_interface', (YLeaf(YType.boolean, 'is-passive-interface'), ['bool'])),
                        ('multicast_address', (YLeaf(YType.boolean, 'multicast-address'), ['bool'])),
                        ('accept_metric', (YLeaf(YType.boolean, 'accept-metric'), ['bool'])),
                        ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                        ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                        ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                        ('metric_cost', (YLeaf(YType.uint32, 'metric-cost'), ['int'])),
                        ('split_horizon', (YLeaf(YType.boolean, 'split-horizon'), ['bool'])),
                        ('poison_horizon', (YLeaf(YType.boolean, 'poison-horizon'), ['bool'])),
                        ('triggered_rip', (YLeaf(YType.boolean, 'triggered-rip'), ['bool'])),
                        ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('join_status', (YLeaf(YType.boolean, 'join-status'), ['bool'])),
                        ('lpts_state', (YLeaf(YType.boolean, 'lpts-state'), ['bool'])),
                        ('auth_mode', (YLeaf(YType.uint32, 'auth-mode'), ['int'])),
                        ('auth_keychain', (YLeaf(YType.str, 'auth-keychain'), ['str'])),
                        ('send_auth_key_exists', (YLeaf(YType.boolean, 'send-auth-key-exists'), ['bool'])),
                        ('auth_key_md5', (YLeaf(YType.boolean, 'auth-key-md5'), ['bool'])),
                        ('auth_key_send_id', (YLeaf(YType.uint64, 'auth-key-send-id'), ['int'])),
                        ('total_pkt_recvd', (YLeaf(YType.uint32, 'total-pkt-recvd'), ['int'])),
                        ('pkt_drop_wrong_kc', (YLeaf(YType.uint32, 'pkt-drop-wrong-kc'), ['int'])),
                        ('pkt_drop_no_auth', (YLeaf(YType.uint32, 'pkt-drop-no-auth'), ['int'])),
                        ('pkt_drop_invalid_auth', (YLeaf(YType.uint32, 'pkt-drop-invalid-auth'), ['int'])),
                        ('pkt_accepted_valid_auth', (YLeaf(YType.uint32, 'pkt-accepted-valid-auth'), ['int'])),
                    ])
                    self.interface_name = None
                    self.interface = None
                    self.if_handle = None
                    self.rip_enabled = None
                    self.is_passive_interface = None
                    self.multicast_address = None
                    self.accept_metric = None
                    self.send_version = None
                    self.receive_version = None
                    self.state = None
                    self.destination_address = None
                    self.prefix_length = None
                    self.metric_cost = None
                    self.split_horizon = None
                    self.poison_horizon = None
                    self.triggered_rip = None
                    self.neighbor_address = None
                    self.oom_flags = None
                    self.join_status = None
                    self.lpts_state = None
                    self.auth_mode = None
                    self.auth_keychain = None
                    self.send_auth_key_exists = None
                    self.auth_key_md5 = None
                    self.auth_key_send_id = None
                    self.total_pkt_recvd = None
                    self.pkt_drop_wrong_kc = None
                    self.pkt_drop_no_auth = None
                    self.pkt_drop_invalid_auth = None
                    self.pkt_accepted_valid_auth = None

                    self.rip_summary = YList(self)
                    self.rip_peer = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface, ['interface_name', 'interface', 'if_handle', 'rip_enabled', 'is_passive_interface', 'multicast_address', 'accept_metric', 'send_version', 'receive_version', 'state', 'destination_address', 'prefix_length', 'metric_cost', 'split_horizon', 'poison_horizon', 'triggered_rip', 'neighbor_address', 'oom_flags', 'join_status', 'lpts_state', 'auth_mode', 'auth_keychain', 'send_auth_key_exists', 'auth_key_md5', 'auth_key_send_id', 'total_pkt_recvd', 'pkt_drop_wrong_kc', 'pkt_drop_no_auth', 'pkt_drop_invalid_auth', 'pkt_accepted_valid_auth'], name, value)


                class RipSummary(Entity):
                    """
                    User defined summary addresses
                    
                    .. attribute:: prefix
                    
                    	Summary address prefix
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Summary address prefix length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop_address
                    
                    	Summary address next hop
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: metric
                    
                    	Summary metric
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.RipSummary, self).__init__()

                        self.yang_name = "rip-summary"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                            ('metric', (YLeaf(YType.int32, 'metric'), ['int'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.next_hop_address = None
                        self.metric = None
                        self._segment_path = lambda: "rip-summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.RipSummary, ['prefix', 'prefix_length', 'next_hop_address', 'metric'], name, value)


                class RipPeer(Entity):
                    """
                    Neighbors on this interface
                    
                    .. attribute:: peer_uptime
                    
                    	Uptime of this peer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_address
                    
                    	IP Address of this peer
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: peer_version
                    
                    	RIP version for this peer
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: discarded_peer_packets
                    
                    	Discarded packets from this peer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discarded_peer_routes
                    
                    	Discarded routes from this peer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rip-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rip.DefaultVrf.Interfaces.Interface.RipPeer, self).__init__()

                        self.yang_name = "rip-peer"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('peer_uptime', (YLeaf(YType.uint32, 'peer-uptime'), ['int'])),
                            ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str'])),
                            ('peer_version', (YLeaf(YType.uint8, 'peer-version'), ['int'])),
                            ('discarded_peer_packets', (YLeaf(YType.uint32, 'discarded-peer-packets'), ['int'])),
                            ('discarded_peer_routes', (YLeaf(YType.uint32, 'discarded-peer-routes'), ['int'])),
                        ])
                        self.peer_uptime = None
                        self.peer_address = None
                        self.peer_version = None
                        self.discarded_peer_packets = None
                        self.discarded_peer_routes = None
                        self._segment_path = lambda: "rip-peer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


        class Global(Entity):
            """
            Global Information 
            
            .. attribute:: vrf_summary
            
            	VRF summary data
            	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global.VrfSummary>`
            
            .. attribute:: interface_summary
            
            	List of Interfaces configured
            	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global.InterfaceSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Global, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf-summary", ("vrf_summary", Rip.DefaultVrf.Global.VrfSummary)), ("interface-summary", ("interface_summary", Rip.DefaultVrf.Global.InterfaceSummary))])
                self._leafs = OrderedDict()

                self.vrf_summary = Rip.DefaultVrf.Global.VrfSummary()
                self.vrf_summary.parent = self
                self._children_name_map["vrf_summary"] = "vrf-summary"

                self.interface_summary = YList(self)
                self._segment_path = lambda: "global"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Global, [], name, value)


            class VrfSummary(Entity):
                """
                VRF summary data
                
                .. attribute:: vrf_name
                
                	VRF Name
                	**type**\: str
                
                .. attribute:: active
                
                	VRF Active indicator
                	**type**\: bool
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_count
                
                	Number of routes allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_count
                
                	Number of paths allocated
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: update_timer
                
                	Update timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_update_time
                
                	Time left for next update
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: invalid_timer
                
                	Invalid timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: hold_down_timer
                
                	Holddown timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flush_timer
                
                	Flush timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_configured_count
                
                	Number of interfaces configured
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: active_interface_count
                
                	Number of active interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Global.VrfSummary, self).__init__()

                    self.yang_name = "vrf-summary"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('route_count', (YLeaf(YType.uint32, 'route-count'), ['int'])),
                        ('path_count', (YLeaf(YType.uint32, 'path-count'), ['int'])),
                        ('update_timer', (YLeaf(YType.uint32, 'update-timer'), ['int'])),
                        ('next_update_time', (YLeaf(YType.uint32, 'next-update-time'), ['int'])),
                        ('invalid_timer', (YLeaf(YType.uint32, 'invalid-timer'), ['int'])),
                        ('hold_down_timer', (YLeaf(YType.uint32, 'hold-down-timer'), ['int'])),
                        ('flush_timer', (YLeaf(YType.uint32, 'flush-timer'), ['int'])),
                        ('interface_configured_count', (YLeaf(YType.uint32, 'interface-configured-count'), ['int'])),
                        ('active_interface_count', (YLeaf(YType.uint32, 'active-interface-count'), ['int'])),
                    ])
                    self.vrf_name = None
                    self.active = None
                    self.oom_flags = None
                    self.route_count = None
                    self.path_count = None
                    self.update_timer = None
                    self.next_update_time = None
                    self.invalid_timer = None
                    self.hold_down_timer = None
                    self.flush_timer = None
                    self.interface_configured_count = None
                    self.active_interface_count = None
                    self._segment_path = lambda: "vrf-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Global.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


            class InterfaceSummary(Entity):
                """
                List of Interfaces configured
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\: str
                
                .. attribute:: enabled
                
                	RIP enabled indicator
                	**type**\: bool
                
                .. attribute:: state
                
                	Interface state
                	**type**\:  :py:class:`InterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.InterfaceState>`
                
                .. attribute:: destination_address
                
                	IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	Prefix length of IP address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: oom_flags
                
                	Current OOM flags
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: send_version
                
                	RIP versions this interface sends out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_version
                
                	RIP versions this interface will receive
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor_count
                
                	Number of neighbors seen
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.DefaultVrf.Global.InterfaceSummary, self).__init__()

                    self.yang_name = "interface-summary"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceState', '')])),
                        ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                        ('oom_flags', (YLeaf(YType.uint32, 'oom-flags'), ['int'])),
                        ('send_version', (YLeaf(YType.uint32, 'send-version'), ['int'])),
                        ('receive_version', (YLeaf(YType.uint32, 'receive-version'), ['int'])),
                        ('neighbor_count', (YLeaf(YType.uint32, 'neighbor-count'), ['int'])),
                    ])
                    self.interface_name = None
                    self.enabled = None
                    self.state = None
                    self.destination_address = None
                    self.prefix_length = None
                    self.oom_flags = None
                    self.send_version = None
                    self.receive_version = None
                    self.neighbor_count = None
                    self._segment_path = lambda: "interface-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Global.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity

