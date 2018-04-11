""" openconfig_bgp 

This module describes a YANG model for BGP protocol
configuration.It is a limited subset of all of the configuration
parameters available in the variety of vendor implementations,
hence it is expected that it would be augmented with vendor\-
specific configuration data as needed. Additional modules or
submodules to handle other aspects of BGP configuration,
including policy, VRFs, VPNs, and additional address families
are also expected.
This model supports the following BGP configuration level
hierarchy\:
 BGP
   \|
   +\-> [ global BGP configuration ]
     +\-> AFI / SAFI global
   +\-> peer group
     +\-> [ peer group config ]
     +\-> AFI / SAFI [ per\-AFI overrides ]
   +\-> neighbor
     +\-> [ neighbor config ]
     +\-> [ optional pointer to peer\-group ]
     +\-> AFI / SAFI [ per\-AFI overrides ]

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Bgp(Entity):
    """
    Top\-level configuration and state for the BGP router
    
    .. attribute:: global_
    
    	Global configuration for the BGP router
    	**type**\:  :py:class:`Global <ydk.models.openconfig.openconfig_bgp.Bgp.Global>`
    
    .. attribute:: neighbors
    
    	Configuration for BGP neighbors
    	**type**\:  :py:class:`Neighbors <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors>`
    
    .. attribute:: peer_groups
    
    	Configuration for BGP peer\-groups
    	**type**\:  :py:class:`PeerGroups <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups>`
    
    

    """

    _prefix = 'oc-bgp'
    _revision = '2016-06-21'

    def __init__(self):
        super(Bgp, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp"
        self.yang_parent_name = "openconfig-bgp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("global", ("global_", Bgp.Global)), ("neighbors", ("neighbors", Bgp.Neighbors)), ("peer-groups", ("peer_groups", Bgp.PeerGroups))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.global_ = Bgp.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.neighbors = Bgp.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")

        self.peer_groups = Bgp.PeerGroups()
        self.peer_groups.parent = self
        self._children_name_map["peer_groups"] = "peer-groups"
        self._children_yang_names.add("peer-groups")
        self._segment_path = lambda: "openconfig-bgp:bgp"


    class Global(Entity):
        """
        Global configuration for the BGP router
        
        .. attribute:: config
        
        	Configuration parameters relating to the global BGP router
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.Config>`
        
        .. attribute:: state
        
        	State information relating to the global BGP router
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.State>`
        
        .. attribute:: default_route_distance
        
        	Administrative distance (or preference) assigned to routes received from different sources (external, internal, and local)
        	**type**\:  :py:class:`DefaultRouteDistance <ydk.models.openconfig.openconfig_bgp.Bgp.Global.DefaultRouteDistance>`
        
        .. attribute:: confederation
        
        	Parameters indicating whether the local system acts as part of a BGP confederation
        	**type**\:  :py:class:`Confederation <ydk.models.openconfig.openconfig_bgp.Bgp.Global.Confederation>`
        
        .. attribute:: graceful_restart
        
        	Parameters relating the graceful restart mechanism for BGP
        	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.Global.GracefulRestart>`
        
        .. attribute:: use_multiple_paths
        
        	Parameters related to the use of multiple paths for the same NLRI
        	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths>`
        
        .. attribute:: route_selection_options
        
        	Parameters relating to options for route selection
        	**type**\:  :py:class:`RouteSelectionOptions <ydk.models.openconfig.openconfig_bgp.Bgp.Global.RouteSelectionOptions>`
        
        .. attribute:: afi_safis
        
        	Address family specific configuration
        	**type**\:  :py:class:`AfiSafis <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis>`
        
        .. attribute:: apply_policy
        
        	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
        	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.Global.ApplyPolicy>`
        
        

        """

        _prefix = 'oc-bgp'
        _revision = '2016-06-21'

        def __init__(self):
            super(Bgp.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "bgp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.Config)), ("state", ("state", Bgp.Global.State)), ("default-route-distance", ("default_route_distance", Bgp.Global.DefaultRouteDistance)), ("confederation", ("confederation", Bgp.Global.Confederation)), ("graceful-restart", ("graceful_restart", Bgp.Global.GracefulRestart)), ("use-multiple-paths", ("use_multiple_paths", Bgp.Global.UseMultiplePaths)), ("route-selection-options", ("route_selection_options", Bgp.Global.RouteSelectionOptions)), ("afi-safis", ("afi_safis", Bgp.Global.AfiSafis)), ("apply-policy", ("apply_policy", Bgp.Global.ApplyPolicy))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.config = Bgp.Global.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.state = Bgp.Global.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")

            self.default_route_distance = Bgp.Global.DefaultRouteDistance()
            self.default_route_distance.parent = self
            self._children_name_map["default_route_distance"] = "default-route-distance"
            self._children_yang_names.add("default-route-distance")

            self.confederation = Bgp.Global.Confederation()
            self.confederation.parent = self
            self._children_name_map["confederation"] = "confederation"
            self._children_yang_names.add("confederation")

            self.graceful_restart = Bgp.Global.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.use_multiple_paths = Bgp.Global.UseMultiplePaths()
            self.use_multiple_paths.parent = self
            self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
            self._children_yang_names.add("use-multiple-paths")

            self.route_selection_options = Bgp.Global.RouteSelectionOptions()
            self.route_selection_options.parent = self
            self._children_name_map["route_selection_options"] = "route-selection-options"
            self._children_yang_names.add("route-selection-options")

            self.afi_safis = Bgp.Global.AfiSafis()
            self.afi_safis.parent = self
            self._children_name_map["afi_safis"] = "afi-safis"
            self._children_yang_names.add("afi-safis")

            self.apply_policy = Bgp.Global.ApplyPolicy()
            self.apply_policy.parent = self
            self._children_name_map["apply_policy"] = "apply-policy"
            self._children_yang_names.add("apply-policy")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "openconfig-bgp:bgp/%s" % self._segment_path()


        class Config(Entity):
            """
            Configuration parameters relating to the global BGP router
            
            .. attribute:: as_
            
            	Local autonomous system number of the router.  Uses the 32\-bit as\-number type from the model in RFC 6991
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: router_id
            
            	Router id of the router \- an unsigned 32\-bit integer expressed in dotted quad notation
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('as_', YLeaf(YType.uint32, 'as')),
                    ('router_id', YLeaf(YType.str, 'router-id')),
                ])
                self.as_ = None
                self.router_id = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bgp.Global.Config, ['as_', 'router_id'], name, value)


        class State(Entity):
            """
            State information relating to the global BGP router
            
            .. attribute:: as_
            
            	Local autonomous system number of the router.  Uses the 32\-bit as\-number type from the model in RFC 6991
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: router_id
            
            	Router id of the router \- an unsigned 32\-bit integer expressed in dotted quad notation
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
            
            .. attribute:: total_paths
            
            	Total number of BGP paths within the context
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_prefixes
            
            	Total number of BGP prefixes received within the context
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('as_', YLeaf(YType.uint32, 'as')),
                    ('router_id', YLeaf(YType.str, 'router-id')),
                    ('total_paths', YLeaf(YType.uint32, 'total-paths')),
                    ('total_prefixes', YLeaf(YType.uint32, 'total-prefixes')),
                ])
                self.as_ = None
                self.router_id = None
                self.total_paths = None
                self.total_prefixes = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bgp.Global.State, ['as_', 'router_id', 'total_paths', 'total_prefixes'], name, value)


        class DefaultRouteDistance(Entity):
            """
            Administrative distance (or preference) assigned to
            routes received from different sources
            (external, internal, and local).
            
            .. attribute:: config
            
            	Configuration parameters relating to the default route distance
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.DefaultRouteDistance.Config>`
            
            .. attribute:: state
            
            	State information relating to the default route distance
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.DefaultRouteDistance.State>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.DefaultRouteDistance, self).__init__()

                self.yang_name = "default-route-distance"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.DefaultRouteDistance.Config)), ("state", ("state", Bgp.Global.DefaultRouteDistance.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.DefaultRouteDistance.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.DefaultRouteDistance.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "default-route-distance"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters relating to the default route
                distance
                
                .. attribute:: external_route_distance
                
                	Administrative distance for routes learned from external BGP (eBGP)
                	**type**\: int
                
                	**range:** 1..255
                
                .. attribute:: internal_route_distance
                
                	Administrative distance for routes learned from internal BGP (iBGP)
                	**type**\: int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.DefaultRouteDistance.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "default-route-distance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('external_route_distance', YLeaf(YType.uint8, 'external-route-distance')),
                        ('internal_route_distance', YLeaf(YType.uint8, 'internal-route-distance')),
                    ])
                    self.external_route_distance = None
                    self.internal_route_distance = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/default-route-distance/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.DefaultRouteDistance.Config, ['external_route_distance', 'internal_route_distance'], name, value)


            class State(Entity):
                """
                State information relating to the default route distance
                
                .. attribute:: external_route_distance
                
                	Administrative distance for routes learned from external BGP (eBGP)
                	**type**\: int
                
                	**range:** 1..255
                
                .. attribute:: internal_route_distance
                
                	Administrative distance for routes learned from internal BGP (iBGP)
                	**type**\: int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.DefaultRouteDistance.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "default-route-distance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('external_route_distance', YLeaf(YType.uint8, 'external-route-distance')),
                        ('internal_route_distance', YLeaf(YType.uint8, 'internal-route-distance')),
                    ])
                    self.external_route_distance = None
                    self.internal_route_distance = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/default-route-distance/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.DefaultRouteDistance.State, ['external_route_distance', 'internal_route_distance'], name, value)


        class Confederation(Entity):
            """
            Parameters indicating whether the local system acts as part
            of a BGP confederation
            
            .. attribute:: config
            
            	Configuration parameters relating to BGP confederations
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.Confederation.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP confederations
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.Confederation.State>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.Confederation, self).__init__()

                self.yang_name = "confederation"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.Confederation.Config)), ("state", ("state", Bgp.Global.Confederation.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.Confederation.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.Confederation.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "confederation"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters relating to BGP confederations
                
                .. attribute:: enabled
                
                	When this leaf is set to true it indicates that the local\-AS is part of a BGP confederation
                	**type**\: bool
                
                .. attribute:: identifier
                
                	Confederation identifier for the autonomous system
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: member_as
                
                	Remote autonomous systems that are to be treated as part of the local confederation
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.Confederation.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "confederation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('identifier', YLeaf(YType.uint32, 'identifier')),
                        ('member_as', YLeafList(YType.uint32, 'member-as')),
                    ])
                    self.enabled = None
                    self.identifier = None
                    self.member_as = []
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/confederation/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.Confederation.Config, ['enabled', 'identifier', 'member_as'], name, value)


            class State(Entity):
                """
                State information relating to the BGP confederations
                
                .. attribute:: enabled
                
                	When this leaf is set to true it indicates that the local\-AS is part of a BGP confederation
                	**type**\: bool
                
                .. attribute:: identifier
                
                	Confederation identifier for the autonomous system
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: member_as
                
                	Remote autonomous systems that are to be treated as part of the local confederation
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.Confederation.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "confederation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('identifier', YLeaf(YType.uint32, 'identifier')),
                        ('member_as', YLeafList(YType.uint32, 'member-as')),
                    ])
                    self.enabled = None
                    self.identifier = None
                    self.member_as = []
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/confederation/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.Confederation.State, ['enabled', 'identifier', 'member_as'], name, value)


        class GracefulRestart(Entity):
            """
            Parameters relating the graceful restart mechanism for BGP
            
            .. attribute:: config
            
            	Configuration parameters relating to graceful\-restart
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.GracefulRestart.Config>`
            
            .. attribute:: state
            
            	State information associated with graceful\-restart
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.GracefulRestart.State>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.GracefulRestart.Config)), ("state", ("state", Bgp.Global.GracefulRestart.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.GracefulRestart.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.GracefulRestart.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "graceful-restart"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters relating to graceful\-restart
                
                .. attribute:: enabled
                
                	Enable or disable the graceful\-restart capability
                	**type**\: bool
                
                .. attribute:: restart_time
                
                	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                	**type**\: int
                
                	**range:** 0..4096
                
                .. attribute:: stale_routes_time
                
                	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: helper_only
                
                	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                	**type**\: bool
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.GracefulRestart.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "graceful-restart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                        ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                        ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                    ])
                    self.enabled = None
                    self.restart_time = None
                    self.stale_routes_time = None
                    self.helper_only = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/graceful-restart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.GracefulRestart.Config, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only'], name, value)


            class State(Entity):
                """
                State information associated with graceful\-restart
                
                .. attribute:: enabled
                
                	Enable or disable the graceful\-restart capability
                	**type**\: bool
                
                .. attribute:: restart_time
                
                	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                	**type**\: int
                
                	**range:** 0..4096
                
                .. attribute:: stale_routes_time
                
                	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: helper_only
                
                	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                	**type**\: bool
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.GracefulRestart.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "graceful-restart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                        ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                        ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                    ])
                    self.enabled = None
                    self.restart_time = None
                    self.stale_routes_time = None
                    self.helper_only = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/graceful-restart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.GracefulRestart.State, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only'], name, value)


        class UseMultiplePaths(Entity):
            """
            Parameters related to the use of multiple paths for the
            same NLRI
            
            .. attribute:: config
            
            	Configuration parameters relating to multipath
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Config>`
            
            .. attribute:: state
            
            	State parameters relating to multipath
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.State>`
            
            .. attribute:: ebgp
            
            	Multipath parameters for eBGP
            	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ebgp>`
            
            .. attribute:: ibgp
            
            	Multipath parameters for iBGP
            	**type**\:  :py:class:`Ibgp <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ibgp>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.UseMultiplePaths, self).__init__()

                self.yang_name = "use-multiple-paths"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.UseMultiplePaths.Config)), ("state", ("state", Bgp.Global.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.Global.UseMultiplePaths.Ebgp)), ("ibgp", ("ibgp", Bgp.Global.UseMultiplePaths.Ibgp))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.UseMultiplePaths.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.UseMultiplePaths.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.ebgp = Bgp.Global.UseMultiplePaths.Ebgp()
                self.ebgp.parent = self
                self._children_name_map["ebgp"] = "ebgp"
                self._children_yang_names.add("ebgp")

                self.ibgp = Bgp.Global.UseMultiplePaths.Ibgp()
                self.ibgp.parent = self
                self._children_name_map["ibgp"] = "ibgp"
                self._children_yang_names.add("ibgp")
                self._segment_path = lambda: "use-multiple-paths"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters relating to multipath
                
                .. attribute:: enabled
                
                	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.UseMultiplePaths.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "use-multiple-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                    ])
                    self.enabled = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.UseMultiplePaths.Config, ['enabled'], name, value)


            class State(Entity):
                """
                State parameters relating to multipath
                
                .. attribute:: enabled
                
                	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.UseMultiplePaths.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "use-multiple-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                    ])
                    self.enabled = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.UseMultiplePaths.State, ['enabled'], name, value)


            class Ebgp(Entity):
                """
                Multipath parameters for eBGP
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multipath
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ebgp.Config>`
                
                .. attribute:: state
                
                	State information relating to eBGP multipath
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ebgp.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.UseMultiplePaths.Ebgp, self).__init__()

                    self.yang_name = "ebgp"
                    self.yang_parent_name = "use-multiple-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.Global.UseMultiplePaths.Ebgp.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Global.UseMultiplePaths.Ebgp.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Global.UseMultiplePaths.Ebgp.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ebgp"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/%s" % self._segment_path()


                class Config(Entity):
                    """
                    Configuration parameters relating to eBGP multipath
                    
                    .. attribute:: allow_multiple_as
                    
                    	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.UseMultiplePaths.Ebgp.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ebgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                            ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                        ])
                        self.allow_multiple_as = None
                        self.maximum_paths = None
                        self._segment_path = lambda: "config"
                        self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/ebgp/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as', 'maximum_paths'], name, value)


                class State(Entity):
                    """
                    State information relating to eBGP multipath
                    
                    .. attribute:: allow_multiple_as
                    
                    	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.UseMultiplePaths.Ebgp.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ebgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                            ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                        ])
                        self.allow_multiple_as = None
                        self.maximum_paths = None
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/ebgp/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.UseMultiplePaths.Ebgp.State, ['allow_multiple_as', 'maximum_paths'], name, value)


            class Ibgp(Entity):
                """
                Multipath parameters for iBGP
                
                .. attribute:: config
                
                	Configuration parameters relating to iBGP multipath
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ibgp.Config>`
                
                .. attribute:: state
                
                	State information relating to iBGP multipath
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.UseMultiplePaths.Ibgp.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.UseMultiplePaths.Ibgp, self).__init__()

                    self.yang_name = "ibgp"
                    self.yang_parent_name = "use-multiple-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.UseMultiplePaths.Ibgp.Config)), ("state", ("state", Bgp.Global.UseMultiplePaths.Ibgp.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Global.UseMultiplePaths.Ibgp.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Global.UseMultiplePaths.Ibgp.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ibgp"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/%s" % self._segment_path()


                class Config(Entity):
                    """
                    Configuration parameters relating to iBGP multipath
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.UseMultiplePaths.Ibgp.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ibgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                        ])
                        self.maximum_paths = None
                        self._segment_path = lambda: "config"
                        self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/ibgp/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.UseMultiplePaths.Ibgp.Config, ['maximum_paths'], name, value)


                class State(Entity):
                    """
                    State information relating to iBGP multipath
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.UseMultiplePaths.Ibgp.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ibgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                        ])
                        self.maximum_paths = None
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-bgp:bgp/global/use-multiple-paths/ibgp/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.UseMultiplePaths.Ibgp.State, ['maximum_paths'], name, value)


        class RouteSelectionOptions(Entity):
            """
            Parameters relating to options for route selection
            
            .. attribute:: config
            
            	Configuration parameters relating to route selection options
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.RouteSelectionOptions.Config>`
            
            .. attribute:: state
            
            	State information for the route selection options
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.RouteSelectionOptions.State>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.RouteSelectionOptions, self).__init__()

                self.yang_name = "route-selection-options"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.RouteSelectionOptions.Config)), ("state", ("state", Bgp.Global.RouteSelectionOptions.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.RouteSelectionOptions.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.RouteSelectionOptions.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "route-selection-options"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters relating to route selection
                options
                
                .. attribute:: always_compare_med
                
                	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: ignore_as_path_length
                
                	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: external_compare_router_id
                
                	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: advertise_inactive_routes
                
                	Advertise inactive routes to external peers.  The default is to only advertise active routes
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: enable_aigp
                
                	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: ignore_next_hop_igp_metric
                
                	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.RouteSelectionOptions.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "route-selection-options"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                        ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                        ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                        ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                        ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                        ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                    ])
                    self.always_compare_med = None
                    self.ignore_as_path_length = None
                    self.external_compare_router_id = None
                    self.advertise_inactive_routes = None
                    self.enable_aigp = None
                    self.ignore_next_hop_igp_metric = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/route-selection-options/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.RouteSelectionOptions.Config, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


            class State(Entity):
                """
                State information for the route selection options
                
                .. attribute:: always_compare_med
                
                	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: ignore_as_path_length
                
                	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: external_compare_router_id
                
                	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: advertise_inactive_routes
                
                	Advertise inactive routes to external peers.  The default is to only advertise active routes
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: enable_aigp
                
                	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: ignore_next_hop_igp_metric
                
                	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.RouteSelectionOptions.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "route-selection-options"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                        ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                        ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                        ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                        ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                        ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                    ])
                    self.always_compare_med = None
                    self.ignore_as_path_length = None
                    self.external_compare_router_id = None
                    self.advertise_inactive_routes = None
                    self.enable_aigp = None
                    self.ignore_next_hop_igp_metric = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/route-selection-options/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.RouteSelectionOptions.State, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


        class AfiSafis(Entity):
            """
            Address family specific configuration
            
            .. attribute:: afi_safi
            
            	AFI,SAFI configuration available for the neighbour or group
            	**type**\: list of  		 :py:class:`AfiSafi <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.AfiSafis, self).__init__()

                self.yang_name = "afi-safis"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("afi-safi", ("afi_safi", Bgp.Global.AfiSafis.AfiSafi))])
                self._leafs = OrderedDict()

                self.afi_safi = YList(self)
                self._segment_path = lambda: "afi-safis"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bgp.Global.AfiSafis, [], name, value)


            class AfiSafi(Entity):
                """
                AFI,SAFI configuration available for the
                neighbour or group
                
                .. attribute:: afi_safi_name  (key)
                
                	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                
                .. attribute:: config
                
                	Configuration parameters for the AFI\-SAFI
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Config>`
                
                .. attribute:: state
                
                	State information relating to the AFI\-SAFI
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.State>`
                
                .. attribute:: graceful_restart
                
                	Parameters relating to BGP graceful\-restart
                	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart>`
                
                .. attribute:: route_selection_options
                
                	Parameters relating to options for route selection
                	**type**\:  :py:class:`RouteSelectionOptions <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions>`
                
                .. attribute:: use_multiple_paths
                
                	Parameters related to the use of multiple paths for the same NLRI
                	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths>`
                
                .. attribute:: apply_policy
                
                	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy>`
                
                .. attribute:: ipv4_unicast
                
                	IPv4 unicast configuration options
                	**type**\:  :py:class:`Ipv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast>`
                
                .. attribute:: ipv6_unicast
                
                	IPv6 unicast configuration options
                	**type**\:  :py:class:`Ipv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast>`
                
                .. attribute:: ipv4_labeled_unicast
                
                	IPv4 Labeled Unicast configuration options
                	**type**\:  :py:class:`Ipv4LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast>`
                
                .. attribute:: ipv6_labeled_unicast
                
                	IPv6 Labeled Unicast configuration options
                	**type**\:  :py:class:`Ipv6LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast>`
                
                .. attribute:: l3vpn_ipv4_unicast
                
                	Unicast IPv4 L3VPN configuration options
                	**type**\:  :py:class:`L3VpnIpv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                
                .. attribute:: l3vpn_ipv6_unicast
                
                	Unicast IPv6 L3VPN configuration options
                	**type**\:  :py:class:`L3VpnIpv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                
                .. attribute:: l3vpn_ipv4_multicast
                
                	Multicast IPv4 L3VPN configuration options
                	**type**\:  :py:class:`L3VpnIpv4Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                
                .. attribute:: l3vpn_ipv6_multicast
                
                	Multicast IPv6 L3VPN configuration options
                	**type**\:  :py:class:`L3VpnIpv6Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                
                .. attribute:: l2vpn_vpls
                
                	BGP\-signalled VPLS configuration options
                	**type**\:  :py:class:`L2VpnVpls <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls>`
                
                .. attribute:: l2vpn_evpn
                
                	BGP EVPN configuration options
                	**type**\:  :py:class:`L2VpnEvpn <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.AfiSafis.AfiSafi, self).__init__()

                    self.yang_name = "afi-safi"
                    self.yang_parent_name = "afi-safis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['afi_safi_name']
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.State)), ("graceful-restart", ("graceful_restart", Bgp.Global.AfiSafis.AfiSafi.GracefulRestart)), ("route-selection-options", ("route_selection_options", Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions)), ("use-multiple-paths", ("use_multiple_paths", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths)), ("apply-policy", ("apply_policy", Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy)), ("ipv4-unicast", ("ipv4_unicast", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast)), ("ipv6-unicast", ("ipv6_unicast", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast)), ("ipv4-labeled-unicast", ("ipv4_labeled_unicast", Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast)), ("ipv6-labeled-unicast", ("ipv6_labeled_unicast", Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast)), ("l3vpn-ipv4-unicast", ("l3vpn_ipv4_unicast", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast)), ("l3vpn-ipv6-unicast", ("l3vpn_ipv6_unicast", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast)), ("l3vpn-ipv4-multicast", ("l3vpn_ipv4_multicast", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast)), ("l3vpn-ipv6-multicast", ("l3vpn_ipv6_multicast", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast)), ("l2vpn-vpls", ("l2vpn_vpls", Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls)), ("l2vpn-evpn", ("l2vpn_evpn", Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                    ])
                    self.afi_safi_name = None

                    self.config = Bgp.Global.AfiSafis.AfiSafi.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Global.AfiSafis.AfiSafi.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.graceful_restart = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"
                    self._children_yang_names.add("graceful-restart")

                    self.route_selection_options = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions()
                    self.route_selection_options.parent = self
                    self._children_name_map["route_selection_options"] = "route-selection-options"
                    self._children_yang_names.add("route-selection-options")

                    self.use_multiple_paths = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths()
                    self.use_multiple_paths.parent = self
                    self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
                    self._children_yang_names.add("use-multiple-paths")

                    self.apply_policy = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy()
                    self.apply_policy.parent = self
                    self._children_name_map["apply_policy"] = "apply-policy"
                    self._children_yang_names.add("apply-policy")

                    self.ipv4_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast()
                    self.ipv4_unicast.parent = self
                    self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                    self._children_yang_names.add("ipv4-unicast")

                    self.ipv6_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast()
                    self.ipv6_unicast.parent = self
                    self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                    self._children_yang_names.add("ipv6-unicast")

                    self.ipv4_labeled_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast()
                    self.ipv4_labeled_unicast.parent = self
                    self._children_name_map["ipv4_labeled_unicast"] = "ipv4-labeled-unicast"
                    self._children_yang_names.add("ipv4-labeled-unicast")

                    self.ipv6_labeled_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast()
                    self.ipv6_labeled_unicast.parent = self
                    self._children_name_map["ipv6_labeled_unicast"] = "ipv6-labeled-unicast"
                    self._children_yang_names.add("ipv6-labeled-unicast")

                    self.l3vpn_ipv4_unicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                    self.l3vpn_ipv4_unicast.parent = self
                    self._children_name_map["l3vpn_ipv4_unicast"] = "l3vpn-ipv4-unicast"
                    self._children_yang_names.add("l3vpn-ipv4-unicast")

                    self.l3vpn_ipv6_unicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                    self.l3vpn_ipv6_unicast.parent = self
                    self._children_name_map["l3vpn_ipv6_unicast"] = "l3vpn-ipv6-unicast"
                    self._children_yang_names.add("l3vpn-ipv6-unicast")

                    self.l3vpn_ipv4_multicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                    self.l3vpn_ipv4_multicast.parent = self
                    self._children_name_map["l3vpn_ipv4_multicast"] = "l3vpn-ipv4-multicast"
                    self._children_yang_names.add("l3vpn-ipv4-multicast")

                    self.l3vpn_ipv6_multicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                    self.l3vpn_ipv6_multicast.parent = self
                    self._children_name_map["l3vpn_ipv6_multicast"] = "l3vpn-ipv6-multicast"
                    self._children_yang_names.add("l3vpn-ipv6-multicast")

                    self.l2vpn_vpls = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls()
                    self.l2vpn_vpls.parent = self
                    self._children_name_map["l2vpn_vpls"] = "l2vpn-vpls"
                    self._children_yang_names.add("l2vpn-vpls")

                    self.l2vpn_evpn = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn()
                    self.l2vpn_evpn.parent = self
                    self._children_name_map["l2vpn_evpn"] = "l2vpn-evpn"
                    self._children_yang_names.add("l2vpn-evpn")
                    self._segment_path = lambda: "afi-safi" + "[afi-safi-name='" + str(self.afi_safi_name) + "']"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/afi-safis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi, ['afi_safi_name'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters for the AFI\-SAFI
                    
                    .. attribute:: afi_safi_name
                    
                    	AFI,SAFI
                    	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                    
                    .. attribute:: enabled
                    
                    	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ])
                        self.afi_safi_name = None
                        self.enabled = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Config, ['afi_safi_name', 'enabled'], name, value)


                class State(Entity):
                    """
                    State information relating to the AFI\-SAFI
                    
                    .. attribute:: afi_safi_name
                    
                    	AFI,SAFI
                    	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                    
                    .. attribute:: enabled
                    
                    	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: total_paths
                    
                    	Total number of BGP paths within the context
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_prefixes
                    
                    	Total number of BGP prefixes received within the context
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('total_paths', YLeaf(YType.uint32, 'total-paths')),
                            ('total_prefixes', YLeaf(YType.uint32, 'total-prefixes')),
                        ])
                        self.afi_safi_name = None
                        self.enabled = None
                        self.total_paths = None
                        self.total_prefixes = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.State, ['afi_safi_name', 'enabled', 'total_paths', 'total_prefixes'], name, value)


                class GracefulRestart(Entity):
                    """
                    Parameters relating to BGP graceful\-restart
                    
                    .. attribute:: config
                    
                    	Configuration options for BGP graceful\-restart
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config>`
                    
                    .. attribute:: state
                    
                    	State information for BGP graceful\-restart
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.GracefulRestart, self).__init__()

                        self.yang_name = "graceful-restart"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "graceful-restart"


                    class Config(Entity):
                        """
                        Configuration options for BGP graceful\-restart
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.enabled = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config, ['enabled'], name, value)


                    class State(Entity):
                        """
                        State information for BGP graceful\-restart
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.enabled = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State, ['enabled'], name, value)


                class RouteSelectionOptions(Entity):
                    """
                    Parameters relating to options for route selection
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to route selection options
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config>`
                    
                    .. attribute:: state
                    
                    	State information for the route selection options
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions, self).__init__()

                        self.yang_name = "route-selection-options"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "route-selection-options"


                    class Config(Entity):
                        """
                        Configuration parameters relating to route selection
                        options
                        
                        .. attribute:: always_compare_med
                        
                        	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: ignore_as_path_length
                        
                        	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: external_compare_router_id
                        
                        	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: advertise_inactive_routes
                        
                        	Advertise inactive routes to external peers.  The default is to only advertise active routes
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: enable_aigp
                        
                        	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: ignore_next_hop_igp_metric
                        
                        	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "route-selection-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                                ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                                ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                                ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                                ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                                ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                            ])
                            self.always_compare_med = None
                            self.ignore_as_path_length = None
                            self.external_compare_router_id = None
                            self.advertise_inactive_routes = None
                            self.enable_aigp = None
                            self.ignore_next_hop_igp_metric = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


                    class State(Entity):
                        """
                        State information for the route selection options
                        
                        .. attribute:: always_compare_med
                        
                        	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: ignore_as_path_length
                        
                        	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: external_compare_router_id
                        
                        	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: advertise_inactive_routes
                        
                        	Advertise inactive routes to external peers.  The default is to only advertise active routes
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: enable_aigp
                        
                        	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: ignore_next_hop_igp_metric
                        
                        	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "route-selection-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                                ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                                ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                                ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                                ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                                ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                            ])
                            self.always_compare_med = None
                            self.ignore_as_path_length = None
                            self.external_compare_router_id = None
                            self.advertise_inactive_routes = None
                            self.enable_aigp = None
                            self.ignore_next_hop_igp_metric = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


                class UseMultiplePaths(Entity):
                    """
                    Parameters related to the use of multiple paths for the
                    same NLRI
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to multipath
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to multipath
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                    
                    .. attribute:: ebgp
                    
                    	Multipath parameters for eBGP
                    	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                    
                    .. attribute:: ibgp
                    
                    	Multipath parameters for iBGP
                    	**type**\:  :py:class:`Ibgp <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths, self).__init__()

                        self.yang_name = "use-multiple-paths"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp)), ("ibgp", ("ibgp", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.ebgp = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                        self.ebgp.parent = self
                        self._children_name_map["ebgp"] = "ebgp"
                        self._children_yang_names.add("ebgp")

                        self.ibgp = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp()
                        self.ibgp.parent = self
                        self._children_name_map["ibgp"] = "ibgp"
                        self._children_yang_names.add("ibgp")
                        self._segment_path = lambda: "use-multiple-paths"


                    class Config(Entity):
                        """
                        Configuration parameters relating to multipath
                        
                        .. attribute:: enabled
                        
                        	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "use-multiple-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.enabled = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config, ['enabled'], name, value)


                    class State(Entity):
                        """
                        State parameters relating to multipath
                        
                        .. attribute:: enabled
                        
                        	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "use-multiple-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.enabled = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State, ['enabled'], name, value)


                    class Ebgp(Entity):
                        """
                        Multipath parameters for eBGP
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to eBGP multipath
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to eBGP multipath
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp, self).__init__()

                            self.yang_name = "ebgp"
                            self.yang_parent_name = "use-multiple-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ebgp"


                        class Config(Entity):
                            """
                            Configuration parameters relating to eBGP multipath
                            
                            .. attribute:: allow_multiple_as
                            
                            	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ebgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                    ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                ])
                                self.allow_multiple_as = None
                                self.maximum_paths = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as', 'maximum_paths'], name, value)


                        class State(Entity):
                            """
                            State information relating to eBGP multipath
                            
                            .. attribute:: allow_multiple_as
                            
                            	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ebgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                    ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                ])
                                self.allow_multiple_as = None
                                self.maximum_paths = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, ['allow_multiple_as', 'maximum_paths'], name, value)


                    class Ibgp(Entity):
                        """
                        Multipath parameters for iBGP
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to iBGP multipath
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to iBGP multipath
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp, self).__init__()

                            self.yang_name = "ibgp"
                            self.yang_parent_name = "use-multiple-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ibgp"


                        class Config(Entity):
                            """
                            Configuration parameters relating to iBGP multipath
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ibgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                ])
                                self.maximum_paths = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config, ['maximum_paths'], name, value)


                        class State(Entity):
                            """
                            State information relating to iBGP multipath
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ibgp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                ])
                                self.maximum_paths = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State, ['maximum_paths'], name, value)


                class ApplyPolicy(Entity):
                    """
                    Anchor point for routing policies in the model.
                    Import and export policies are with respect to the local
                    routing table, i.e., export (send) and import (receive),
                    depending on the context.
                    
                    .. attribute:: config
                    
                    	Policy configuration data
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state for routing policy
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy, self).__init__()

                        self.yang_name = "apply-policy"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "apply-policy"


                    class Config(Entity):
                        """
                        Policy configuration data.
                        
                        .. attribute:: import_policy
                        
                        	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                        
                        .. attribute:: default_import_policy
                        
                        	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                        	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                        
                        	**default value**\: REJECT_ROUTE
                        
                        .. attribute:: export_policy
                        
                        	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                        
                        .. attribute:: default_export_policy
                        
                        	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                        	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                        
                        	**default value**\: REJECT_ROUTE
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "apply-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('import_policy', YLeafList(YType.str, 'import-policy')),
                                ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                ('export_policy', YLeafList(YType.str, 'export-policy')),
                                ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                            ])
                            self.import_policy = []
                            self.default_import_policy = None
                            self.export_policy = []
                            self.default_export_policy = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                    class State(Entity):
                        """
                        Operational state for routing policy
                        
                        .. attribute:: import_policy
                        
                        	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                        
                        .. attribute:: default_import_policy
                        
                        	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                        	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                        
                        	**default value**\: REJECT_ROUTE
                        
                        .. attribute:: export_policy
                        
                        	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                        
                        .. attribute:: default_export_policy
                        
                        	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                        	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                        
                        	**default value**\: REJECT_ROUTE
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "apply-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('import_policy', YLeafList(YType.str, 'import-policy')),
                                ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                ('export_policy', YLeafList(YType.str, 'export-policy')),
                                ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                            ])
                            self.import_policy = []
                            self.default_import_policy = None
                            self.export_policy = []
                            self.default_export_policy = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                class Ipv4Unicast(Entity):
                    """
                    IPv4 unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                    
                    .. attribute:: state
                    
                    	State information for common IPv4 and IPv6 unicast parameters
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast, self).__init__()

                        self.yang_name = "ipv4-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit)), ("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")

                        self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ipv4-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "ipv4-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters for common IPv4 and IPv6 unicast
                        AFI\-SAFI options
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ipv4-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                            ])
                            self.send_default_route = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config, ['send_default_route'], name, value)


                    class State(Entity):
                        """
                        State information for common IPv4 and IPv6 unicast
                        parameters
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ipv4-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                            ])
                            self.send_default_route = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State, ['send_default_route'], name, value)


                class Ipv6Unicast(Entity):
                    """
                    IPv6 unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                    
                    .. attribute:: state
                    
                    	State information for common IPv4 and IPv6 unicast parameters
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast, self).__init__()

                        self.yang_name = "ipv6-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit)), ("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")

                        self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ipv6-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "ipv6-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters for common IPv4 and IPv6 unicast
                        AFI\-SAFI options
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ipv6-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                            ])
                            self.send_default_route = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config, ['send_default_route'], name, value)


                    class State(Entity):
                        """
                        State information for common IPv4 and IPv6 unicast
                        parameters
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ipv6-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                            ])
                            self.send_default_route = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State, ['send_default_route'], name, value)


                class Ipv4LabeledUnicast(Entity):
                    """
                    IPv4 Labeled Unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast, self).__init__()

                        self.yang_name = "ipv4-labeled-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "ipv4-labeled-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "ipv4-labeled-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class Ipv6LabeledUnicast(Entity):
                    """
                    IPv6 Labeled Unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast, self).__init__()

                        self.yang_name = "ipv6-labeled-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "ipv6-labeled-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "ipv6-labeled-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L3VpnIpv4Unicast(Entity):
                    """
                    Unicast IPv4 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast, self).__init__()

                        self.yang_name = "l3vpn-ipv4-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l3vpn-ipv4-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l3vpn-ipv4-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L3VpnIpv6Unicast(Entity):
                    """
                    Unicast IPv6 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast, self).__init__()

                        self.yang_name = "l3vpn-ipv6-unicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l3vpn-ipv6-unicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l3vpn-ipv6-unicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L3VpnIpv4Multicast(Entity):
                    """
                    Multicast IPv4 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast, self).__init__()

                        self.yang_name = "l3vpn-ipv4-multicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l3vpn-ipv4-multicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l3vpn-ipv4-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L3VpnIpv6Multicast(Entity):
                    """
                    Multicast IPv6 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast, self).__init__()

                        self.yang_name = "l3vpn-ipv6-multicast"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l3vpn-ipv6-multicast"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l3vpn-ipv6-multicast"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L2VpnVpls(Entity):
                    """
                    BGP\-signalled VPLS configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls, self).__init__()

                        self.yang_name = "l2vpn-vpls"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l2vpn-vpls"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l2vpn-vpls"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                class L2VpnEvpn(Entity):
                    """
                    BGP EVPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn, self).__init__()

                        self.yang_name = "l2vpn-evpn"
                        self.yang_parent_name = "afi-safi"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                        self.prefix_limit.parent = self
                        self._children_name_map["prefix_limit"] = "prefix-limit"
                        self._children_yang_names.add("prefix-limit")
                        self._segment_path = lambda: "l2vpn-evpn"


                    class PrefixLimit(Entity):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit, self).__init__()

                            self.yang_name = "prefix-limit"
                            self.yang_parent_name = "l2vpn-evpn"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config)), ("state", ("state", Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix-limit"


                        class Config(Entity):
                            """
                            Configuration parameters relating to the prefix
                            limit for the AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class State(Entity):
                            """
                            State information relating to the prefix\-limit for the
                            AFI\-SAFI
                            
                            .. attribute:: max_prefixes
                            
                            	Maximum number of prefixes that will be accepted from the neighbour
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: shutdown_threshold_pct
                            
                            	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            .. attribute:: restart_timer
                            
                            	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix-limit"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                    ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                    ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                ])
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


        class ApplyPolicy(Entity):
            """
            Anchor point for routing policies in the model.
            Import and export policies are with respect to the local
            routing table, i.e., export (send) and import (receive),
            depending on the context.
            
            .. attribute:: config
            
            	Policy configuration data
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Global.ApplyPolicy.Config>`
            
            .. attribute:: state
            
            	Operational state for routing policy
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Global.ApplyPolicy.State>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Global.ApplyPolicy, self).__init__()

                self.yang_name = "apply-policy"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Global.ApplyPolicy.Config)), ("state", ("state", Bgp.Global.ApplyPolicy.State))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.config = Bgp.Global.ApplyPolicy.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Global.ApplyPolicy.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "apply-policy"
                self._absolute_path = lambda: "openconfig-bgp:bgp/global/%s" % self._segment_path()


            class Config(Entity):
                """
                Policy configuration data.
                
                .. attribute:: import_policy
                
                	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                
                .. attribute:: default_import_policy
                
                	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                
                	**default value**\: REJECT_ROUTE
                
                .. attribute:: export_policy
                
                	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                
                .. attribute:: default_export_policy
                
                	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                
                	**default value**\: REJECT_ROUTE
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.ApplyPolicy.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "apply-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('import_policy', YLeafList(YType.str, 'import-policy')),
                        ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                        ('export_policy', YLeafList(YType.str, 'export-policy')),
                        ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                    ])
                    self.import_policy = []
                    self.default_import_policy = None
                    self.export_policy = []
                    self.default_export_policy = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/apply-policy/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


            class State(Entity):
                """
                Operational state for routing policy
                
                .. attribute:: import_policy
                
                	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                
                .. attribute:: default_import_policy
                
                	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                
                	**default value**\: REJECT_ROUTE
                
                .. attribute:: export_policy
                
                	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                
                .. attribute:: default_export_policy
                
                	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                
                	**default value**\: REJECT_ROUTE
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Global.ApplyPolicy.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "apply-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('import_policy', YLeafList(YType.str, 'import-policy')),
                        ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                        ('export_policy', YLeafList(YType.str, 'export-policy')),
                        ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                    ])
                    self.import_policy = []
                    self.default_import_policy = None
                    self.export_policy = []
                    self.default_export_policy = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-bgp:bgp/global/apply-policy/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Global.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


    class Neighbors(Entity):
        """
        Configuration for BGP neighbors
        
        .. attribute:: neighbor
        
        	List of BGP neighbors configured on the local system, uniquely identified by peer IPv[46] address
        	**type**\: list of  		 :py:class:`Neighbor <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'oc-bgp'
        _revision = '2016-06-21'

        def __init__(self):
            super(Bgp.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "bgp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("neighbor", ("neighbor", Bgp.Neighbors.Neighbor))])
            self._leafs = OrderedDict()

            self.neighbor = YList(self)
            self._segment_path = lambda: "neighbors"
            self._absolute_path = lambda: "openconfig-bgp:bgp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bgp.Neighbors, [], name, value)


        class Neighbor(Entity):
            """
            List of BGP neighbors configured on the local system,
            uniquely identified by peer IPv[46] address
            
            .. attribute:: neighbor_address  (key)
            
            	Reference to the address of the BGP neighbor used as a key in the neighbor list
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`neighbor_address <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Config>`
            
            .. attribute:: config
            
            	Configuration parameters relating to the BGP neighbor or group
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP neighbor
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State>`
            
            .. attribute:: timers
            
            	Timers related to a BGP neighbor
            	**type**\:  :py:class:`Timers <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Timers>`
            
            .. attribute:: transport
            
            	Transport session parameters for the BGP neighbor
            	**type**\:  :py:class:`Transport <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Transport>`
            
            .. attribute:: error_handling
            
            	Error handling parameters used for the BGP neighbor or group
            	**type**\:  :py:class:`ErrorHandling <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ErrorHandling>`
            
            .. attribute:: graceful_restart
            
            	Parameters relating the graceful restart mechanism for BGP
            	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.GracefulRestart>`
            
            .. attribute:: logging_options
            
            	Logging options for events related to the BGP neighbor or group
            	**type**\:  :py:class:`LoggingOptions <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.LoggingOptions>`
            
            .. attribute:: ebgp_multihop
            
            	eBGP multi\-hop parameters for the BGPgroup
            	**type**\:  :py:class:`EbgpMultihop <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.EbgpMultihop>`
            
            .. attribute:: route_reflector
            
            	Route reflector parameters for the BGPgroup
            	**type**\:  :py:class:`RouteReflector <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.RouteReflector>`
            
            .. attribute:: as_path_options
            
            	AS\_PATH manipulation parameters for the BGP neighbor or group
            	**type**\:  :py:class:`AsPathOptions <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AsPathOptions>`
            
            .. attribute:: add_paths
            
            	Parameters relating to the advertisement and receipt of multiple paths for a single NLRI (add\-paths)
            	**type**\:  :py:class:`AddPaths <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AddPaths>`
            
            .. attribute:: use_multiple_paths
            
            	Parameters related to the use of multiple\-paths for the same NLRI when they are received only from this neighbor
            	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths>`
            
            .. attribute:: apply_policy
            
            	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
            	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ApplyPolicy>`
            
            .. attribute:: afi_safis
            
            	Per\-address\-family configuration parameters associated with the neighbor
            	**type**\:  :py:class:`AfiSafis <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['neighbor_address']
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.State)), ("timers", ("timers", Bgp.Neighbors.Neighbor.Timers)), ("transport", ("transport", Bgp.Neighbors.Neighbor.Transport)), ("error-handling", ("error_handling", Bgp.Neighbors.Neighbor.ErrorHandling)), ("graceful-restart", ("graceful_restart", Bgp.Neighbors.Neighbor.GracefulRestart)), ("logging-options", ("logging_options", Bgp.Neighbors.Neighbor.LoggingOptions)), ("ebgp-multihop", ("ebgp_multihop", Bgp.Neighbors.Neighbor.EbgpMultihop)), ("route-reflector", ("route_reflector", Bgp.Neighbors.Neighbor.RouteReflector)), ("as-path-options", ("as_path_options", Bgp.Neighbors.Neighbor.AsPathOptions)), ("add-paths", ("add_paths", Bgp.Neighbors.Neighbor.AddPaths)), ("use-multiple-paths", ("use_multiple_paths", Bgp.Neighbors.Neighbor.UseMultiplePaths)), ("apply-policy", ("apply_policy", Bgp.Neighbors.Neighbor.ApplyPolicy)), ("afi-safis", ("afi_safis", Bgp.Neighbors.Neighbor.AfiSafis))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                ])
                self.neighbor_address = None

                self.config = Bgp.Neighbors.Neighbor.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.Neighbors.Neighbor.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.timers = Bgp.Neighbors.Neighbor.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")

                self.transport = Bgp.Neighbors.Neighbor.Transport()
                self.transport.parent = self
                self._children_name_map["transport"] = "transport"
                self._children_yang_names.add("transport")

                self.error_handling = Bgp.Neighbors.Neighbor.ErrorHandling()
                self.error_handling.parent = self
                self._children_name_map["error_handling"] = "error-handling"
                self._children_yang_names.add("error-handling")

                self.graceful_restart = Bgp.Neighbors.Neighbor.GracefulRestart()
                self.graceful_restart.parent = self
                self._children_name_map["graceful_restart"] = "graceful-restart"
                self._children_yang_names.add("graceful-restart")

                self.logging_options = Bgp.Neighbors.Neighbor.LoggingOptions()
                self.logging_options.parent = self
                self._children_name_map["logging_options"] = "logging-options"
                self._children_yang_names.add("logging-options")

                self.ebgp_multihop = Bgp.Neighbors.Neighbor.EbgpMultihop()
                self.ebgp_multihop.parent = self
                self._children_name_map["ebgp_multihop"] = "ebgp-multihop"
                self._children_yang_names.add("ebgp-multihop")

                self.route_reflector = Bgp.Neighbors.Neighbor.RouteReflector()
                self.route_reflector.parent = self
                self._children_name_map["route_reflector"] = "route-reflector"
                self._children_yang_names.add("route-reflector")

                self.as_path_options = Bgp.Neighbors.Neighbor.AsPathOptions()
                self.as_path_options.parent = self
                self._children_name_map["as_path_options"] = "as-path-options"
                self._children_yang_names.add("as-path-options")

                self.add_paths = Bgp.Neighbors.Neighbor.AddPaths()
                self.add_paths.parent = self
                self._children_name_map["add_paths"] = "add-paths"
                self._children_yang_names.add("add-paths")

                self.use_multiple_paths = Bgp.Neighbors.Neighbor.UseMultiplePaths()
                self.use_multiple_paths.parent = self
                self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
                self._children_yang_names.add("use-multiple-paths")

                self.apply_policy = Bgp.Neighbors.Neighbor.ApplyPolicy()
                self.apply_policy.parent = self
                self._children_name_map["apply_policy"] = "apply-policy"
                self._children_yang_names.add("apply-policy")

                self.afi_safis = Bgp.Neighbors.Neighbor.AfiSafis()
                self.afi_safis.parent = self
                self._children_name_map["afi_safis"] = "afi-safis"
                self._children_yang_names.add("afi-safis")
                self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                self._absolute_path = lambda: "openconfig-bgp:bgp/neighbors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bgp.Neighbors.Neighbor, ['neighbor_address'], name, value)


            class Config(Entity):
                """
                Configuration parameters relating to the BGP neighbor or
                group
                
                .. attribute:: peer_group
                
                	The peer\-group with which this neighbor is associated
                	**type**\: str
                
                	**refers to**\:  :py:class:`peer_group_name <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup>`
                
                .. attribute:: neighbor_address
                
                	Address of the BGP peer, either in IPv4 or IPv6
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: enabled
                
                	Whether the BGP peer is enabled. In cases where the enabled leaf is set to false, the local system should not initiate connections to the neighbor, and should not respond to TCP connections attempts from the neighbor. If the state of the BGP session is ESTABLISHED at the time that this leaf is set to false, the BGP session should be ceased
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: peer_as
                
                	AS number of the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_as
                
                	The local autonomous system number that is to be used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_type
                
                	Explicitly designate the peer or peer group as internal (iBGP) or external (eBGP)
                	**type**\:  :py:class:`PeerType <ydk.models.openconfig.openconfig_bgp_types.PeerType>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers \- when this leaf is not specified, the AS\_PATH attribute should be sent to the peer unchanged
                	**type**\:  :py:class:`REMOVEPRIVATEASOPTION <ydk.models.openconfig.openconfig_bgp_types.REMOVEPRIVATEASOPTION>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\:  :py:class:`CommunityType <ydk.models.openconfig.openconfig_bgp_types.CommunityType>`
                
                	**default value**\: NONE
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_group', YLeaf(YType.str, 'peer-group')),
                        ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('peer_as', YLeaf(YType.uint32, 'peer-as')),
                        ('local_as', YLeaf(YType.uint32, 'local-as')),
                        ('peer_type', YLeaf(YType.enumeration, 'peer-type')),
                        ('auth_password', YLeaf(YType.str, 'auth-password')),
                        ('remove_private_as', YLeaf(YType.identityref, 'remove-private-as')),
                        ('route_flap_damping', YLeaf(YType.boolean, 'route-flap-damping')),
                        ('send_community', YLeaf(YType.enumeration, 'send-community')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.peer_group = None
                    self.neighbor_address = None
                    self.enabled = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Neighbors.Neighbor.Config, ['peer_group', 'neighbor_address', 'enabled', 'peer_as', 'local_as', 'peer_type', 'auth_password', 'remove_private_as', 'route_flap_damping', 'send_community', 'description'], name, value)


            class State(Entity):
                """
                State information relating to the BGP neighbor
                
                .. attribute:: peer_group
                
                	The peer\-group with which this neighbor is associated
                	**type**\: str
                
                	**refers to**\:  :py:class:`peer_group_name <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup>`
                
                .. attribute:: neighbor_address
                
                	Address of the BGP peer, either in IPv4 or IPv6
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: enabled
                
                	Whether the BGP peer is enabled. In cases where the enabled leaf is set to false, the local system should not initiate connections to the neighbor, and should not respond to TCP connections attempts from the neighbor. If the state of the BGP session is ESTABLISHED at the time that this leaf is set to false, the BGP session should be ceased
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: peer_as
                
                	AS number of the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_as
                
                	The local autonomous system number that is to be used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_type
                
                	Explicitly designate the peer or peer group as internal (iBGP) or external (eBGP)
                	**type**\:  :py:class:`PeerType <ydk.models.openconfig.openconfig_bgp_types.PeerType>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers \- when this leaf is not specified, the AS\_PATH attribute should be sent to the peer unchanged
                	**type**\:  :py:class:`REMOVEPRIVATEASOPTION <ydk.models.openconfig.openconfig_bgp_types.REMOVEPRIVATEASOPTION>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\:  :py:class:`CommunityType <ydk.models.openconfig.openconfig_bgp_types.CommunityType>`
                
                	**default value**\: NONE
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: session_state
                
                	Operational state of the BGP peer
                	**type**\:  :py:class:`SessionState <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State.SessionState>`
                
                .. attribute:: last_established
                
                	This timestamp indicates the time that the BGP session last transitioned in or out of the Established state.  The value is the timestamp in seconds relative to the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC). The BGP session uptime can be computed by clients as the difference between this value and the current time in UTC (assuming the session is in the ESTABLISHED state, per the session\-state leaf)
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: established_transitions
                
                	Number of transitions to the Established state for the neighbor session.  This value is analogous to the bgpPeerFsmEstablishedTransitions object from the standard BGP\-4 MIB
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: supported_capabilities
                
                	BGP capabilities negotiated as supported with the peer
                	**type**\: list of   :py:class:`BGPCAPABILITY <ydk.models.openconfig.openconfig_bgp_types.BGPCAPABILITY>`
                
                .. attribute:: messages
                
                	Counters for BGP messages sent and received from the neighbor
                	**type**\:  :py:class:`Messages <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State.Messages>`
                
                .. attribute:: queues
                
                	Counters related to queued messages associated with the BGP neighbor
                	**type**\:  :py:class:`Queues <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State.Queues>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("messages", ("messages", Bgp.Neighbors.Neighbor.State.Messages)), ("queues", ("queues", Bgp.Neighbors.Neighbor.State.Queues))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_group', YLeaf(YType.str, 'peer-group')),
                        ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ('peer_as', YLeaf(YType.uint32, 'peer-as')),
                        ('local_as', YLeaf(YType.uint32, 'local-as')),
                        ('peer_type', YLeaf(YType.enumeration, 'peer-type')),
                        ('auth_password', YLeaf(YType.str, 'auth-password')),
                        ('remove_private_as', YLeaf(YType.identityref, 'remove-private-as')),
                        ('route_flap_damping', YLeaf(YType.boolean, 'route-flap-damping')),
                        ('send_community', YLeaf(YType.enumeration, 'send-community')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('session_state', YLeaf(YType.enumeration, 'session-state')),
                        ('last_established', YLeaf(YType.uint64, 'last-established')),
                        ('established_transitions', YLeaf(YType.uint64, 'established-transitions')),
                        ('supported_capabilities', YLeafList(YType.identityref, 'supported-capabilities')),
                    ])
                    self.peer_group = None
                    self.neighbor_address = None
                    self.enabled = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.session_state = None
                    self.last_established = None
                    self.established_transitions = None
                    self.supported_capabilities = []

                    self.messages = Bgp.Neighbors.Neighbor.State.Messages()
                    self.messages.parent = self
                    self._children_name_map["messages"] = "messages"
                    self._children_yang_names.add("messages")

                    self.queues = Bgp.Neighbors.Neighbor.State.Queues()
                    self.queues.parent = self
                    self._children_name_map["queues"] = "queues"
                    self._children_yang_names.add("queues")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Neighbors.Neighbor.State, ['peer_group', 'neighbor_address', 'enabled', 'peer_as', 'local_as', 'peer_type', 'auth_password', 'remove_private_as', 'route_flap_damping', 'send_community', 'description', 'session_state', 'last_established', 'established_transitions', 'supported_capabilities'], name, value)

                class SessionState(Enum):
                    """
                    SessionState (Enum Class)

                    Operational state of the BGP peer

                    .. data:: IDLE = 0

                    	neighbor is down, and in the Idle state of the

                    	FSM

                    .. data:: CONNECT = 1

                    	neighbor is down, and the session is waiting for

                    	the underlying transport session to be established

                    .. data:: ACTIVE = 2

                    	neighbor is down, and the local system is awaiting

                    	a conncetion from the remote peer

                    .. data:: OPENSENT = 3

                    	neighbor is in the process of being established.

                    	The local system has sent an OPEN message

                    .. data:: OPENCONFIRM = 4

                    	neighbor is in the process of being established.

                    	The local system is awaiting a NOTIFICATION or

                    	KEEPALIVE message

                    .. data:: ESTABLISHED = 5

                    	neighbor is up - the BGP session with the peer is

                    	established

                    """

                    IDLE = Enum.YLeaf(0, "IDLE")

                    CONNECT = Enum.YLeaf(1, "CONNECT")

                    ACTIVE = Enum.YLeaf(2, "ACTIVE")

                    OPENSENT = Enum.YLeaf(3, "OPENSENT")

                    OPENCONFIRM = Enum.YLeaf(4, "OPENCONFIRM")

                    ESTABLISHED = Enum.YLeaf(5, "ESTABLISHED")



                class Messages(Entity):
                    """
                    Counters for BGP messages sent and received from the
                    neighbor
                    
                    .. attribute:: sent
                    
                    	Counters relating to BGP messages sent to the neighbor
                    	**type**\:  :py:class:`Sent <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State.Messages.Sent>`
                    
                    .. attribute:: received
                    
                    	Counters for BGP messages received from the neighbor
                    	**type**\:  :py:class:`Received <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.State.Messages.Received>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.State.Messages, self).__init__()

                        self.yang_name = "messages"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("sent", ("sent", Bgp.Neighbors.Neighbor.State.Messages.Sent)), ("received", ("received", Bgp.Neighbors.Neighbor.State.Messages.Received))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.sent = Bgp.Neighbors.Neighbor.State.Messages.Sent()
                        self.sent.parent = self
                        self._children_name_map["sent"] = "sent"
                        self._children_yang_names.add("sent")

                        self.received = Bgp.Neighbors.Neighbor.State.Messages.Received()
                        self.received.parent = self
                        self._children_name_map["received"] = "received"
                        self._children_yang_names.add("received")
                        self._segment_path = lambda: "messages"


                    class Sent(Entity):
                        """
                        Counters relating to BGP messages sent to the neighbor
                        
                        .. attribute:: update
                        
                        	Number of BGP UPDATE messages announcing, withdrawing or modifying paths exchanged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: notification
                        
                        	Number of BGP NOTIFICATION messages indicating an error condition has occurred exchanged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.State.Messages.Sent, self).__init__()

                            self.yang_name = "sent"
                            self.yang_parent_name = "messages"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('update', YLeaf(YType.uint64, 'UPDATE')),
                                ('notification', YLeaf(YType.uint64, 'NOTIFICATION')),
                            ])
                            self.update = None
                            self.notification = None
                            self._segment_path = lambda: "sent"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.State.Messages.Sent, ['update', 'notification'], name, value)


                    class Received(Entity):
                        """
                        Counters for BGP messages received from the neighbor
                        
                        .. attribute:: update
                        
                        	Number of BGP UPDATE messages announcing, withdrawing or modifying paths exchanged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: notification
                        
                        	Number of BGP NOTIFICATION messages indicating an error condition has occurred exchanged
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.State.Messages.Received, self).__init__()

                            self.yang_name = "received"
                            self.yang_parent_name = "messages"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('update', YLeaf(YType.uint64, 'UPDATE')),
                                ('notification', YLeaf(YType.uint64, 'NOTIFICATION')),
                            ])
                            self.update = None
                            self.notification = None
                            self._segment_path = lambda: "received"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.State.Messages.Received, ['update', 'notification'], name, value)


                class Queues(Entity):
                    """
                    Counters related to queued messages associated with the
                    BGP neighbor
                    
                    .. attribute:: input
                    
                    	The number of messages received from the peer currently queued
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output
                    
                    	The number of messages queued to be sent to the peer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.State.Queues, self).__init__()

                        self.yang_name = "queues"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('input', YLeaf(YType.uint32, 'input')),
                            ('output', YLeaf(YType.uint32, 'output')),
                        ])
                        self.input = None
                        self.output = None
                        self._segment_path = lambda: "queues"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.State.Queues, ['input', 'output'], name, value)


            class Timers(Entity):
                """
                Timers related to a BGP neighbor
                
                .. attribute:: config
                
                	Configuration parameters relating to timers used for the BGP neighbor
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Timers.Config>`
                
                .. attribute:: state
                
                	State information relating to the timers used for the BGP neighbor
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Timers.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.Timers.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.Timers.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.Timers.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.Timers.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "timers"


                class Config(Entity):
                    """
                    Configuration parameters relating to timers used for the
                    BGP neighbor
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 90
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.Timers.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('connect_retry', YLeaf(YType.str, 'connect-retry')),
                            ('hold_time', YLeaf(YType.str, 'hold-time')),
                            ('keepalive_interval', YLeaf(YType.str, 'keepalive-interval')),
                            ('minimum_advertisement_interval', YLeaf(YType.str, 'minimum-advertisement-interval')),
                        ])
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.Timers.Config, ['connect_retry', 'hold_time', 'keepalive_interval', 'minimum_advertisement_interval'], name, value)


                class State(Entity):
                    """
                    State information relating to the timers used for the BGP
                    neighbor
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 90
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: negotiated_hold_time
                    
                    	The negotiated hold\-time for the BGP session
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.Timers.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('connect_retry', YLeaf(YType.str, 'connect-retry')),
                            ('hold_time', YLeaf(YType.str, 'hold-time')),
                            ('keepalive_interval', YLeaf(YType.str, 'keepalive-interval')),
                            ('minimum_advertisement_interval', YLeaf(YType.str, 'minimum-advertisement-interval')),
                            ('negotiated_hold_time', YLeaf(YType.str, 'negotiated-hold-time')),
                        ])
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None
                        self.negotiated_hold_time = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.Timers.State, ['connect_retry', 'hold_time', 'keepalive_interval', 'minimum_advertisement_interval', 'negotiated_hold_time'], name, value)


            class Transport(Entity):
                """
                Transport session parameters for the BGP neighbor
                
                .. attribute:: config
                
                	Configuration parameters relating to the transport session(s) used for the BGP neighbor
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Transport.Config>`
                
                .. attribute:: state
                
                	State information relating to the transport session(s) used for the BGP neighbor
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.Transport.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.Transport.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.Transport.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.Transport.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.Transport.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "transport"


                class Config(Entity):
                    """
                    Configuration parameters relating to the transport
                    session(s) used for the BGP neighbor
                    
                    .. attribute:: tcp_mss
                    
                    	Sets the max segment size for BGP TCP sessions
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mtu_discovery
                    
                    	Turns path mtu discovery for BGP TCP sessions on (true) or off (false)
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.Transport.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "transport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_mss', YLeaf(YType.uint16, 'tcp-mss')),
                            ('mtu_discovery', YLeaf(YType.boolean, 'mtu-discovery')),
                            ('passive_mode', YLeaf(YType.boolean, 'passive-mode')),
                            ('local_address', YLeaf(YType.str, 'local-address')),
                        ])
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.Transport.Config, ['tcp_mss', 'mtu_discovery', 'passive_mode', 'local_address'], name, value)


                class State(Entity):
                    """
                    State information relating to the transport session(s)
                    used for the BGP neighbor
                    
                    .. attribute:: tcp_mss
                    
                    	Sets the max segment size for BGP TCP sessions
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mtu_discovery
                    
                    	Turns path mtu discovery for BGP TCP sessions on (true) or off (false)
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    .. attribute:: local_port
                    
                    	Local TCP port being used for the TCP session supporting the BGP session
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: remote_address
                    
                    	Remote address to which the BGP session has been established
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: remote_port
                    
                    	Remote port being used by the peer for the TCP session supporting the BGP session
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.Transport.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "transport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_mss', YLeaf(YType.uint16, 'tcp-mss')),
                            ('mtu_discovery', YLeaf(YType.boolean, 'mtu-discovery')),
                            ('passive_mode', YLeaf(YType.boolean, 'passive-mode')),
                            ('local_address', YLeaf(YType.str, 'local-address')),
                            ('local_port', YLeaf(YType.uint16, 'local-port')),
                            ('remote_address', YLeaf(YType.str, 'remote-address')),
                            ('remote_port', YLeaf(YType.uint16, 'remote-port')),
                        ])
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None
                        self.local_port = None
                        self.remote_address = None
                        self.remote_port = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.Transport.State, ['tcp_mss', 'mtu_discovery', 'passive_mode', 'local_address', 'local_port', 'remote_address', 'remote_port'], name, value)


            class ErrorHandling(Entity):
                """
                Error handling parameters used for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying the behavior or enhanced error handling mechanisms for the BGP neighbor
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ErrorHandling.Config>`
                
                .. attribute:: state
                
                	State information relating to enhanced error handling mechanisms for the BGP neighbor
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ErrorHandling.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.ErrorHandling, self).__init__()

                    self.yang_name = "error-handling"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.ErrorHandling.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.ErrorHandling.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.ErrorHandling.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.ErrorHandling.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "error-handling"


                class Config(Entity):
                    """
                    Configuration parameters enabling or modifying the
                    behavior or enhanced error handling mechanisms for the BGP
                    neighbor
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.ErrorHandling.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "error-handling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('treat_as_withdraw', YLeaf(YType.boolean, 'treat-as-withdraw')),
                        ])
                        self.treat_as_withdraw = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.ErrorHandling.Config, ['treat_as_withdraw'], name, value)


                class State(Entity):
                    """
                    State information relating to enhanced error handling
                    mechanisms for the BGP neighbor
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: erroneous_update_messages
                    
                    	The number of BGP UPDATE messages for which the treat\-as\-withdraw mechanism has been applied based on erroneous message contents
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.ErrorHandling.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "error-handling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('treat_as_withdraw', YLeaf(YType.boolean, 'treat-as-withdraw')),
                            ('erroneous_update_messages', YLeaf(YType.uint32, 'erroneous-update-messages')),
                        ])
                        self.treat_as_withdraw = None
                        self.erroneous_update_messages = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.ErrorHandling.State, ['treat_as_withdraw', 'erroneous_update_messages'], name, value)


            class GracefulRestart(Entity):
                """
                Parameters relating the graceful restart mechanism for BGP
                
                .. attribute:: config
                
                	Configuration parameters relating to graceful\-restart
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.GracefulRestart.Config>`
                
                .. attribute:: state
                
                	State information associated with graceful\-restart
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.GracefulRestart.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.GracefulRestart, self).__init__()

                    self.yang_name = "graceful-restart"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.GracefulRestart.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.GracefulRestart.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.GracefulRestart.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.GracefulRestart.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "graceful-restart"


                class Config(Entity):
                    """
                    Configuration parameters relating to graceful\-restart
                    
                    .. attribute:: enabled
                    
                    	Enable or disable the graceful\-restart capability
                    	**type**\: bool
                    
                    .. attribute:: restart_time
                    
                    	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: stale_routes_time
                    
                    	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.GracefulRestart.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "graceful-restart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                            ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                            ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                        ])
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.GracefulRestart.Config, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only'], name, value)


                class State(Entity):
                    """
                    State information associated with graceful\-restart
                    
                    .. attribute:: enabled
                    
                    	Enable or disable the graceful\-restart capability
                    	**type**\: bool
                    
                    .. attribute:: restart_time
                    
                    	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: stale_routes_time
                    
                    	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    .. attribute:: peer_restart_time
                    
                    	The period of time (advertised by the peer) that the peer expects a restart of a BGP session to take
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: peer_restarting
                    
                    	This flag indicates whether the remote neighbor is currently in the process of restarting, and hence received routes are currently stale
                    	**type**\: bool
                    
                    .. attribute:: local_restarting
                    
                    	This flag indicates whether the local neighbor is currently restarting. The flag is unset after all NLRI have been advertised to the peer, and the End\-of\-RIB (EOR) marker has been unset
                    	**type**\: bool
                    
                    .. attribute:: mode
                    
                    	Ths leaf indicates the mode of operation of BGP graceful restart with the peer
                    	**type**\:  :py:class:`Mode <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.GracefulRestart.State.Mode>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.GracefulRestart.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "graceful-restart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                            ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                            ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                            ('peer_restart_time', YLeaf(YType.uint16, 'peer-restart-time')),
                            ('peer_restarting', YLeaf(YType.boolean, 'peer-restarting')),
                            ('local_restarting', YLeaf(YType.boolean, 'local-restarting')),
                            ('mode', YLeaf(YType.enumeration, 'mode')),
                        ])
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None
                        self.peer_restart_time = None
                        self.peer_restarting = None
                        self.local_restarting = None
                        self.mode = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.GracefulRestart.State, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only', 'peer_restart_time', 'peer_restarting', 'local_restarting', 'mode'], name, value)

                    class Mode(Enum):
                        """
                        Mode (Enum Class)

                        Ths leaf indicates the mode of operation of BGP graceful

                        restart with the peer

                        .. data:: HELPER_ONLY = 0

                        	The local router is operating in helper-only mode, and

                        	hence will not retain forwarding state during a local

                        	session restart, but will do so during a restart of the

                        	remote peer

                        .. data:: BILATERAL = 1

                        	The local router is operating in both helper mode, and

                        	hence retains forwarding state during a remote restart,

                        	and also maintains forwarding state during local session

                        	restart

                        .. data:: REMOTE_HELPER = 2

                        	The local system is able to retain routes during restart

                        	but the remote system is only able to act as a helper

                        """

                        HELPER_ONLY = Enum.YLeaf(0, "HELPER_ONLY")

                        BILATERAL = Enum.YLeaf(1, "BILATERAL")

                        REMOTE_HELPER = Enum.YLeaf(2, "REMOTE_HELPER")



            class LoggingOptions(Entity):
                """
                Logging options for events related to the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying logging for events relating to the BGPgroup
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.LoggingOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to logging for the BGP neighbor or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.LoggingOptions.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.LoggingOptions, self).__init__()

                    self.yang_name = "logging-options"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.LoggingOptions.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.LoggingOptions.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.LoggingOptions.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.LoggingOptions.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "logging-options"


                class Config(Entity):
                    """
                    Configuration parameters enabling or modifying logging
                    for events relating to the BGPgroup
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.LoggingOptions.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "logging-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_neighbor_state_changes', YLeaf(YType.boolean, 'log-neighbor-state-changes')),
                        ])
                        self.log_neighbor_state_changes = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.LoggingOptions.Config, ['log_neighbor_state_changes'], name, value)


                class State(Entity):
                    """
                    State information relating to logging for the BGP neighbor
                    or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.LoggingOptions.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "logging-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_neighbor_state_changes', YLeaf(YType.boolean, 'log-neighbor-state-changes')),
                        ])
                        self.log_neighbor_state_changes = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.LoggingOptions.State, ['log_neighbor_state_changes'], name, value)


            class EbgpMultihop(Entity):
                """
                eBGP multi\-hop parameters for the BGPgroup
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multihop for the BGP group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.EbgpMultihop.Config>`
                
                .. attribute:: state
                
                	State information for eBGP multihop, for the BGP neighbor or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.EbgpMultihop.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.EbgpMultihop, self).__init__()

                    self.yang_name = "ebgp-multihop"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.EbgpMultihop.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.EbgpMultihop.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.EbgpMultihop.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.EbgpMultihop.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ebgp-multihop"


                class Config(Entity):
                    """
                    Configuration parameters relating to eBGP multihop for the
                    BGP group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.EbgpMultihop.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ebgp-multihop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('multihop_ttl', YLeaf(YType.uint8, 'multihop-ttl')),
                        ])
                        self.enabled = None
                        self.multihop_ttl = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.EbgpMultihop.Config, ['enabled', 'multihop_ttl'], name, value)


                class State(Entity):
                    """
                    State information for eBGP multihop, for the BGP neighbor
                    or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.EbgpMultihop.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ebgp-multihop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('multihop_ttl', YLeaf(YType.uint8, 'multihop-ttl')),
                        ])
                        self.enabled = None
                        self.multihop_ttl = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.EbgpMultihop.State, ['enabled', 'multihop_ttl'], name, value)


            class RouteReflector(Entity):
                """
                Route reflector parameters for the BGPgroup
                
                .. attribute:: config
                
                	Configuraton parameters relating to route reflection for the BGPgroup
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.RouteReflector.Config>`
                
                .. attribute:: state
                
                	State information relating to route reflection for the BGPgroup
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.RouteReflector.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.RouteReflector, self).__init__()

                    self.yang_name = "route-reflector"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.RouteReflector.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.RouteReflector.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.RouteReflector.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.RouteReflector.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "route-reflector"


                class Config(Entity):
                    """
                    Configuraton parameters relating to route reflection
                    for the BGPgroup
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.RouteReflector.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "route-reflector"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_reflector_cluster_id', YLeaf(YType.str, 'route-reflector-cluster-id')),
                            ('route_reflector_client', YLeaf(YType.boolean, 'route-reflector-client')),
                        ])
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.RouteReflector.Config, ['route_reflector_cluster_id', 'route_reflector_client'], name, value)


                class State(Entity):
                    """
                    State information relating to route reflection for the
                    BGPgroup
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.RouteReflector.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "route-reflector"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_reflector_cluster_id', YLeaf(YType.str, 'route-reflector-cluster-id')),
                            ('route_reflector_client', YLeaf(YType.boolean, 'route-reflector-client')),
                        ])
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.RouteReflector.State, ['route_reflector_cluster_id', 'route_reflector_client'], name, value)


            class AsPathOptions(Entity):
                """
                AS\_PATH manipulation parameters for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters relating to AS\_PATH manipulation for the BGP peer or group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AsPathOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to the AS\_PATH manipulation mechanisms for the BGP peer or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AsPathOptions.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.AsPathOptions, self).__init__()

                    self.yang_name = "as-path-options"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AsPathOptions.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AsPathOptions.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.AsPathOptions.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.AsPathOptions.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "as-path-options"


                class Config(Entity):
                    """
                    Configuration parameters relating to AS\_PATH manipulation
                    for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**default value**\: 0
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.AsPathOptions.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "as-path-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_own_as', YLeaf(YType.uint8, 'allow-own-as')),
                            ('replace_peer_as', YLeaf(YType.boolean, 'replace-peer-as')),
                        ])
                        self.allow_own_as = None
                        self.replace_peer_as = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.AsPathOptions.Config, ['allow_own_as', 'replace_peer_as'], name, value)


                class State(Entity):
                    """
                    State information relating to the AS\_PATH manipulation
                    mechanisms for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**default value**\: 0
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.AsPathOptions.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "as-path-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_own_as', YLeaf(YType.uint8, 'allow-own-as')),
                            ('replace_peer_as', YLeaf(YType.boolean, 'replace-peer-as')),
                        ])
                        self.allow_own_as = None
                        self.replace_peer_as = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.AsPathOptions.State, ['allow_own_as', 'replace_peer_as'], name, value)


            class AddPaths(Entity):
                """
                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add\-paths)
                
                .. attribute:: config
                
                	Configuration parameters relating to ADD\_PATHS
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AddPaths.Config>`
                
                .. attribute:: state
                
                	State information associated with ADD\_PATHS
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AddPaths.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.AddPaths, self).__init__()

                    self.yang_name = "add-paths"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AddPaths.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AddPaths.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.AddPaths.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.AddPaths.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "add-paths"


                class Config(Entity):
                    """
                    Configuration parameters relating to ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: eligible_prefix_policy
                    
                    	A reference to a routing policy which can be used to restrict the prefixes for which add\-paths is enabled
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.AddPaths.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "add-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('receive', YLeaf(YType.boolean, 'receive')),
                            ('send_max', YLeaf(YType.uint8, 'send-max')),
                            ('eligible_prefix_policy', YLeaf(YType.str, 'eligible-prefix-policy')),
                        ])
                        self.receive = None
                        self.send_max = None
                        self.eligible_prefix_policy = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.AddPaths.Config, ['receive', 'send_max', 'eligible_prefix_policy'], name, value)


                class State(Entity):
                    """
                    State information associated with ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: eligible_prefix_policy
                    
                    	A reference to a routing policy which can be used to restrict the prefixes for which add\-paths is enabled
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.AddPaths.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "add-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('receive', YLeaf(YType.boolean, 'receive')),
                            ('send_max', YLeaf(YType.uint8, 'send-max')),
                            ('eligible_prefix_policy', YLeaf(YType.str, 'eligible-prefix-policy')),
                        ])
                        self.receive = None
                        self.send_max = None
                        self.eligible_prefix_policy = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.AddPaths.State, ['receive', 'send_max', 'eligible_prefix_policy'], name, value)


            class UseMultiplePaths(Entity):
                """
                Parameters related to the use of multiple\-paths for the same
                NLRI when they are received only from this neighbor
                
                .. attribute:: config
                
                	Configuration parameters relating to multipath
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Config>`
                
                .. attribute:: state
                
                	State parameters relating to multipath
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.State>`
                
                .. attribute:: ebgp
                
                	Multipath configuration for eBGP
                	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.UseMultiplePaths, self).__init__()

                    self.yang_name = "use-multiple-paths"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.UseMultiplePaths.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.UseMultiplePaths.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.UseMultiplePaths.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.ebgp = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp()
                    self.ebgp.parent = self
                    self._children_name_map["ebgp"] = "ebgp"
                    self._children_yang_names.add("ebgp")
                    self._segment_path = lambda: "use-multiple-paths"


                class Config(Entity):
                    """
                    Configuration parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.UseMultiplePaths.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ])
                        self.enabled = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.UseMultiplePaths.Config, ['enabled'], name, value)


                class State(Entity):
                    """
                    State parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.UseMultiplePaths.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ])
                        self.enabled = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.UseMultiplePaths.State, ['enabled'], name, value)


                class Ebgp(Entity):
                    """
                    Multipath configuration for eBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to eBGP multipath
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to eBGP multipath
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp, self).__init__()

                        self.yang_name = "ebgp"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ebgp"


                    class Config(Entity):
                        """
                        Configuration parameters relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ebgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                            ])
                            self.allow_multiple_as = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as'], name, value)


                    class State(Entity):
                        """
                        State information relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ebgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                            ])
                            self.allow_multiple_as = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State, ['allow_multiple_as'], name, value)


            class ApplyPolicy(Entity):
                """
                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                
                .. attribute:: config
                
                	Policy configuration data
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ApplyPolicy.Config>`
                
                .. attribute:: state
                
                	Operational state for routing policy
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.ApplyPolicy.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.ApplyPolicy, self).__init__()

                    self.yang_name = "apply-policy"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.ApplyPolicy.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.ApplyPolicy.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.Neighbors.Neighbor.ApplyPolicy.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.Neighbors.Neighbor.ApplyPolicy.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "apply-policy"


                class Config(Entity):
                    """
                    Policy configuration data.
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.ApplyPolicy.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "apply-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('import_policy', YLeafList(YType.str, 'import-policy')),
                            ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                            ('export_policy', YLeafList(YType.str, 'export-policy')),
                            ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                        ])
                        self.import_policy = []
                        self.default_import_policy = None
                        self.export_policy = []
                        self.default_export_policy = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                class State(Entity):
                    """
                    Operational state for routing policy
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.ApplyPolicy.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "apply-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('import_policy', YLeafList(YType.str, 'import-policy')),
                            ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                            ('export_policy', YLeafList(YType.str, 'export-policy')),
                            ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                        ])
                        self.import_policy = []
                        self.default_import_policy = None
                        self.export_policy = []
                        self.default_export_policy = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


            class AfiSafis(Entity):
                """
                Per\-address\-family configuration parameters associated with
                the neighbor
                
                .. attribute:: afi_safi
                
                	AFI,SAFI configuration available for the neighbour or group
                	**type**\: list of  		 :py:class:`AfiSafi <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.Neighbors.Neighbor.AfiSafis, self).__init__()

                    self.yang_name = "afi-safis"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("afi-safi", ("afi_safi", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi))])
                    self._leafs = OrderedDict()

                    self.afi_safi = YList(self)
                    self._segment_path = lambda: "afi-safis"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis, [], name, value)


                class AfiSafi(Entity):
                    """
                    AFI,SAFI configuration available for the
                    neighbour or group
                    
                    .. attribute:: afi_safi_name  (key)
                    
                    	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                    	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the AFI\-SAFI
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to the AFI\-SAFI
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State>`
                    
                    .. attribute:: graceful_restart
                    
                    	Parameters relating to BGP graceful\-restart
                    	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart>`
                    
                    .. attribute:: apply_policy
                    
                    	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                    	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy>`
                    
                    .. attribute:: ipv4_unicast
                    
                    	IPv4 unicast configuration options
                    	**type**\:  :py:class:`Ipv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast>`
                    
                    .. attribute:: ipv6_unicast
                    
                    	IPv6 unicast configuration options
                    	**type**\:  :py:class:`Ipv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast>`
                    
                    .. attribute:: ipv4_labeled_unicast
                    
                    	IPv4 Labeled Unicast configuration options
                    	**type**\:  :py:class:`Ipv4LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast>`
                    
                    .. attribute:: ipv6_labeled_unicast
                    
                    	IPv6 Labeled Unicast configuration options
                    	**type**\:  :py:class:`Ipv6LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast>`
                    
                    .. attribute:: l3vpn_ipv4_unicast
                    
                    	Unicast IPv4 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                    
                    .. attribute:: l3vpn_ipv6_unicast
                    
                    	Unicast IPv6 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                    
                    .. attribute:: l3vpn_ipv4_multicast
                    
                    	Multicast IPv4 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv4Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                    
                    .. attribute:: l3vpn_ipv6_multicast
                    
                    	Multicast IPv6 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv6Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                    
                    .. attribute:: l2vpn_vpls
                    
                    	BGP\-signalled VPLS configuration options
                    	**type**\:  :py:class:`L2VpnVpls <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls>`
                    
                    .. attribute:: l2vpn_evpn
                    
                    	BGP EVPN configuration options
                    	**type**\:  :py:class:`L2VpnEvpn <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn>`
                    
                    .. attribute:: use_multiple_paths
                    
                    	Parameters related to the use of multiple\-paths for the same NLRI when they are received only from this neighbor
                    	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi, self).__init__()

                        self.yang_name = "afi-safi"
                        self.yang_parent_name = "afi-safis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi_safi_name']
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State)), ("graceful-restart", ("graceful_restart", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart)), ("apply-policy", ("apply_policy", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy)), ("ipv4-unicast", ("ipv4_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast)), ("ipv6-unicast", ("ipv6_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast)), ("ipv4-labeled-unicast", ("ipv4_labeled_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast)), ("ipv6-labeled-unicast", ("ipv6_labeled_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast)), ("l3vpn-ipv4-unicast", ("l3vpn_ipv4_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast)), ("l3vpn-ipv6-unicast", ("l3vpn_ipv6_unicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast)), ("l3vpn-ipv4-multicast", ("l3vpn_ipv4_multicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast)), ("l3vpn-ipv6-multicast", ("l3vpn_ipv6_multicast", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast)), ("l2vpn-vpls", ("l2vpn_vpls", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls)), ("l2vpn-evpn", ("l2vpn_evpn", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn)), ("use-multiple-paths", ("use_multiple_paths", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                        ])
                        self.afi_safi_name = None

                        self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.graceful_restart = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart()
                        self.graceful_restart.parent = self
                        self._children_name_map["graceful_restart"] = "graceful-restart"
                        self._children_yang_names.add("graceful-restart")

                        self.apply_policy = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy()
                        self.apply_policy.parent = self
                        self._children_name_map["apply_policy"] = "apply-policy"
                        self._children_yang_names.add("apply-policy")

                        self.ipv4_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._children_yang_names.add("ipv4-unicast")

                        self.ipv6_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._children_yang_names.add("ipv6-unicast")

                        self.ipv4_labeled_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast()
                        self.ipv4_labeled_unicast.parent = self
                        self._children_name_map["ipv4_labeled_unicast"] = "ipv4-labeled-unicast"
                        self._children_yang_names.add("ipv4-labeled-unicast")

                        self.ipv6_labeled_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast()
                        self.ipv6_labeled_unicast.parent = self
                        self._children_name_map["ipv6_labeled_unicast"] = "ipv6-labeled-unicast"
                        self._children_yang_names.add("ipv6-labeled-unicast")

                        self.l3vpn_ipv4_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                        self.l3vpn_ipv4_unicast.parent = self
                        self._children_name_map["l3vpn_ipv4_unicast"] = "l3vpn-ipv4-unicast"
                        self._children_yang_names.add("l3vpn-ipv4-unicast")

                        self.l3vpn_ipv6_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                        self.l3vpn_ipv6_unicast.parent = self
                        self._children_name_map["l3vpn_ipv6_unicast"] = "l3vpn-ipv6-unicast"
                        self._children_yang_names.add("l3vpn-ipv6-unicast")

                        self.l3vpn_ipv4_multicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                        self.l3vpn_ipv4_multicast.parent = self
                        self._children_name_map["l3vpn_ipv4_multicast"] = "l3vpn-ipv4-multicast"
                        self._children_yang_names.add("l3vpn-ipv4-multicast")

                        self.l3vpn_ipv6_multicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                        self.l3vpn_ipv6_multicast.parent = self
                        self._children_name_map["l3vpn_ipv6_multicast"] = "l3vpn-ipv6-multicast"
                        self._children_yang_names.add("l3vpn-ipv6-multicast")

                        self.l2vpn_vpls = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls()
                        self.l2vpn_vpls.parent = self
                        self._children_name_map["l2vpn_vpls"] = "l2vpn-vpls"
                        self._children_yang_names.add("l2vpn-vpls")

                        self.l2vpn_evpn = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn()
                        self.l2vpn_evpn.parent = self
                        self._children_name_map["l2vpn_evpn"] = "l2vpn-evpn"
                        self._children_yang_names.add("l2vpn-evpn")

                        self.use_multiple_paths = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths()
                        self.use_multiple_paths.parent = self
                        self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
                        self._children_yang_names.add("use-multiple-paths")
                        self._segment_path = lambda: "afi-safi" + "[afi-safi-name='" + str(self.afi_safi_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi, ['afi_safi_name'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters for the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.afi_safi_name = None
                            self.enabled = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config, ['afi_safi_name', 'enabled'], name, value)


                    class State(Entity):
                        """
                        State information relating to the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: active
                        
                        	This value indicates whether a particular AFI\-SAFI has been succesfully negotiated with the peer. An AFI\-SAFI may be enabled in the current running configuration, but a session restart may be required in order to negotiate the new capability
                        	**type**\: bool
                        
                        .. attribute:: prefixes
                        
                        	Prefix counters for the BGP session
                        	**type**\:  :py:class:`Prefixes <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefixes", ("prefixes", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('active', YLeaf(YType.boolean, 'active')),
                            ])
                            self.afi_safi_name = None
                            self.enabled = None
                            self.active = None

                            self.prefixes = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"
                            self._children_yang_names.add("prefixes")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State, ['afi_safi_name', 'enabled', 'active'], name, value)


                        class Prefixes(Entity):
                            """
                            Prefix counters for the BGP session
                            
                            .. attribute:: received
                            
                            	The number of prefixes received from the neighbor
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sent
                            
                            	The number of prefixes advertised to the neighbor
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: installed
                            
                            	The number of advertised prefixes installed in the Loc\-RIB
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes, self).__init__()

                                self.yang_name = "prefixes"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received', YLeaf(YType.uint32, 'received')),
                                    ('sent', YLeaf(YType.uint32, 'sent')),
                                    ('installed', YLeaf(YType.uint32, 'installed')),
                                ])
                                self.received = None
                                self.sent = None
                                self.installed = None
                                self._segment_path = lambda: "prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes, ['received', 'sent', 'installed'], name, value)


                    class GracefulRestart(Entity):
                        """
                        Parameters relating to BGP graceful\-restart
                        
                        .. attribute:: config
                        
                        	Configuration options for BGP graceful\-restart
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config>`
                        
                        .. attribute:: state
                        
                        	State information for BGP graceful\-restart
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart, self).__init__()

                            self.yang_name = "graceful-restart"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "graceful-restart"


                        class Config(Entity):
                            """
                            Configuration options for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "graceful-restart"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config, ['enabled'], name, value)


                        class State(Entity):
                            """
                            State information for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: received
                            
                            	This leaf indicates whether the neighbor advertised the ability to support graceful\-restart for this AFI\-SAFI
                            	**type**\: bool
                            
                            .. attribute:: advertised
                            
                            	This leaf indicates whether the ability to support graceful\-restart has been advertised to the peer
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "graceful-restart"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                    ('received', YLeaf(YType.boolean, 'received')),
                                    ('advertised', YLeaf(YType.boolean, 'advertised')),
                                ])
                                self.enabled = None
                                self.received = None
                                self.advertised = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State, ['enabled', 'received', 'advertised'], name, value)


                    class ApplyPolicy(Entity):
                        """
                        Anchor point for routing policies in the model.
                        Import and export policies are with respect to the local
                        routing table, i.e., export (send) and import (receive),
                        depending on the context.
                        
                        .. attribute:: config
                        
                        	Policy configuration data
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for routing policy
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy, self).__init__()

                            self.yang_name = "apply-policy"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "apply-policy"


                        class Config(Entity):
                            """
                            Policy configuration data.
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "apply-policy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('import_policy', YLeafList(YType.str, 'import-policy')),
                                    ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                    ('export_policy', YLeafList(YType.str, 'export-policy')),
                                    ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                                ])
                                self.import_policy = []
                                self.default_import_policy = None
                                self.export_policy = []
                                self.default_export_policy = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                        class State(Entity):
                            """
                            Operational state for routing policy
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "apply-policy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('import_policy', YLeafList(YType.str, 'import-policy')),
                                    ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                    ('export_policy', YLeafList(YType.str, 'export-policy')),
                                    ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                                ])
                                self.import_policy = []
                                self.default_import_policy = None
                                self.export_policy = []
                                self.default_export_policy = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                    class Ipv4Unicast(Entity):
                        """
                        IPv4 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast, self).__init__()

                            self.yang_name = "ipv4-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit)), ("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")

                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ipv4-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config, ['send_default_route'], name, value)


                        class State(Entity):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State, ['send_default_route'], name, value)


                    class Ipv6Unicast(Entity):
                        """
                        IPv6 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast, self).__init__()

                            self.yang_name = "ipv6-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit)), ("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")

                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ipv6-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config, ['send_default_route'], name, value)


                        class State(Entity):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State, ['send_default_route'], name, value)


                    class Ipv4LabeledUnicast(Entity):
                        """
                        IPv4 Labeled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast, self).__init__()

                            self.yang_name = "ipv4-labeled-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "ipv4-labeled-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv4-labeled-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class Ipv6LabeledUnicast(Entity):
                        """
                        IPv6 Labeled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast, self).__init__()

                            self.yang_name = "ipv6-labeled-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "ipv6-labeled-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv6-labeled-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv4Unicast(Entity):
                        """
                        Unicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast, self).__init__()

                            self.yang_name = "l3vpn-ipv4-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv4-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv6Unicast(Entity):
                        """
                        Unicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast, self).__init__()

                            self.yang_name = "l3vpn-ipv6-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv6-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv4Multicast(Entity):
                        """
                        Multicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast, self).__init__()

                            self.yang_name = "l3vpn-ipv4-multicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv4-multicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv4-multicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv6Multicast(Entity):
                        """
                        Multicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast, self).__init__()

                            self.yang_name = "l3vpn-ipv6-multicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv6-multicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv6-multicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L2VpnVpls(Entity):
                        """
                        BGP\-signalled VPLS configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls, self).__init__()

                            self.yang_name = "l2vpn-vpls"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l2vpn-vpls"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l2vpn-vpls"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L2VpnEvpn(Entity):
                        """
                        BGP EVPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn, self).__init__()

                            self.yang_name = "l2vpn-evpn"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l2vpn-evpn"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l2vpn-evpn"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class UseMultiplePaths(Entity):
                        """
                        Parameters related to the use of multiple\-paths for the same
                        NLRI when they are received only from this neighbor
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to multipath
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to multipath
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                        
                        .. attribute:: ebgp
                        
                        	Multipath configuration for eBGP
                        	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths, self).__init__()

                            self.yang_name = "use-multiple-paths"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.ebgp = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                            self.ebgp.parent = self
                            self._children_name_map["ebgp"] = "ebgp"
                            self._children_yang_names.add("ebgp")
                            self._segment_path = lambda: "use-multiple-paths"


                        class Config(Entity):
                            """
                            Configuration parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config, ['enabled'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State, ['enabled'], name, value)


                        class Ebgp(Entity):
                            """
                            Multipath configuration for eBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to eBGP multipath
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to eBGP multipath
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp, self).__init__()

                                self.yang_name = "ebgp"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "ebgp"


                            class Config(Entity):
                                """
                                Configuration parameters relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "ebgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                    ])
                                    self.allow_multiple_as = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as'], name, value)


                            class State(Entity):
                                """
                                State information relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "ebgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                    ])
                                    self.allow_multiple_as = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, ['allow_multiple_as'], name, value)


    class PeerGroups(Entity):
        """
        Configuration for BGP peer\-groups
        
        .. attribute:: peer_group
        
        	List of BGP peer\-groups configured on the local system \- uniquely identified by peer\-group name
        	**type**\: list of  		 :py:class:`PeerGroup <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup>`
        
        

        """

        _prefix = 'oc-bgp'
        _revision = '2016-06-21'

        def __init__(self):
            super(Bgp.PeerGroups, self).__init__()

            self.yang_name = "peer-groups"
            self.yang_parent_name = "bgp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("peer-group", ("peer_group", Bgp.PeerGroups.PeerGroup))])
            self._leafs = OrderedDict()

            self.peer_group = YList(self)
            self._segment_path = lambda: "peer-groups"
            self._absolute_path = lambda: "openconfig-bgp:bgp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Bgp.PeerGroups, [], name, value)


        class PeerGroup(Entity):
            """
            List of BGP peer\-groups configured on the local system \-
            uniquely identified by peer\-group name
            
            .. attribute:: peer_group_name  (key)
            
            	Reference to the name of the BGP peer\-group used as a key in the peer\-group list
            	**type**\: str
            
            	**refers to**\:  :py:class:`peer_group_name <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Config>`
            
            .. attribute:: config
            
            	Configuration parameters relating to the BGP neighbor or group
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP peer\-group
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.State>`
            
            .. attribute:: timers
            
            	Timers related to a BGP peer\-group
            	**type**\:  :py:class:`Timers <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Timers>`
            
            .. attribute:: transport
            
            	Transport session parameters for the BGP peer\-group
            	**type**\:  :py:class:`Transport <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Transport>`
            
            .. attribute:: error_handling
            
            	Error handling parameters used for the BGP peer\-group
            	**type**\:  :py:class:`ErrorHandling <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling>`
            
            .. attribute:: graceful_restart
            
            	Parameters relating the graceful restart mechanism for BGP
            	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart>`
            
            .. attribute:: logging_options
            
            	Logging options for events related to the BGP neighbor or group
            	**type**\:  :py:class:`LoggingOptions <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions>`
            
            .. attribute:: ebgp_multihop
            
            	eBGP multi\-hop parameters for the BGPgroup
            	**type**\:  :py:class:`EbgpMultihop <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop>`
            
            .. attribute:: route_reflector
            
            	Route reflector parameters for the BGPgroup
            	**type**\:  :py:class:`RouteReflector <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.RouteReflector>`
            
            .. attribute:: as_path_options
            
            	AS\_PATH manipulation parameters for the BGP neighbor or group
            	**type**\:  :py:class:`AsPathOptions <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions>`
            
            .. attribute:: add_paths
            
            	Parameters relating to the advertisement and receipt of multiple paths for a single NLRI (add\-paths)
            	**type**\:  :py:class:`AddPaths <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AddPaths>`
            
            .. attribute:: use_multiple_paths
            
            	Parameters related to the use of multiple paths for the same NLRI
            	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths>`
            
            .. attribute:: apply_policy
            
            	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
            	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy>`
            
            .. attribute:: afi_safis
            
            	Per\-address\-family configuration parameters associated with thegroup
            	**type**\:  :py:class:`AfiSafis <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis>`
            
            

            """

            _prefix = 'oc-bgp'
            _revision = '2016-06-21'

            def __init__(self):
                super(Bgp.PeerGroups.PeerGroup, self).__init__()

                self.yang_name = "peer-group"
                self.yang_parent_name = "peer-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_group_name']
                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.State)), ("timers", ("timers", Bgp.PeerGroups.PeerGroup.Timers)), ("transport", ("transport", Bgp.PeerGroups.PeerGroup.Transport)), ("error-handling", ("error_handling", Bgp.PeerGroups.PeerGroup.ErrorHandling)), ("graceful-restart", ("graceful_restart", Bgp.PeerGroups.PeerGroup.GracefulRestart)), ("logging-options", ("logging_options", Bgp.PeerGroups.PeerGroup.LoggingOptions)), ("ebgp-multihop", ("ebgp_multihop", Bgp.PeerGroups.PeerGroup.EbgpMultihop)), ("route-reflector", ("route_reflector", Bgp.PeerGroups.PeerGroup.RouteReflector)), ("as-path-options", ("as_path_options", Bgp.PeerGroups.PeerGroup.AsPathOptions)), ("add-paths", ("add_paths", Bgp.PeerGroups.PeerGroup.AddPaths)), ("use-multiple-paths", ("use_multiple_paths", Bgp.PeerGroups.PeerGroup.UseMultiplePaths)), ("apply-policy", ("apply_policy", Bgp.PeerGroups.PeerGroup.ApplyPolicy)), ("afi-safis", ("afi_safis", Bgp.PeerGroups.PeerGroup.AfiSafis))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('peer_group_name', YLeaf(YType.str, 'peer-group-name')),
                ])
                self.peer_group_name = None

                self.config = Bgp.PeerGroups.PeerGroup.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Bgp.PeerGroups.PeerGroup.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.timers = Bgp.PeerGroups.PeerGroup.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")

                self.transport = Bgp.PeerGroups.PeerGroup.Transport()
                self.transport.parent = self
                self._children_name_map["transport"] = "transport"
                self._children_yang_names.add("transport")

                self.error_handling = Bgp.PeerGroups.PeerGroup.ErrorHandling()
                self.error_handling.parent = self
                self._children_name_map["error_handling"] = "error-handling"
                self._children_yang_names.add("error-handling")

                self.graceful_restart = Bgp.PeerGroups.PeerGroup.GracefulRestart()
                self.graceful_restart.parent = self
                self._children_name_map["graceful_restart"] = "graceful-restart"
                self._children_yang_names.add("graceful-restart")

                self.logging_options = Bgp.PeerGroups.PeerGroup.LoggingOptions()
                self.logging_options.parent = self
                self._children_name_map["logging_options"] = "logging-options"
                self._children_yang_names.add("logging-options")

                self.ebgp_multihop = Bgp.PeerGroups.PeerGroup.EbgpMultihop()
                self.ebgp_multihop.parent = self
                self._children_name_map["ebgp_multihop"] = "ebgp-multihop"
                self._children_yang_names.add("ebgp-multihop")

                self.route_reflector = Bgp.PeerGroups.PeerGroup.RouteReflector()
                self.route_reflector.parent = self
                self._children_name_map["route_reflector"] = "route-reflector"
                self._children_yang_names.add("route-reflector")

                self.as_path_options = Bgp.PeerGroups.PeerGroup.AsPathOptions()
                self.as_path_options.parent = self
                self._children_name_map["as_path_options"] = "as-path-options"
                self._children_yang_names.add("as-path-options")

                self.add_paths = Bgp.PeerGroups.PeerGroup.AddPaths()
                self.add_paths.parent = self
                self._children_name_map["add_paths"] = "add-paths"
                self._children_yang_names.add("add-paths")

                self.use_multiple_paths = Bgp.PeerGroups.PeerGroup.UseMultiplePaths()
                self.use_multiple_paths.parent = self
                self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
                self._children_yang_names.add("use-multiple-paths")

                self.apply_policy = Bgp.PeerGroups.PeerGroup.ApplyPolicy()
                self.apply_policy.parent = self
                self._children_name_map["apply_policy"] = "apply-policy"
                self._children_yang_names.add("apply-policy")

                self.afi_safis = Bgp.PeerGroups.PeerGroup.AfiSafis()
                self.afi_safis.parent = self
                self._children_name_map["afi_safis"] = "afi-safis"
                self._children_yang_names.add("afi-safis")
                self._segment_path = lambda: "peer-group" + "[peer-group-name='" + str(self.peer_group_name) + "']"
                self._absolute_path = lambda: "openconfig-bgp:bgp/peer-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Bgp.PeerGroups.PeerGroup, ['peer_group_name'], name, value)


            class Config(Entity):
                """
                Configuration parameters relating to the BGP neighbor or
                group
                
                .. attribute:: peer_group_name
                
                	Name of the BGP peer\-group
                	**type**\: str
                
                .. attribute:: peer_as
                
                	AS number of the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_as
                
                	The local autonomous system number that is to be used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_type
                
                	Explicitly designate the peer or peer group as internal (iBGP) or external (eBGP)
                	**type**\:  :py:class:`PeerType <ydk.models.openconfig.openconfig_bgp_types.PeerType>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers \- when this leaf is not specified, the AS\_PATH attribute should be sent to the peer unchanged
                	**type**\:  :py:class:`REMOVEPRIVATEASOPTION <ydk.models.openconfig.openconfig_bgp_types.REMOVEPRIVATEASOPTION>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\:  :py:class:`CommunityType <ydk.models.openconfig.openconfig_bgp_types.CommunityType>`
                
                	**default value**\: NONE
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_group_name', YLeaf(YType.str, 'peer-group-name')),
                        ('peer_as', YLeaf(YType.uint32, 'peer-as')),
                        ('local_as', YLeaf(YType.uint32, 'local-as')),
                        ('peer_type', YLeaf(YType.enumeration, 'peer-type')),
                        ('auth_password', YLeaf(YType.str, 'auth-password')),
                        ('remove_private_as', YLeaf(YType.identityref, 'remove-private-as')),
                        ('route_flap_damping', YLeaf(YType.boolean, 'route-flap-damping')),
                        ('send_community', YLeaf(YType.enumeration, 'send-community')),
                        ('description', YLeaf(YType.str, 'description')),
                    ])
                    self.peer_group_name = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.Config, ['peer_group_name', 'peer_as', 'local_as', 'peer_type', 'auth_password', 'remove_private_as', 'route_flap_damping', 'send_community', 'description'], name, value)


            class State(Entity):
                """
                State information relating to the BGP peer\-group
                
                .. attribute:: peer_group_name
                
                	Name of the BGP peer\-group
                	**type**\: str
                
                .. attribute:: peer_as
                
                	AS number of the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_as
                
                	The local autonomous system number that is to be used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_type
                
                	Explicitly designate the peer or peer group as internal (iBGP) or external (eBGP)
                	**type**\:  :py:class:`PeerType <ydk.models.openconfig.openconfig_bgp_types.PeerType>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers \- when this leaf is not specified, the AS\_PATH attribute should be sent to the peer unchanged
                	**type**\:  :py:class:`REMOVEPRIVATEASOPTION <ydk.models.openconfig.openconfig_bgp_types.REMOVEPRIVATEASOPTION>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\:  :py:class:`CommunityType <ydk.models.openconfig.openconfig_bgp_types.CommunityType>`
                
                	**default value**\: NONE
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: total_paths
                
                	Total number of BGP paths within the context
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_prefixes
                
                	Total number of BGP prefixes received within the context
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_group_name', YLeaf(YType.str, 'peer-group-name')),
                        ('peer_as', YLeaf(YType.uint32, 'peer-as')),
                        ('local_as', YLeaf(YType.uint32, 'local-as')),
                        ('peer_type', YLeaf(YType.enumeration, 'peer-type')),
                        ('auth_password', YLeaf(YType.str, 'auth-password')),
                        ('remove_private_as', YLeaf(YType.identityref, 'remove-private-as')),
                        ('route_flap_damping', YLeaf(YType.boolean, 'route-flap-damping')),
                        ('send_community', YLeaf(YType.enumeration, 'send-community')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('total_paths', YLeaf(YType.uint32, 'total-paths')),
                        ('total_prefixes', YLeaf(YType.uint32, 'total-prefixes')),
                    ])
                    self.peer_group_name = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.total_paths = None
                    self.total_prefixes = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.State, ['peer_group_name', 'peer_as', 'local_as', 'peer_type', 'auth_password', 'remove_private_as', 'route_flap_damping', 'send_community', 'description', 'total_paths', 'total_prefixes'], name, value)


            class Timers(Entity):
                """
                Timers related to a BGP peer\-group
                
                .. attribute:: config
                
                	Configuration parameters relating to timers used for the BGP neighbor or peer group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Timers.Config>`
                
                .. attribute:: state
                
                	State information relating to the timers used for the BGP group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Timers.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.Timers.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.Timers.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.Timers.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.Timers.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "timers"


                class Config(Entity):
                    """
                    Configuration parameters relating to timers used for the
                    BGP neighbor or peer group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 90
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.Timers.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('connect_retry', YLeaf(YType.str, 'connect-retry')),
                            ('hold_time', YLeaf(YType.str, 'hold-time')),
                            ('keepalive_interval', YLeaf(YType.str, 'keepalive-interval')),
                            ('minimum_advertisement_interval', YLeaf(YType.str, 'minimum-advertisement-interval')),
                        ])
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.Timers.Config, ['connect_retry', 'hold_time', 'keepalive_interval', 'minimum_advertisement_interval'], name, value)


                class State(Entity):
                    """
                    State information relating to the timers used for the BGP
                    group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 90
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**default value**\: 30
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.Timers.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('connect_retry', YLeaf(YType.str, 'connect-retry')),
                            ('hold_time', YLeaf(YType.str, 'hold-time')),
                            ('keepalive_interval', YLeaf(YType.str, 'keepalive-interval')),
                            ('minimum_advertisement_interval', YLeaf(YType.str, 'minimum-advertisement-interval')),
                        ])
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.Timers.State, ['connect_retry', 'hold_time', 'keepalive_interval', 'minimum_advertisement_interval'], name, value)


            class Transport(Entity):
                """
                Transport session parameters for the BGP peer\-group
                
                .. attribute:: config
                
                	Configuration parameters relating to the transport session(s) used for the BGP neighbor or group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Transport.Config>`
                
                .. attribute:: state
                
                	State information relating to the transport session(s) used for the BGP neighbor or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.Transport.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.Transport.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.Transport.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.Transport.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.Transport.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "transport"


                class Config(Entity):
                    """
                    Configuration parameters relating to the transport
                    session(s) used for the BGP neighbor or group
                    
                    .. attribute:: tcp_mss
                    
                    	Sets the max segment size for BGP TCP sessions
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mtu_discovery
                    
                    	Turns path mtu discovery for BGP TCP sessions on (true) or off (false)
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.Transport.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "transport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_mss', YLeaf(YType.uint16, 'tcp-mss')),
                            ('mtu_discovery', YLeaf(YType.boolean, 'mtu-discovery')),
                            ('passive_mode', YLeaf(YType.boolean, 'passive-mode')),
                            ('local_address', YLeaf(YType.str, 'local-address')),
                        ])
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.Transport.Config, ['tcp_mss', 'mtu_discovery', 'passive_mode', 'local_address'], name, value)


                class State(Entity):
                    """
                    State information relating to the transport session(s)
                    used for the BGP neighbor or group
                    
                    .. attribute:: tcp_mss
                    
                    	Sets the max segment size for BGP TCP sessions
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: mtu_discovery
                    
                    	Turns path mtu discovery for BGP TCP sessions on (true) or off (false)
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.Transport.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "transport"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_mss', YLeaf(YType.uint16, 'tcp-mss')),
                            ('mtu_discovery', YLeaf(YType.boolean, 'mtu-discovery')),
                            ('passive_mode', YLeaf(YType.boolean, 'passive-mode')),
                            ('local_address', YLeaf(YType.str, 'local-address')),
                        ])
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.Transport.State, ['tcp_mss', 'mtu_discovery', 'passive_mode', 'local_address'], name, value)


            class ErrorHandling(Entity):
                """
                Error handling parameters used for the BGP peer\-group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying the behavior or enhanced error handling mechanisms for the BGP group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling.Config>`
                
                .. attribute:: state
                
                	State information relating to enhanced error handling mechanisms for the BGP group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.ErrorHandling, self).__init__()

                    self.yang_name = "error-handling"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.ErrorHandling.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.ErrorHandling.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.ErrorHandling.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.ErrorHandling.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "error-handling"


                class Config(Entity):
                    """
                    Configuration parameters enabling or modifying the
                    behavior or enhanced error handling mechanisms for the BGP
                    group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.ErrorHandling.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "error-handling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('treat_as_withdraw', YLeaf(YType.boolean, 'treat-as-withdraw')),
                        ])
                        self.treat_as_withdraw = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.ErrorHandling.Config, ['treat_as_withdraw'], name, value)


                class State(Entity):
                    """
                    State information relating to enhanced error handling
                    mechanisms for the BGP group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.ErrorHandling.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "error-handling"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('treat_as_withdraw', YLeaf(YType.boolean, 'treat-as-withdraw')),
                        ])
                        self.treat_as_withdraw = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.ErrorHandling.State, ['treat_as_withdraw'], name, value)


            class GracefulRestart(Entity):
                """
                Parameters relating the graceful restart mechanism for BGP
                
                .. attribute:: config
                
                	Configuration parameters relating to graceful\-restart
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart.Config>`
                
                .. attribute:: state
                
                	State information associated with graceful\-restart
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.GracefulRestart, self).__init__()

                    self.yang_name = "graceful-restart"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.GracefulRestart.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.GracefulRestart.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.GracefulRestart.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.GracefulRestart.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "graceful-restart"


                class Config(Entity):
                    """
                    Configuration parameters relating to graceful\-restart
                    
                    .. attribute:: enabled
                    
                    	Enable or disable the graceful\-restart capability
                    	**type**\: bool
                    
                    .. attribute:: restart_time
                    
                    	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: stale_routes_time
                    
                    	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.GracefulRestart.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "graceful-restart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                            ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                            ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                        ])
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.GracefulRestart.Config, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only'], name, value)


                class State(Entity):
                    """
                    State information associated with graceful\-restart
                    
                    .. attribute:: enabled
                    
                    	Enable or disable the graceful\-restart capability
                    	**type**\: bool
                    
                    .. attribute:: restart_time
                    
                    	Estimated time (in seconds) for the local BGP speaker to restart a session. This value is advertise in the graceful restart BGP capability.  This is a 12\-bit value, referred to as Restart Time in RFC4724.  Per RFC4724, the suggested default value is <= the hold\-time value
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: stale_routes_time
                    
                    	An upper\-bound on the time thate stale routes will be retained by a router after a session is restarted. If an End\-of\-RIB (EOR) marker is received prior to this timer expiring stale\-routes will be flushed upon its receipt \- if no EOR is received, then when this timer expires stale paths will be purged. This timer is referred to as the Selection\_Deferral\_Timer in RFC4724
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.GracefulRestart.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "graceful-restart"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('restart_time', YLeaf(YType.uint16, 'restart-time')),
                            ('stale_routes_time', YLeaf(YType.str, 'stale-routes-time')),
                            ('helper_only', YLeaf(YType.boolean, 'helper-only')),
                        ])
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.GracefulRestart.State, ['enabled', 'restart_time', 'stale_routes_time', 'helper_only'], name, value)


            class LoggingOptions(Entity):
                """
                Logging options for events related to the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying logging for events relating to the BGPgroup
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to logging for the BGP neighbor or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.LoggingOptions, self).__init__()

                    self.yang_name = "logging-options"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.LoggingOptions.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.LoggingOptions.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.LoggingOptions.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.LoggingOptions.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "logging-options"


                class Config(Entity):
                    """
                    Configuration parameters enabling or modifying logging
                    for events relating to the BGPgroup
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.LoggingOptions.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "logging-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_neighbor_state_changes', YLeaf(YType.boolean, 'log-neighbor-state-changes')),
                        ])
                        self.log_neighbor_state_changes = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.LoggingOptions.Config, ['log_neighbor_state_changes'], name, value)


                class State(Entity):
                    """
                    State information relating to logging for the BGP neighbor
                    or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.LoggingOptions.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "logging-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('log_neighbor_state_changes', YLeaf(YType.boolean, 'log-neighbor-state-changes')),
                        ])
                        self.log_neighbor_state_changes = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.LoggingOptions.State, ['log_neighbor_state_changes'], name, value)


            class EbgpMultihop(Entity):
                """
                eBGP multi\-hop parameters for the BGPgroup
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multihop for the BGP group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config>`
                
                .. attribute:: state
                
                	State information for eBGP multihop, for the BGP neighbor or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.EbgpMultihop, self).__init__()

                    self.yang_name = "ebgp-multihop"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.EbgpMultihop.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.EbgpMultihop.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "ebgp-multihop"


                class Config(Entity):
                    """
                    Configuration parameters relating to eBGP multihop for the
                    BGP group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ebgp-multihop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('multihop_ttl', YLeaf(YType.uint8, 'multihop-ttl')),
                        ])
                        self.enabled = None
                        self.multihop_ttl = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config, ['enabled', 'multihop_ttl'], name, value)


                class State(Entity):
                    """
                    State information for eBGP multihop, for the BGP neighbor
                    or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.EbgpMultihop.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ebgp-multihop"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('multihop_ttl', YLeaf(YType.uint8, 'multihop-ttl')),
                        ])
                        self.enabled = None
                        self.multihop_ttl = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.EbgpMultihop.State, ['enabled', 'multihop_ttl'], name, value)


            class RouteReflector(Entity):
                """
                Route reflector parameters for the BGPgroup
                
                .. attribute:: config
                
                	Configuraton parameters relating to route reflection for the BGPgroup
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.RouteReflector.Config>`
                
                .. attribute:: state
                
                	State information relating to route reflection for the BGPgroup
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.RouteReflector.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.RouteReflector, self).__init__()

                    self.yang_name = "route-reflector"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.RouteReflector.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.RouteReflector.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.RouteReflector.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.RouteReflector.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "route-reflector"


                class Config(Entity):
                    """
                    Configuraton parameters relating to route reflection
                    for the BGPgroup
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.RouteReflector.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "route-reflector"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_reflector_cluster_id', YLeaf(YType.str, 'route-reflector-cluster-id')),
                            ('route_reflector_client', YLeaf(YType.boolean, 'route-reflector-client')),
                        ])
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.RouteReflector.Config, ['route_reflector_cluster_id', 'route_reflector_client'], name, value)


                class State(Entity):
                    """
                    State information relating to route reflection for the
                    BGPgroup
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.RouteReflector.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "route-reflector"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_reflector_cluster_id', YLeaf(YType.str, 'route-reflector-cluster-id')),
                            ('route_reflector_client', YLeaf(YType.boolean, 'route-reflector-client')),
                        ])
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.RouteReflector.State, ['route_reflector_cluster_id', 'route_reflector_client'], name, value)


            class AsPathOptions(Entity):
                """
                AS\_PATH manipulation parameters for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters relating to AS\_PATH manipulation for the BGP peer or group
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to the AS\_PATH manipulation mechanisms for the BGP peer or group
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.AsPathOptions, self).__init__()

                    self.yang_name = "as-path-options"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AsPathOptions.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AsPathOptions.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.AsPathOptions.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.AsPathOptions.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "as-path-options"


                class Config(Entity):
                    """
                    Configuration parameters relating to AS\_PATH manipulation
                    for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**default value**\: 0
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.AsPathOptions.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "as-path-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_own_as', YLeaf(YType.uint8, 'allow-own-as')),
                            ('replace_peer_as', YLeaf(YType.boolean, 'replace-peer-as')),
                        ])
                        self.allow_own_as = None
                        self.replace_peer_as = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.AsPathOptions.Config, ['allow_own_as', 'replace_peer_as'], name, value)


                class State(Entity):
                    """
                    State information relating to the AS\_PATH manipulation
                    mechanisms for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**default value**\: 0
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.AsPathOptions.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "as-path-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('allow_own_as', YLeaf(YType.uint8, 'allow-own-as')),
                            ('replace_peer_as', YLeaf(YType.boolean, 'replace-peer-as')),
                        ])
                        self.allow_own_as = None
                        self.replace_peer_as = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.AsPathOptions.State, ['allow_own_as', 'replace_peer_as'], name, value)


            class AddPaths(Entity):
                """
                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add\-paths)
                
                .. attribute:: config
                
                	Configuration parameters relating to ADD\_PATHS
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AddPaths.Config>`
                
                .. attribute:: state
                
                	State information associated with ADD\_PATHS
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AddPaths.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.AddPaths, self).__init__()

                    self.yang_name = "add-paths"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AddPaths.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AddPaths.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.AddPaths.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.AddPaths.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "add-paths"


                class Config(Entity):
                    """
                    Configuration parameters relating to ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: eligible_prefix_policy
                    
                    	A reference to a routing policy which can be used to restrict the prefixes for which add\-paths is enabled
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.AddPaths.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "add-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('receive', YLeaf(YType.boolean, 'receive')),
                            ('send_max', YLeaf(YType.uint8, 'send-max')),
                            ('eligible_prefix_policy', YLeaf(YType.str, 'eligible-prefix-policy')),
                        ])
                        self.receive = None
                        self.send_max = None
                        self.eligible_prefix_policy = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.AddPaths.Config, ['receive', 'send_max', 'eligible_prefix_policy'], name, value)


                class State(Entity):
                    """
                    State information associated with ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: eligible_prefix_policy
                    
                    	A reference to a routing policy which can be used to restrict the prefixes for which add\-paths is enabled
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.AddPaths.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "add-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('receive', YLeaf(YType.boolean, 'receive')),
                            ('send_max', YLeaf(YType.uint8, 'send-max')),
                            ('eligible_prefix_policy', YLeaf(YType.str, 'eligible-prefix-policy')),
                        ])
                        self.receive = None
                        self.send_max = None
                        self.eligible_prefix_policy = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.AddPaths.State, ['receive', 'send_max', 'eligible_prefix_policy'], name, value)


            class UseMultiplePaths(Entity):
                """
                Parameters related to the use of multiple paths for the
                same NLRI
                
                .. attribute:: config
                
                	Configuration parameters relating to multipath
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config>`
                
                .. attribute:: state
                
                	State parameters relating to multipath
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State>`
                
                .. attribute:: ebgp
                
                	Multipath parameters for eBGP
                	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp>`
                
                .. attribute:: ibgp
                
                	Multipath parameters for iBGP
                	**type**\:  :py:class:`Ibgp <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths, self).__init__()

                    self.yang_name = "use-multiple-paths"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp)), ("ibgp", ("ibgp", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.ebgp = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp()
                    self.ebgp.parent = self
                    self._children_name_map["ebgp"] = "ebgp"
                    self._children_yang_names.add("ebgp")

                    self.ibgp = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp()
                    self.ibgp.parent = self
                    self._children_name_map["ibgp"] = "ibgp"
                    self._children_yang_names.add("ibgp")
                    self._segment_path = lambda: "use-multiple-paths"


                class Config(Entity):
                    """
                    Configuration parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ])
                        self.enabled = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config, ['enabled'], name, value)


                class State(Entity):
                    """
                    State parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                        ])
                        self.enabled = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State, ['enabled'], name, value)


                class Ebgp(Entity):
                    """
                    Multipath parameters for eBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to eBGP multipath
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to eBGP multipath
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp, self).__init__()

                        self.yang_name = "ebgp"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ebgp"


                    class Config(Entity):
                        """
                        Configuration parameters relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ebgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                            ])
                            self.allow_multiple_as = None
                            self.maximum_paths = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as', 'maximum_paths'], name, value)


                    class State(Entity):
                        """
                        State information relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ebgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                            ])
                            self.allow_multiple_as = None
                            self.maximum_paths = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State, ['allow_multiple_as', 'maximum_paths'], name, value)


                class Ibgp(Entity):
                    """
                    Multipath parameters for iBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to iBGP multipath
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to iBGP multipath
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp, self).__init__()

                        self.yang_name = "ibgp"
                        self.yang_parent_name = "use-multiple-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ibgp"


                    class Config(Entity):
                        """
                        Configuration parameters relating to iBGP multipath
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ibgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                            ])
                            self.maximum_paths = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config, ['maximum_paths'], name, value)


                    class State(Entity):
                        """
                        State information relating to iBGP multipath
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ibgp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                            ])
                            self.maximum_paths = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State, ['maximum_paths'], name, value)


            class ApplyPolicy(Entity):
                """
                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                
                .. attribute:: config
                
                	Policy configuration data
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config>`
                
                .. attribute:: state
                
                	Operational state for routing policy
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy.State>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.ApplyPolicy, self).__init__()

                    self.yang_name = "apply-policy"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.ApplyPolicy.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config = Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Bgp.PeerGroups.PeerGroup.ApplyPolicy.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "apply-policy"


                class Config(Entity):
                    """
                    Policy configuration data.
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "apply-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('import_policy', YLeafList(YType.str, 'import-policy')),
                            ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                            ('export_policy', YLeafList(YType.str, 'export-policy')),
                            ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                        ])
                        self.import_policy = []
                        self.default_import_policy = None
                        self.export_policy = []
                        self.default_export_policy = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                class State(Entity):
                    """
                    Operational state for routing policy
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                    
                    	**default value**\: REJECT_ROUTE
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.ApplyPolicy.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "apply-policy"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('import_policy', YLeafList(YType.str, 'import-policy')),
                            ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                            ('export_policy', YLeafList(YType.str, 'export-policy')),
                            ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                        ])
                        self.import_policy = []
                        self.default_import_policy = None
                        self.export_policy = []
                        self.default_export_policy = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


            class AfiSafis(Entity):
                """
                Per\-address\-family configuration parameters associated with
                thegroup
                
                .. attribute:: afi_safi
                
                	AFI,SAFI configuration available for the neighbour or group
                	**type**\: list of  		 :py:class:`AfiSafi <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi>`
                
                

                """

                _prefix = 'oc-bgp'
                _revision = '2016-06-21'

                def __init__(self):
                    super(Bgp.PeerGroups.PeerGroup.AfiSafis, self).__init__()

                    self.yang_name = "afi-safis"
                    self.yang_parent_name = "peer-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("afi-safi", ("afi_safi", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi))])
                    self._leafs = OrderedDict()

                    self.afi_safi = YList(self)
                    self._segment_path = lambda: "afi-safis"

                def __setattr__(self, name, value):
                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis, [], name, value)


                class AfiSafi(Entity):
                    """
                    AFI,SAFI configuration available for the
                    neighbour or group
                    
                    .. attribute:: afi_safi_name  (key)
                    
                    	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                    	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the AFI\-SAFI
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to the AFI\-SAFI
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State>`
                    
                    .. attribute:: graceful_restart
                    
                    	Parameters relating to BGP graceful\-restart
                    	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart>`
                    
                    .. attribute:: route_selection_options
                    
                    	Parameters relating to options for route selection
                    	**type**\:  :py:class:`RouteSelectionOptions <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions>`
                    
                    .. attribute:: use_multiple_paths
                    
                    	Parameters related to the use of multiple paths for the same NLRI
                    	**type**\:  :py:class:`UseMultiplePaths <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths>`
                    
                    .. attribute:: apply_policy
                    
                    	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                    	**type**\:  :py:class:`ApplyPolicy <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy>`
                    
                    .. attribute:: ipv4_unicast
                    
                    	IPv4 unicast configuration options
                    	**type**\:  :py:class:`Ipv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast>`
                    
                    .. attribute:: ipv6_unicast
                    
                    	IPv6 unicast configuration options
                    	**type**\:  :py:class:`Ipv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast>`
                    
                    .. attribute:: ipv4_labeled_unicast
                    
                    	IPv4 Labeled Unicast configuration options
                    	**type**\:  :py:class:`Ipv4LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast>`
                    
                    .. attribute:: ipv6_labeled_unicast
                    
                    	IPv6 Labeled Unicast configuration options
                    	**type**\:  :py:class:`Ipv6LabeledUnicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast>`
                    
                    .. attribute:: l3vpn_ipv4_unicast
                    
                    	Unicast IPv4 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv4Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                    
                    .. attribute:: l3vpn_ipv6_unicast
                    
                    	Unicast IPv6 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv6Unicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                    
                    .. attribute:: l3vpn_ipv4_multicast
                    
                    	Multicast IPv4 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv4Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                    
                    .. attribute:: l3vpn_ipv6_multicast
                    
                    	Multicast IPv6 L3VPN configuration options
                    	**type**\:  :py:class:`L3VpnIpv6Multicast <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                    
                    .. attribute:: l2vpn_vpls
                    
                    	BGP\-signalled VPLS configuration options
                    	**type**\:  :py:class:`L2VpnVpls <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls>`
                    
                    .. attribute:: l2vpn_evpn
                    
                    	BGP EVPN configuration options
                    	**type**\:  :py:class:`L2VpnEvpn <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn>`
                    
                    

                    """

                    _prefix = 'oc-bgp'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi, self).__init__()

                        self.yang_name = "afi-safi"
                        self.yang_parent_name = "afi-safis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi_safi_name']
                        self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State)), ("graceful-restart", ("graceful_restart", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart)), ("route-selection-options", ("route_selection_options", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions)), ("use-multiple-paths", ("use_multiple_paths", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths)), ("apply-policy", ("apply_policy", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy)), ("ipv4-unicast", ("ipv4_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast)), ("ipv6-unicast", ("ipv6_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast)), ("ipv4-labeled-unicast", ("ipv4_labeled_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast)), ("ipv6-labeled-unicast", ("ipv6_labeled_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast)), ("l3vpn-ipv4-unicast", ("l3vpn_ipv4_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast)), ("l3vpn-ipv6-unicast", ("l3vpn_ipv6_unicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast)), ("l3vpn-ipv4-multicast", ("l3vpn_ipv4_multicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast)), ("l3vpn-ipv6-multicast", ("l3vpn_ipv6_multicast", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast)), ("l2vpn-vpls", ("l2vpn_vpls", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls)), ("l2vpn-evpn", ("l2vpn_evpn", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                        ])
                        self.afi_safi_name = None

                        self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.graceful_restart = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart()
                        self.graceful_restart.parent = self
                        self._children_name_map["graceful_restart"] = "graceful-restart"
                        self._children_yang_names.add("graceful-restart")

                        self.route_selection_options = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions()
                        self.route_selection_options.parent = self
                        self._children_name_map["route_selection_options"] = "route-selection-options"
                        self._children_yang_names.add("route-selection-options")

                        self.use_multiple_paths = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths()
                        self.use_multiple_paths.parent = self
                        self._children_name_map["use_multiple_paths"] = "use-multiple-paths"
                        self._children_yang_names.add("use-multiple-paths")

                        self.apply_policy = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy()
                        self.apply_policy.parent = self
                        self._children_name_map["apply_policy"] = "apply-policy"
                        self._children_yang_names.add("apply-policy")

                        self.ipv4_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._children_yang_names.add("ipv4-unicast")

                        self.ipv6_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._children_yang_names.add("ipv6-unicast")

                        self.ipv4_labeled_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast()
                        self.ipv4_labeled_unicast.parent = self
                        self._children_name_map["ipv4_labeled_unicast"] = "ipv4-labeled-unicast"
                        self._children_yang_names.add("ipv4-labeled-unicast")

                        self.ipv6_labeled_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast()
                        self.ipv6_labeled_unicast.parent = self
                        self._children_name_map["ipv6_labeled_unicast"] = "ipv6-labeled-unicast"
                        self._children_yang_names.add("ipv6-labeled-unicast")

                        self.l3vpn_ipv4_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                        self.l3vpn_ipv4_unicast.parent = self
                        self._children_name_map["l3vpn_ipv4_unicast"] = "l3vpn-ipv4-unicast"
                        self._children_yang_names.add("l3vpn-ipv4-unicast")

                        self.l3vpn_ipv6_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                        self.l3vpn_ipv6_unicast.parent = self
                        self._children_name_map["l3vpn_ipv6_unicast"] = "l3vpn-ipv6-unicast"
                        self._children_yang_names.add("l3vpn-ipv6-unicast")

                        self.l3vpn_ipv4_multicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                        self.l3vpn_ipv4_multicast.parent = self
                        self._children_name_map["l3vpn_ipv4_multicast"] = "l3vpn-ipv4-multicast"
                        self._children_yang_names.add("l3vpn-ipv4-multicast")

                        self.l3vpn_ipv6_multicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                        self.l3vpn_ipv6_multicast.parent = self
                        self._children_name_map["l3vpn_ipv6_multicast"] = "l3vpn-ipv6-multicast"
                        self._children_yang_names.add("l3vpn-ipv6-multicast")

                        self.l2vpn_vpls = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls()
                        self.l2vpn_vpls.parent = self
                        self._children_name_map["l2vpn_vpls"] = "l2vpn-vpls"
                        self._children_yang_names.add("l2vpn-vpls")

                        self.l2vpn_evpn = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn()
                        self.l2vpn_evpn.parent = self
                        self._children_name_map["l2vpn_evpn"] = "l2vpn-evpn"
                        self._children_yang_names.add("l2vpn-evpn")
                        self._segment_path = lambda: "afi-safi" + "[afi-safi-name='" + str(self.afi_safi_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi, ['afi_safi_name'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters for the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.afi_safi_name = None
                            self.enabled = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config, ['afi_safi_name', 'enabled'], name, value)


                    class State(Entity):
                        """
                        State information relating to the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ])
                            self.afi_safi_name = None
                            self.enabled = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State, ['afi_safi_name', 'enabled'], name, value)


                    class GracefulRestart(Entity):
                        """
                        Parameters relating to BGP graceful\-restart
                        
                        .. attribute:: config
                        
                        	Configuration options for BGP graceful\-restart
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config>`
                        
                        .. attribute:: state
                        
                        	State information for BGP graceful\-restart
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart, self).__init__()

                            self.yang_name = "graceful-restart"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "graceful-restart"


                        class Config(Entity):
                            """
                            Configuration options for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "graceful-restart"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config, ['enabled'], name, value)


                        class State(Entity):
                            """
                            State information for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "graceful-restart"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State, ['enabled'], name, value)


                    class RouteSelectionOptions(Entity):
                        """
                        Parameters relating to options for route selection
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to route selection options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config>`
                        
                        .. attribute:: state
                        
                        	State information for the route selection options
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions, self).__init__()

                            self.yang_name = "route-selection-options"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "route-selection-options"


                        class Config(Entity):
                            """
                            Configuration parameters relating to route selection
                            options
                            
                            .. attribute:: always_compare_med
                            
                            	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ignore_as_path_length
                            
                            	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: external_compare_router_id
                            
                            	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            .. attribute:: advertise_inactive_routes
                            
                            	Advertise inactive routes to external peers.  The default is to only advertise active routes
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: enable_aigp
                            
                            	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ignore_next_hop_igp_metric
                            
                            	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "route-selection-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                                    ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                                    ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                                    ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                                    ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                                    ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                                ])
                                self.always_compare_med = None
                                self.ignore_as_path_length = None
                                self.external_compare_router_id = None
                                self.advertise_inactive_routes = None
                                self.enable_aigp = None
                                self.ignore_next_hop_igp_metric = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


                        class State(Entity):
                            """
                            State information for the route selection options
                            
                            .. attribute:: always_compare_med
                            
                            	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ignore_as_path_length
                            
                            	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: external_compare_router_id
                            
                            	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            .. attribute:: advertise_inactive_routes
                            
                            	Advertise inactive routes to external peers.  The default is to only advertise active routes
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: enable_aigp
                            
                            	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: ignore_next_hop_igp_metric
                            
                            	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "route-selection-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('always_compare_med', YLeaf(YType.boolean, 'always-compare-med')),
                                    ('ignore_as_path_length', YLeaf(YType.boolean, 'ignore-as-path-length')),
                                    ('external_compare_router_id', YLeaf(YType.boolean, 'external-compare-router-id')),
                                    ('advertise_inactive_routes', YLeaf(YType.boolean, 'advertise-inactive-routes')),
                                    ('enable_aigp', YLeaf(YType.boolean, 'enable-aigp')),
                                    ('ignore_next_hop_igp_metric', YLeaf(YType.boolean, 'ignore-next-hop-igp-metric')),
                                ])
                                self.always_compare_med = None
                                self.ignore_as_path_length = None
                                self.external_compare_router_id = None
                                self.advertise_inactive_routes = None
                                self.enable_aigp = None
                                self.ignore_next_hop_igp_metric = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State, ['always_compare_med', 'ignore_as_path_length', 'external_compare_router_id', 'advertise_inactive_routes', 'enable_aigp', 'ignore_next_hop_igp_metric'], name, value)


                    class UseMultiplePaths(Entity):
                        """
                        Parameters related to the use of multiple paths for the
                        same NLRI
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to multipath
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to multipath
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                        
                        .. attribute:: ebgp
                        
                        	Multipath parameters for eBGP
                        	**type**\:  :py:class:`Ebgp <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                        
                        .. attribute:: ibgp
                        
                        	Multipath parameters for iBGP
                        	**type**\:  :py:class:`Ibgp <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths, self).__init__()

                            self.yang_name = "use-multiple-paths"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State)), ("ebgp", ("ebgp", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp)), ("ibgp", ("ibgp", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.ebgp = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                            self.ebgp.parent = self
                            self._children_name_map["ebgp"] = "ebgp"
                            self._children_yang_names.add("ebgp")

                            self.ibgp = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp()
                            self.ibgp.parent = self
                            self._children_name_map["ibgp"] = "ibgp"
                            self._children_yang_names.add("ibgp")
                            self._segment_path = lambda: "use-multiple-paths"


                        class Config(Entity):
                            """
                            Configuration parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config, ['enabled'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.enabled = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State, ['enabled'], name, value)


                        class Ebgp(Entity):
                            """
                            Multipath parameters for eBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to eBGP multipath
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to eBGP multipath
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp, self).__init__()

                                self.yang_name = "ebgp"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "ebgp"


                            class Config(Entity):
                                """
                                Configuration parameters relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "ebgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                        ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                    ])
                                    self.allow_multiple_as = None
                                    self.maximum_paths = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config, ['allow_multiple_as', 'maximum_paths'], name, value)


                            class State(Entity):
                                """
                                State information relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "ebgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('allow_multiple_as', YLeaf(YType.boolean, 'allow-multiple-as')),
                                        ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                    ])
                                    self.allow_multiple_as = None
                                    self.maximum_paths = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State, ['allow_multiple_as', 'maximum_paths'], name, value)


                        class Ibgp(Entity):
                            """
                            Multipath parameters for iBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to iBGP multipath
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to iBGP multipath
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp, self).__init__()

                                self.yang_name = "ibgp"
                                self.yang_parent_name = "use-multiple-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "ibgp"


                            class Config(Entity):
                                """
                                Configuration parameters relating to iBGP multipath
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "ibgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                    ])
                                    self.maximum_paths = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config, ['maximum_paths'], name, value)


                            class State(Entity):
                                """
                                State information relating to iBGP multipath
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**default value**\: 1
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "ibgp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('maximum_paths', YLeaf(YType.uint32, 'maximum-paths')),
                                    ])
                                    self.maximum_paths = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State, ['maximum_paths'], name, value)


                    class ApplyPolicy(Entity):
                        """
                        Anchor point for routing policies in the model.
                        Import and export policies are with respect to the local
                        routing table, i.e., export (send) and import (receive),
                        depending on the context.
                        
                        .. attribute:: config
                        
                        	Policy configuration data
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for routing policy
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy, self).__init__()

                            self.yang_name = "apply-policy"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "apply-policy"


                        class Config(Entity):
                            """
                            Policy configuration data.
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "apply-policy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('import_policy', YLeafList(YType.str, 'import-policy')),
                                    ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                    ('export_policy', YLeafList(YType.str, 'export-policy')),
                                    ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                                ])
                                self.import_policy = []
                                self.default_import_policy = None
                                self.export_policy = []
                                self.default_export_policy = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                        class State(Entity):
                            """
                            Operational state for routing policy
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\:  :py:class:`DefaultPolicyType <ydk.models.openconfig.openconfig_routing_policy.DefaultPolicyType>`
                            
                            	**default value**\: REJECT_ROUTE
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "apply-policy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('import_policy', YLeafList(YType.str, 'import-policy')),
                                    ('default_import_policy', YLeaf(YType.enumeration, 'default-import-policy')),
                                    ('export_policy', YLeafList(YType.str, 'export-policy')),
                                    ('default_export_policy', YLeaf(YType.enumeration, 'default-export-policy')),
                                ])
                                self.import_policy = []
                                self.default_import_policy = None
                                self.export_policy = []
                                self.default_export_policy = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State, ['import_policy', 'default_import_policy', 'export_policy', 'default_export_policy'], name, value)


                    class Ipv4Unicast(Entity):
                        """
                        IPv4 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast, self).__init__()

                            self.yang_name = "ipv4-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit)), ("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ipv4-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config, ['send_default_route'], name, value)


                        class State(Entity):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State, ['send_default_route'], name, value)


                    class Ipv6Unicast(Entity):
                        """
                        IPv6 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast, self).__init__()

                            self.yang_name = "ipv6-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit)), ("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")

                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "ipv6-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config, ['send_default_route'], name, value)


                        class State(Entity):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('send_default_route', YLeaf(YType.boolean, 'send-default-route')),
                                ])
                                self.send_default_route = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State, ['send_default_route'], name, value)


                    class Ipv4LabeledUnicast(Entity):
                        """
                        IPv4 Labeled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast, self).__init__()

                            self.yang_name = "ipv4-labeled-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "ipv4-labeled-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv4-labeled-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class Ipv6LabeledUnicast(Entity):
                        """
                        IPv6 Labeled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast, self).__init__()

                            self.yang_name = "ipv6-labeled-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "ipv6-labeled-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "ipv6-labeled-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabeledUnicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv4Unicast(Entity):
                        """
                        Unicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast, self).__init__()

                            self.yang_name = "l3vpn-ipv4-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv4-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv6Unicast(Entity):
                        """
                        Unicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast, self).__init__()

                            self.yang_name = "l3vpn-ipv6-unicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv6-unicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv4Multicast(Entity):
                        """
                        Multicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast, self).__init__()

                            self.yang_name = "l3vpn-ipv4-multicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv4-multicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv4-multicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L3VpnIpv6Multicast(Entity):
                        """
                        Multicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast, self).__init__()

                            self.yang_name = "l3vpn-ipv6-multicast"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l3vpn-ipv6-multicast"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l3vpn-ipv6-multicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L2VpnVpls(Entity):
                        """
                        BGP\-signalled VPLS configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls, self).__init__()

                            self.yang_name = "l2vpn-vpls"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l2vpn-vpls"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l2vpn-vpls"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                    class L2VpnEvpn(Entity):
                        """
                        BGP EVPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\:  :py:class:`PrefixLimit <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'oc-bgp'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn, self).__init__()

                            self.yang_name = "l2vpn-evpn"
                            self.yang_parent_name = "afi-safi"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("prefix-limit", ("prefix_limit", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                            self.prefix_limit.parent = self
                            self._children_name_map["prefix_limit"] = "prefix-limit"
                            self._children_yang_names.add("prefix-limit")
                            self._segment_path = lambda: "l2vpn-evpn"


                        class PrefixLimit(Entity):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit, self).__init__()

                                self.yang_name = "prefix-limit"
                                self.yang_parent_name = "l2vpn-evpn"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config)), ("state", ("state", Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "prefix-limit"


                            class Config(Entity):
                                """
                                Configuration parameters relating to the prefix
                                limit for the AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)


                            class State(Entity):
                                """
                                State information relating to the prefix\-limit for the
                                AFI\-SAFI
                                
                                .. attribute:: max_prefixes
                                
                                	Maximum number of prefixes that will be accepted from the neighbour
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: shutdown_threshold_pct
                                
                                	Threshold on number of prefixes that can be received from a neighbour before generation of warning messages or log entries. Expressed as a percentage of max\-prefixes
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                .. attribute:: restart_timer
                                
                                	Time interval in seconds after which the BGP session is re\-established after being torn down due to exceeding the max\-prefix limit
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                	**units**\: seconds
                                
                                

                                """

                                _prefix = 'oc-bgp'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "prefix-limit"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefixes', YLeaf(YType.uint32, 'max-prefixes')),
                                        ('shutdown_threshold_pct', YLeaf(YType.uint8, 'shutdown-threshold-pct')),
                                        ('restart_timer', YLeaf(YType.str, 'restart-timer')),
                                    ])
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State, ['max_prefixes', 'shutdown_threshold_pct', 'restart_timer'], name, value)

    def clone_ptr(self):
        self._top_entity = Bgp()
        return self._top_entity

