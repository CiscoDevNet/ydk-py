""" Cisco_IOS_XR_ip_rip_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rip package operational data.

This module contains definitions
for the following management objects\:
  rip\: RIP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class InterfaceState(Enum):
    """
    InterfaceState

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
    RipRouteOrigin

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
        self._child_container_classes = {"vrfs" : ("vrfs", Rip.Vrfs), "protocol" : ("protocol", Rip.Protocol), "default-vrf" : ("default_vrf", Rip.DefaultVrf)}
        self._child_list_classes = {}

        self.vrfs = Rip.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")

        self.protocol = Rip.Protocol()
        self.protocol.parent = self
        self._children_name_map["protocol"] = "protocol"
        self._children_yang_names.add("protocol")

        self.default_vrf = Rip.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip"


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
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", Rip.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Rip.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            Operational data for a particular VRF
            
            .. attribute:: vrf_name  <key>
            
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
            	**type**\:  :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"routes" : ("routes", Rip.Vrfs.Vrf.Routes), "configuration" : ("configuration", Rip.Vrfs.Vrf.Configuration), "statistics" : ("statistics", Rip.Vrfs.Vrf.Statistics), "interfaces" : ("interfaces", Rip.Vrfs.Vrf.Interfaces), "global" : ("global_", Rip.Vrfs.Vrf.Global_)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.routes = Rip.Vrfs.Vrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"
                self._children_yang_names.add("routes")

                self.configuration = Rip.Vrfs.Vrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.statistics = Rip.Vrfs.Vrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.interfaces = Rip.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.global_ = Rip.Vrfs.Vrf.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/vrfs/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {"route" : ("route", Rip.Vrfs.Vrf.Routes.Route)}

                    self.route = YList(self)
                    self._segment_path = lambda: "routes"

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
                        self._child_container_classes = {}
                        self._child_list_classes = {"paths" : ("paths", Rip.Vrfs.Vrf.Routes.Route.Paths)}

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                        self.distance = YLeaf(YType.uint16, "distance")

                        self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                        self.route_type = YLeaf(YType.uint16, "route-type")

                        self.route_summary = YLeaf(YType.boolean, "route-summary")

                        self.route_tag = YLeaf(YType.uint16, "route-tag")

                        self.version = YLeaf(YType.uint8, "version")

                        self.attributes = YLeaf(YType.uint32, "attributes")

                        self.active = YLeaf(YType.boolean, "active")

                        self.path_origin = YLeaf(YType.enumeration, "path-origin")

                        self.hold_down = YLeaf(YType.boolean, "hold-down")

                        self.paths = YList(self)
                        self._segment_path = lambda: "route"

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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.metric = YLeaf(YType.uint16, "metric")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.interface = YLeaf(YType.str, "interface")

                            self.uptime = YLeaf(YType.uint32, "uptime")

                            self.is_permanent = YLeaf(YType.boolean, "is-permanent")
                            self._segment_path = lambda: "paths"

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active = YLeaf(YType.boolean, "active")

                    self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

                    self.rip_version = YLeaf(YType.int32, "rip-version")

                    self.default_metric = YLeaf(YType.uint8, "default-metric")

                    self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                    self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                    self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                    self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")
                    self._segment_path = lambda: "configuration"

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                    self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                    self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

                    self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                    self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                    self.query_responses = YLeaf(YType.uint32, "query-responses")

                    self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                    self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                    self.rib_updates = YLeaf(YType.uint32, "rib-updates")
                    self._segment_path = lambda: "statistics"

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
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Rip.Vrfs.Vrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {"rip-summary" : ("rip_summary", Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary), "rip-peer" : ("rip_peer", Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.if_handle = YLeaf(YType.str, "if-handle")

                        self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                        self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                        self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                        self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                        self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                        self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                        self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.join_status = YLeaf(YType.boolean, "join-status")

                        self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                        self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                        self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                        self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                        self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                        self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                        self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                        self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                        self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                        self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                        self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                        self.rip_summary = YList(self)
                        self.rip_peer = YList(self)
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.metric = YLeaf(YType.int32, "metric")
                            self._segment_path = lambda: "rip-summary"

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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                            self.peer_address = YLeaf(YType.str, "peer-address")

                            self.peer_version = YLeaf(YType.uint8, "peer-version")

                            self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                            self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")
                            self._segment_path = lambda: "rip-peer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


            class Global_(Entity):
                """
                Global Information 
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.VrfSummary>`
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Vrfs.Vrf.Global_.InterfaceSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Vrfs.Vrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"vrf-summary" : ("vrf_summary", Rip.Vrfs.Vrf.Global_.VrfSummary)}
                    self._child_list_classes = {"interface-summary" : ("interface_summary", Rip.Vrfs.Vrf.Global_.InterfaceSummary)}

                    self.vrf_summary = Rip.Vrfs.Vrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"
                    self._children_yang_names.add("vrf-summary")

                    self.interface_summary = YList(self)
                    self._segment_path = lambda: "global"

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Vrfs.Vrf.Global_, [], name, value)


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
                        super(Rip.Vrfs.Vrf.Global_.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.active = YLeaf(YType.boolean, "active")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.route_count = YLeaf(YType.uint32, "route-count")

                        self.path_count = YLeaf(YType.uint32, "path-count")

                        self.update_timer = YLeaf(YType.uint32, "update-timer")

                        self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                        self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                        self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                        self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                        self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                        self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")
                        self._segment_path = lambda: "vrf-summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Global_.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


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
                        super(Rip.Vrfs.Vrf.Global_.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")
                        self._segment_path = lambda: "interface-summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Vrfs.Vrf.Global_.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)


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
            self._child_container_classes = {"process" : ("process", Rip.Protocol.Process), "default-vrf" : ("default_vrf", Rip.Protocol.DefaultVrf)}
            self._child_list_classes = {}

            self.process = Rip.Protocol.Process()
            self.process.parent = self
            self._children_name_map["process"] = "process"
            self._children_yang_names.add("process")

            self.default_vrf = Rip.Protocol.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._children_yang_names.add("default-vrf")
            self._segment_path = lambda: "protocol"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()


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
                self._child_container_classes = {}
                self._child_list_classes = {"vrf-summary" : ("vrf_summary", Rip.Protocol.Process.VrfSummary)}

                self.vrf_config_count = YLeaf(YType.uint32, "vrf-config-count")

                self.vrf_active_count = YLeaf(YType.uint32, "vrf-active-count")

                self.socket_descriptor = YLeaf(YType.int32, "socket-descriptor")

                self.current_oom_state = YLeaf(YType.int32, "current-oom-state")

                self.route_count = YLeaf(YType.uint32, "route-count")

                self.path_count = YLeaf(YType.uint32, "path-count")

                self.vrf_summary = YList(self)
                self._segment_path = lambda: "process"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.active = YLeaf(YType.boolean, "active")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                    self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")
                    self._segment_path = lambda: "vrf-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/process/%s" % self._segment_path()

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
            	**type**\:  :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.Protocol.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "protocol"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"routes" : ("routes", Rip.Protocol.DefaultVrf.Routes), "configuration" : ("configuration", Rip.Protocol.DefaultVrf.Configuration), "statistics" : ("statistics", Rip.Protocol.DefaultVrf.Statistics), "interfaces" : ("interfaces", Rip.Protocol.DefaultVrf.Interfaces), "global" : ("global_", Rip.Protocol.DefaultVrf.Global_)}
                self._child_list_classes = {}

                self.routes = Rip.Protocol.DefaultVrf.Routes()
                self.routes.parent = self
                self._children_name_map["routes"] = "routes"
                self._children_yang_names.add("routes")

                self.configuration = Rip.Protocol.DefaultVrf.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.statistics = Rip.Protocol.DefaultVrf.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.interfaces = Rip.Protocol.DefaultVrf.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.global_ = Rip.Protocol.DefaultVrf.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")
                self._segment_path = lambda: "default-vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/%s" % self._segment_path()


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
                    self._child_container_classes = {}
                    self._child_list_classes = {"route" : ("route", Rip.Protocol.DefaultVrf.Routes.Route)}

                    self.route = YList(self)
                    self._segment_path = lambda: "routes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()

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
                        self._child_container_classes = {}
                        self._child_list_classes = {"paths" : ("paths", Rip.Protocol.DefaultVrf.Routes.Route.Paths)}

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                        self.distance = YLeaf(YType.uint16, "distance")

                        self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                        self.route_type = YLeaf(YType.uint16, "route-type")

                        self.route_summary = YLeaf(YType.boolean, "route-summary")

                        self.route_tag = YLeaf(YType.uint16, "route-tag")

                        self.version = YLeaf(YType.uint8, "version")

                        self.attributes = YLeaf(YType.uint32, "attributes")

                        self.active = YLeaf(YType.boolean, "active")

                        self.path_origin = YLeaf(YType.enumeration, "path-origin")

                        self.hold_down = YLeaf(YType.boolean, "hold-down")

                        self.paths = YList(self)
                        self._segment_path = lambda: "route"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/%s" % self._segment_path()

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
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.metric = YLeaf(YType.uint16, "metric")

                            self.tag = YLeaf(YType.uint16, "tag")

                            self.interface = YLeaf(YType.str, "interface")

                            self.uptime = YLeaf(YType.uint32, "uptime")

                            self.is_permanent = YLeaf(YType.boolean, "is-permanent")
                            self._segment_path = lambda: "paths"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/routes/route/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active = YLeaf(YType.boolean, "active")

                    self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

                    self.rip_version = YLeaf(YType.int32, "rip-version")

                    self.default_metric = YLeaf(YType.uint8, "default-metric")

                    self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                    self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                    self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                    self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")
                    self._segment_path = lambda: "configuration"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.received_packets = YLeaf(YType.uint32, "received-packets")

                    self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                    self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                    self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

                    self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                    self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                    self.query_responses = YLeaf(YType.uint32, "query-responses")

                    self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                    self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                    self.rib_updates = YLeaf(YType.uint32, "rib-updates")
                    self._segment_path = lambda: "statistics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Rip.Protocol.DefaultVrf.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular RIP interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: if_handle
                    
                    	Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {"rip-summary" : ("rip_summary", Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary), "rip-peer" : ("rip_peer", Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.if_handle = YLeaf(YType.str, "if-handle")

                        self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                        self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                        self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                        self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                        self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                        self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                        self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                        self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.join_status = YLeaf(YType.boolean, "join-status")

                        self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                        self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                        self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                        self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                        self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                        self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                        self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                        self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                        self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                        self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                        self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                        self.rip_summary = YList(self)
                        self.rip_peer = YList(self)
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/interfaces/%s" % self._segment_path()

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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.metric = YLeaf(YType.int32, "metric")
                            self._segment_path = lambda: "rip-summary"

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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                            self.peer_address = YLeaf(YType.str, "peer-address")

                            self.peer_version = YLeaf(YType.uint8, "peer-version")

                            self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                            self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")
                            self._segment_path = lambda: "rip-peer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


            class Global_(Entity):
                """
                Global Information 
                
                .. attribute:: vrf_summary
                
                	VRF summary data
                	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.VrfSummary>`
                
                .. attribute:: interface_summary
                
                	List of Interfaces configured
                	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.Protocol.DefaultVrf.Global_.InterfaceSummary>`
                
                

                """

                _prefix = 'ip-rip-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rip.Protocol.DefaultVrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"vrf-summary" : ("vrf_summary", Rip.Protocol.DefaultVrf.Global_.VrfSummary)}
                    self._child_list_classes = {"interface-summary" : ("interface_summary", Rip.Protocol.DefaultVrf.Global_.InterfaceSummary)}

                    self.vrf_summary = Rip.Protocol.DefaultVrf.Global_.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"
                    self._children_yang_names.add("vrf-summary")

                    self.interface_summary = YList(self)
                    self._segment_path = lambda: "global"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.Protocol.DefaultVrf.Global_, [], name, value)


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
                        super(Rip.Protocol.DefaultVrf.Global_.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.active = YLeaf(YType.boolean, "active")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.route_count = YLeaf(YType.uint32, "route-count")

                        self.path_count = YLeaf(YType.uint32, "path-count")

                        self.update_timer = YLeaf(YType.uint32, "update-timer")

                        self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                        self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                        self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                        self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                        self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                        self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")
                        self._segment_path = lambda: "vrf-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Global_.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


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
                        super(Rip.Protocol.DefaultVrf.Global_.InterfaceSummary, self).__init__()

                        self.yang_name = "interface-summary"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                        self.send_version = YLeaf(YType.uint32, "send-version")

                        self.receive_version = YLeaf(YType.uint32, "receive-version")

                        self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")
                        self._segment_path = lambda: "interface-summary"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/protocol/default-vrf/global/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.Protocol.DefaultVrf.Global_.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)


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
        	**type**\:  :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_>`
        
        

        """

        _prefix = 'ip-rip-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rip.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "rip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"routes" : ("routes", Rip.DefaultVrf.Routes), "configuration" : ("configuration", Rip.DefaultVrf.Configuration), "statistics" : ("statistics", Rip.DefaultVrf.Statistics), "interfaces" : ("interfaces", Rip.DefaultVrf.Interfaces), "global" : ("global_", Rip.DefaultVrf.Global_)}
            self._child_list_classes = {}

            self.routes = Rip.DefaultVrf.Routes()
            self.routes.parent = self
            self._children_name_map["routes"] = "routes"
            self._children_yang_names.add("routes")

            self.configuration = Rip.DefaultVrf.Configuration()
            self.configuration.parent = self
            self._children_name_map["configuration"] = "configuration"
            self._children_yang_names.add("configuration")

            self.statistics = Rip.DefaultVrf.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

            self.interfaces = Rip.DefaultVrf.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.global_ = Rip.DefaultVrf.Global_()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._children_yang_names.add("global")
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/%s" % self._segment_path()


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
                self._child_container_classes = {}
                self._child_list_classes = {"route" : ("route", Rip.DefaultVrf.Routes.Route)}

                self.route = YList(self)
                self._segment_path = lambda: "routes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()

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
                    self._child_container_classes = {}
                    self._child_list_classes = {"paths" : ("paths", Rip.DefaultVrf.Routes.Route.Paths)}

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.prefix_length_xr = YLeaf(YType.uint32, "prefix-length-xr")

                    self.distance = YLeaf(YType.uint16, "distance")

                    self.bgp_count = YLeaf(YType.uint16, "bgp-count")

                    self.route_type = YLeaf(YType.uint16, "route-type")

                    self.route_summary = YLeaf(YType.boolean, "route-summary")

                    self.route_tag = YLeaf(YType.uint16, "route-tag")

                    self.version = YLeaf(YType.uint8, "version")

                    self.attributes = YLeaf(YType.uint32, "attributes")

                    self.active = YLeaf(YType.boolean, "active")

                    self.path_origin = YLeaf(YType.enumeration, "path-origin")

                    self.hold_down = YLeaf(YType.boolean, "hold-down")

                    self.paths = YList(self)
                    self._segment_path = lambda: "route"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/%s" % self._segment_path()

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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                        self.metric = YLeaf(YType.uint16, "metric")

                        self.tag = YLeaf(YType.uint16, "tag")

                        self.interface = YLeaf(YType.str, "interface")

                        self.uptime = YLeaf(YType.uint32, "uptime")

                        self.is_permanent = YLeaf(YType.boolean, "is-permanent")
                        self._segment_path = lambda: "paths"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/routes/route/%s" % self._segment_path()

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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.active = YLeaf(YType.boolean, "active")

                self.vr_fised_socket = YLeaf(YType.boolean, "vr-fised-socket")

                self.rip_version = YLeaf(YType.int32, "rip-version")

                self.default_metric = YLeaf(YType.uint8, "default-metric")

                self.maximum_paths = YLeaf(YType.uint8, "maximum-paths")

                self.auto_summarize = YLeaf(YType.boolean, "auto-summarize")

                self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                self.flash_threshold = YLeaf(YType.uint8, "flash-threshold")

                self.input_q_length = YLeaf(YType.uint16, "input-q-length")

                self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                self.validation_indicator = YLeaf(YType.boolean, "validation-indicator")

                self.update_timer = YLeaf(YType.uint32, "update-timer")

                self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                self.nsf_status = YLeaf(YType.boolean, "nsf-status")

                self.nsf_life_time = YLeaf(YType.uint32, "nsf-life-time")
                self._segment_path = lambda: "configuration"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()

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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.received_packets = YLeaf(YType.uint32, "received-packets")

                self.discarded_packets = YLeaf(YType.uint32, "discarded-packets")

                self.discarded_routes = YLeaf(YType.uint32, "discarded-routes")

                self.standby_packets_received = YLeaf(YType.uint32, "standby-packets-received")

                self.sent_messages = YLeaf(YType.uint32, "sent-messages")

                self.sent_message_failures = YLeaf(YType.uint32, "sent-message-failures")

                self.query_responses = YLeaf(YType.uint32, "query-responses")

                self.periodic_updates = YLeaf(YType.uint32, "periodic-updates")

                self.route_count = YLeaf(YType.uint32, "route-count")

                self.path_count = YLeaf(YType.uint32, "path-count")

                self.route_malloc_failures = YLeaf(YType.uint32, "route-malloc-failures")

                self.path_malloc_failures = YLeaf(YType.uint32, "path-malloc-failures")

                self.rib_updates = YLeaf(YType.uint32, "rib-updates")
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()

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
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Rip.DefaultVrf.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Interfaces, [], name, value)


            class Interface(Entity):
                """
                Information about a particular RIP interface
                
                .. attribute:: interface_name  <key>
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: interface
                
                	Interface name
                	**type**\: str
                
                .. attribute:: if_handle
                
                	Interface handle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {"rip-summary" : ("rip_summary", Rip.DefaultVrf.Interfaces.Interface.RipSummary), "rip-peer" : ("rip_peer", Rip.DefaultVrf.Interfaces.Interface.RipPeer)}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.interface = YLeaf(YType.str, "interface")

                    self.if_handle = YLeaf(YType.str, "if-handle")

                    self.rip_enabled = YLeaf(YType.boolean, "rip-enabled")

                    self.is_passive_interface = YLeaf(YType.boolean, "is-passive-interface")

                    self.multicast_address = YLeaf(YType.boolean, "multicast-address")

                    self.accept_metric = YLeaf(YType.boolean, "accept-metric")

                    self.send_version = YLeaf(YType.uint32, "send-version")

                    self.receive_version = YLeaf(YType.uint32, "receive-version")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.metric_cost = YLeaf(YType.uint32, "metric-cost")

                    self.split_horizon = YLeaf(YType.boolean, "split-horizon")

                    self.poison_horizon = YLeaf(YType.boolean, "poison-horizon")

                    self.triggered_rip = YLeaf(YType.boolean, "triggered-rip")

                    self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.join_status = YLeaf(YType.boolean, "join-status")

                    self.lpts_state = YLeaf(YType.boolean, "lpts-state")

                    self.auth_mode = YLeaf(YType.uint32, "auth-mode")

                    self.auth_keychain = YLeaf(YType.str, "auth-keychain")

                    self.send_auth_key_exists = YLeaf(YType.boolean, "send-auth-key-exists")

                    self.auth_key_md5 = YLeaf(YType.boolean, "auth-key-md5")

                    self.auth_key_send_id = YLeaf(YType.uint64, "auth-key-send-id")

                    self.total_pkt_recvd = YLeaf(YType.uint32, "total-pkt-recvd")

                    self.pkt_drop_wrong_kc = YLeaf(YType.uint32, "pkt-drop-wrong-kc")

                    self.pkt_drop_no_auth = YLeaf(YType.uint32, "pkt-drop-no-auth")

                    self.pkt_drop_invalid_auth = YLeaf(YType.uint32, "pkt-drop-invalid-auth")

                    self.pkt_accepted_valid_auth = YLeaf(YType.uint32, "pkt-accepted-valid-auth")

                    self.rip_summary = YList(self)
                    self.rip_peer = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/interfaces/%s" % self._segment_path()

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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                        self.metric = YLeaf(YType.int32, "metric")
                        self._segment_path = lambda: "rip-summary"

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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.peer_uptime = YLeaf(YType.uint32, "peer-uptime")

                        self.peer_address = YLeaf(YType.str, "peer-address")

                        self.peer_version = YLeaf(YType.uint8, "peer-version")

                        self.discarded_peer_packets = YLeaf(YType.uint32, "discarded-peer-packets")

                        self.discarded_peer_routes = YLeaf(YType.uint32, "discarded-peer-routes")
                        self._segment_path = lambda: "rip-peer"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Rip.DefaultVrf.Interfaces.Interface.RipPeer, ['peer_uptime', 'peer_address', 'peer_version', 'discarded_peer_packets', 'discarded_peer_routes'], name, value)


        class Global_(Entity):
            """
            Global Information 
            
            .. attribute:: vrf_summary
            
            	VRF summary data
            	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.VrfSummary>`
            
            .. attribute:: interface_summary
            
            	List of Interfaces configured
            	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper.Rip.DefaultVrf.Global_.InterfaceSummary>`
            
            

            """

            _prefix = 'ip-rip-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rip.DefaultVrf.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"vrf-summary" : ("vrf_summary", Rip.DefaultVrf.Global_.VrfSummary)}
                self._child_list_classes = {"interface-summary" : ("interface_summary", Rip.DefaultVrf.Global_.InterfaceSummary)}

                self.vrf_summary = Rip.DefaultVrf.Global_.VrfSummary()
                self.vrf_summary.parent = self
                self._children_name_map["vrf_summary"] = "vrf-summary"
                self._children_yang_names.add("vrf-summary")

                self.interface_summary = YList(self)
                self._segment_path = lambda: "global"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Rip.DefaultVrf.Global_, [], name, value)


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
                    super(Rip.DefaultVrf.Global_.VrfSummary, self).__init__()

                    self.yang_name = "vrf-summary"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.active = YLeaf(YType.boolean, "active")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.route_count = YLeaf(YType.uint32, "route-count")

                    self.path_count = YLeaf(YType.uint32, "path-count")

                    self.update_timer = YLeaf(YType.uint32, "update-timer")

                    self.next_update_time = YLeaf(YType.uint32, "next-update-time")

                    self.invalid_timer = YLeaf(YType.uint32, "invalid-timer")

                    self.hold_down_timer = YLeaf(YType.uint32, "hold-down-timer")

                    self.flush_timer = YLeaf(YType.uint32, "flush-timer")

                    self.interface_configured_count = YLeaf(YType.uint32, "interface-configured-count")

                    self.active_interface_count = YLeaf(YType.uint32, "active-interface-count")
                    self._segment_path = lambda: "vrf-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Global_.VrfSummary, ['vrf_name', 'active', 'oom_flags', 'route_count', 'path_count', 'update_timer', 'next_update_time', 'invalid_timer', 'hold_down_timer', 'flush_timer', 'interface_configured_count', 'active_interface_count'], name, value)


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
                    super(Rip.DefaultVrf.Global_.InterfaceSummary, self).__init__()

                    self.yang_name = "interface-summary"
                    self.yang_parent_name = "global"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                    self.oom_flags = YLeaf(YType.uint32, "oom-flags")

                    self.send_version = YLeaf(YType.uint32, "send-version")

                    self.receive_version = YLeaf(YType.uint32, "receive-version")

                    self.neighbor_count = YLeaf(YType.uint32, "neighbor-count")
                    self._segment_path = lambda: "interface-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-rip-oper:rip/default-vrf/global/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Rip.DefaultVrf.Global_.InterfaceSummary, ['interface_name', 'enabled', 'state', 'destination_address', 'prefix_length', 'oom_flags', 'send_version', 'receive_version', 'neighbor_count'], name, value)

    def clone_ptr(self):
        self._top_entity = Rip()
        return self._top_entity

