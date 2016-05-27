""" bgp 

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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.bgp.bgp_types import CommunityTypeEnum
from ydk.models.bgp.bgp_types import PeerTypeEnum
from ydk.models.bgp.bgp_types import RemovePrivateAsOptionEnum
from ydk.models.routing.routing_policy import DefaultPolicyTypeEnum


class Bgp(object):
    """
    Top\-level configuration and state for the BGP router
    
    .. attribute:: global_
    
    	Global configuration for the BGP router
    	**type**\: :py:class:`Global <ydk.models.bgp.bgp.Bgp.Global>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: neighbors
    
    	Configuration for BGP neighbors
    	**type**\: :py:class:`Neighbors <ydk.models.bgp.bgp.Bgp.Neighbors>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: peer_groups
    
    	Configuration for BGP peer\-groups
    	**type**\: :py:class:`PeerGroups <ydk.models.bgp.bgp.Bgp.PeerGroups>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'bgp'
    _revision = '2015-05-15'

    def __init__(self):
        self.global_ = Bgp.Global()
        self.global_.parent = self
        self.neighbors = Bgp.Neighbors()
        self.neighbors.parent = self
        self.peer_groups = Bgp.PeerGroups()
        self.peer_groups.parent = self


    class Global(object):
        """
        Global configuration for the BGP router
        
        .. attribute:: config
        
        	Configuration parameters relating to the global BGP router
        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.Config>`
        
        .. attribute:: state
        
        	State information relating to the global BGP router
        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.State>`
        
        .. attribute:: route_selection_options
        
        	Parameters relating to options for route selection
        	**type**\: :py:class:`RouteSelectionOptions <ydk.models.bgp.bgp.Bgp.Global.RouteSelectionOptions>`
        
        .. attribute:: default_route_distance
        
        	Administrative distance (or preference) assigned to routes received from different sources (external, internal, and local)
        	**type**\: :py:class:`DefaultRouteDistance <ydk.models.bgp.bgp.Bgp.Global.DefaultRouteDistance>`
        
        .. attribute:: confederation
        
        	Parameters indicating whether the local system acts as part of a BGP confederation
        	**type**\: :py:class:`Confederation <ydk.models.bgp.bgp.Bgp.Global.Confederation>`
        
        .. attribute:: use_multiple_paths
        
        	Parameters related to the use of multiple paths for the same NLRI
        	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths>`
        
        .. attribute:: graceful_restart
        
        	Parameters relating the graceful restart mechanism for BGP
        	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.Global.GracefulRestart>`
        
        .. attribute:: afi_safis
        
        	Address family specific configuration
        	**type**\: :py:class:`AfiSafis <ydk.models.bgp.bgp.Bgp.Global.AfiSafis>`
        
        .. attribute:: apply_policy
        
        	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
        	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.Global.ApplyPolicy>`
        
        

        """

        _prefix = 'bgp'
        _revision = '2015-05-15'

        def __init__(self):
            self.parent = None
            self.config = Bgp.Global.Config()
            self.config.parent = self
            self.state = Bgp.Global.State()
            self.state.parent = self
            self.route_selection_options = Bgp.Global.RouteSelectionOptions()
            self.route_selection_options.parent = self
            self.default_route_distance = Bgp.Global.DefaultRouteDistance()
            self.default_route_distance.parent = self
            self.confederation = Bgp.Global.Confederation()
            self.confederation.parent = self
            self.use_multiple_paths = Bgp.Global.UseMultiplePaths()
            self.use_multiple_paths.parent = self
            self.graceful_restart = Bgp.Global.GracefulRestart()
            self.graceful_restart.parent = self
            self.afi_safis = Bgp.Global.AfiSafis()
            self.afi_safis.parent = self
            self.apply_policy = Bgp.Global.ApplyPolicy()
            self.apply_policy.parent = self


        class Config(object):
            """
            Configuration parameters relating to the global BGP router
            
            .. attribute:: as_
            
            	Local autonomous system number of the router.  Uses the 32\-bit as\-number type from the model in RFC 6991
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: router_id
            
            	Router id of the router, expressed as an 32\-bit value, IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.as_ = None
                self.router_id = None

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.as_ is not None:
                    return True

                if self.router_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.Config']['meta_info']


        class State(object):
            """
            State information relating to the global BGP router
            
            .. attribute:: as_
            
            	Local autonomous system number of the router.  Uses the 32\-bit as\-number type from the model in RFC 6991
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: router_id
            
            	Router id of the router, expressed as an 32\-bit value, IPv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: total_paths
            
            	Total number of BGP paths within the context
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: total_prefixes
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.as_ = None
                self.router_id = None
                self.total_paths = None
                self.total_prefixes = None

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.as_ is not None:
                    return True

                if self.router_id is not None:
                    return True

                if self.total_paths is not None:
                    return True

                if self.total_prefixes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.State']['meta_info']


        class RouteSelectionOptions(object):
            """
            Parameters relating to options for route selection
            
            .. attribute:: config
            
            	Configuration parameters relating to route selection options
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.RouteSelectionOptions.Config>`
            
            .. attribute:: state
            
            	State information for the route selection options
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.RouteSelectionOptions.State>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.RouteSelectionOptions.Config()
                self.config.parent = self
                self.state = Bgp.Global.RouteSelectionOptions.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration parameters relating to route selection
                options
                
                .. attribute:: always_compare_med
                
                	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                	**type**\: bool
                
                .. attribute:: ignore_as_path_length
                
                	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                	**type**\: bool
                
                .. attribute:: external_compare_router_id
                
                	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                	**type**\: bool
                
                .. attribute:: advertise_inactive_routes
                
                	Advertise inactive routes to external peers.  The default is to only advertise active routes
                	**type**\: bool
                
                .. attribute:: enable_aigp
                
                	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                	**type**\: bool
                
                .. attribute:: ignore_next_hop_igp_metric
                
                	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.always_compare_med = None
                    self.ignore_as_path_length = None
                    self.external_compare_router_id = None
                    self.advertise_inactive_routes = None
                    self.enable_aigp = None
                    self.ignore_next_hop_igp_metric = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:route-selection-options/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.always_compare_med is not None:
                        return True

                    if self.ignore_as_path_length is not None:
                        return True

                    if self.external_compare_router_id is not None:
                        return True

                    if self.advertise_inactive_routes is not None:
                        return True

                    if self.enable_aigp is not None:
                        return True

                    if self.ignore_next_hop_igp_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.RouteSelectionOptions.Config']['meta_info']


            class State(object):
                """
                State information for the route selection options
                
                .. attribute:: always_compare_med
                
                	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                	**type**\: bool
                
                .. attribute:: ignore_as_path_length
                
                	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                	**type**\: bool
                
                .. attribute:: external_compare_router_id
                
                	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                	**type**\: bool
                
                .. attribute:: advertise_inactive_routes
                
                	Advertise inactive routes to external peers.  The default is to only advertise active routes
                	**type**\: bool
                
                .. attribute:: enable_aigp
                
                	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                	**type**\: bool
                
                .. attribute:: ignore_next_hop_igp_metric
                
                	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.always_compare_med = None
                    self.ignore_as_path_length = None
                    self.external_compare_router_id = None
                    self.advertise_inactive_routes = None
                    self.enable_aigp = None
                    self.ignore_next_hop_igp_metric = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:route-selection-options/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.always_compare_med is not None:
                        return True

                    if self.ignore_as_path_length is not None:
                        return True

                    if self.external_compare_router_id is not None:
                        return True

                    if self.advertise_inactive_routes is not None:
                        return True

                    if self.enable_aigp is not None:
                        return True

                    if self.ignore_next_hop_igp_metric is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.RouteSelectionOptions.State']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:route-selection-options'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.RouteSelectionOptions']['meta_info']


        class DefaultRouteDistance(object):
            """
            Administrative distance (or preference) assigned to
            routes received from different sources
            (external, internal, and local).
            
            .. attribute:: config
            
            	Configuration parameters relating to the default route distance
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.DefaultRouteDistance.Config>`
            
            .. attribute:: state
            
            	State information relating to the default route distance
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.DefaultRouteDistance.State>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.DefaultRouteDistance.Config()
                self.config.parent = self
                self.state = Bgp.Global.DefaultRouteDistance.State()
                self.state.parent = self


            class Config(object):
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

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.external_route_distance = None
                    self.internal_route_distance = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:default-route-distance/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.external_route_distance is not None:
                        return True

                    if self.internal_route_distance is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.DefaultRouteDistance.Config']['meta_info']


            class State(object):
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

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.external_route_distance = None
                    self.internal_route_distance = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:default-route-distance/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.external_route_distance is not None:
                        return True

                    if self.internal_route_distance is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.DefaultRouteDistance.State']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:default-route-distance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.DefaultRouteDistance']['meta_info']


        class Confederation(object):
            """
            Parameters indicating whether the local system acts as part
            of a BGP confederation
            
            .. attribute:: config
            
            	Configuration parameters relating to BGP confederations
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.Confederation.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP confederations
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.Confederation.State>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.Confederation.Config()
                self.config.parent = self
                self.state = Bgp.Global.Confederation.State()
                self.state.parent = self


            class Config(object):
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

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None
                    self.identifier = None
                    self.member_as = YLeafList()
                    self.member_as.parent = self
                    self.member_as.name = 'member_as'

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:confederation/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    if self.identifier is not None:
                        return True

                    if self.member_as is not None:
                        for child in self.member_as:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.Confederation.Config']['meta_info']


            class State(object):
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

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None
                    self.identifier = None
                    self.member_as = YLeafList()
                    self.member_as.parent = self
                    self.member_as.name = 'member_as'

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:confederation/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    if self.identifier is not None:
                        return True

                    if self.member_as is not None:
                        for child in self.member_as:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.Confederation.State']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:confederation'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.Confederation']['meta_info']


        class UseMultiplePaths(object):
            """
            Parameters related to the use of multiple paths for the
            same NLRI
            
            .. attribute:: config
            
            	Configuration parameters relating to multipath
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Config>`
            
            .. attribute:: state
            
            	State parameters relating to multipath
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.State>`
            
            .. attribute:: ebgp
            
            	Multipath parameters for eBGP
            	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ebgp>`
            
            .. attribute:: ibgp
            
            	Multipath parameters for iBGP
            	**type**\: :py:class:`Ibgp <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ibgp>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.UseMultiplePaths.Config()
                self.config.parent = self
                self.state = Bgp.Global.UseMultiplePaths.State()
                self.state.parent = self
                self.ebgp = Bgp.Global.UseMultiplePaths.Ebgp()
                self.ebgp.parent = self
                self.ibgp = Bgp.Global.UseMultiplePaths.Ibgp()
                self.ibgp.parent = self


            class Config(object):
                """
                Configuration parameters relating to multipath
                
                .. attribute:: enabled
                
                	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.UseMultiplePaths.Config']['meta_info']


            class State(object):
                """
                State parameters relating to multipath
                
                .. attribute:: enabled
                
                	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.UseMultiplePaths.State']['meta_info']


            class Ebgp(object):
                """
                Multipath parameters for eBGP
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multipath
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ebgp.Config>`
                
                .. attribute:: state
                
                	State information relating to eBGP multipath
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ebgp.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Global.UseMultiplePaths.Ebgp.Config()
                    self.config.parent = self
                    self.state = Bgp.Global.UseMultiplePaths.Ebgp.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to eBGP multipath
                    
                    .. attribute:: allow_multiple_as
                    
                    	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                    	**type**\: bool
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_multiple_as = None
                        self.maximum_paths = None

                    @property
                    def _common_path(self):

                        return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ebgp/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_multiple_as is not None:
                            return True

                        if self.maximum_paths is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.UseMultiplePaths.Ebgp.Config']['meta_info']


                class State(object):
                    """
                    State information relating to eBGP multipath
                    
                    .. attribute:: allow_multiple_as
                    
                    	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                    	**type**\: bool
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_multiple_as = None
                        self.maximum_paths = None

                    @property
                    def _common_path(self):

                        return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ebgp/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_multiple_as is not None:
                            return True

                        if self.maximum_paths is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.UseMultiplePaths.Ebgp.State']['meta_info']

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ebgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.UseMultiplePaths.Ebgp']['meta_info']


            class Ibgp(object):
                """
                Multipath parameters for iBGP
                
                .. attribute:: config
                
                	Configuration parameters relating to iBGP multipath
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ibgp.Config>`
                
                .. attribute:: state
                
                	State information relating to iBGP multipath
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.UseMultiplePaths.Ibgp.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Global.UseMultiplePaths.Ibgp.Config()
                    self.config.parent = self
                    self.state = Bgp.Global.UseMultiplePaths.Ibgp.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to iBGP multipath
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.maximum_paths = None

                    @property
                    def _common_path(self):

                        return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ibgp/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.maximum_paths is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.UseMultiplePaths.Ibgp.Config']['meta_info']


                class State(object):
                    """
                    State information relating to iBGP multipath
                    
                    .. attribute:: maximum_paths
                    
                    	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.maximum_paths = None

                    @property
                    def _common_path(self):

                        return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ibgp/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.maximum_paths is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.UseMultiplePaths.Ibgp.State']['meta_info']

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:use-multiple-paths/bgp:ibgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.UseMultiplePaths.Ibgp']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:use-multiple-paths'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.ebgp is not None and self.ebgp._has_data():
                    return True

                if self.ibgp is not None and self.ibgp._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.UseMultiplePaths']['meta_info']


        class GracefulRestart(object):
            """
            Parameters relating the graceful restart mechanism for BGP
            
            .. attribute:: config
            
            	Configuration parameters relating to graceful\-restart
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.GracefulRestart.Config>`
            
            .. attribute:: state
            
            	State information associated with graceful\-restart
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.GracefulRestart.State>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.GracefulRestart.Config()
                self.config.parent = self
                self.state = Bgp.Global.GracefulRestart.State()
                self.state.parent = self


            class Config(object):
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
                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: helper_only
                
                	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None
                    self.restart_time = None
                    self.stale_routes_time = None
                    self.helper_only = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:graceful-restart/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    if self.restart_time is not None:
                        return True

                    if self.stale_routes_time is not None:
                        return True

                    if self.helper_only is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.GracefulRestart.Config']['meta_info']


            class State(object):
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
                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: helper_only
                
                	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                	**type**\: bool
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.enabled = None
                    self.restart_time = None
                    self.stale_routes_time = None
                    self.helper_only = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:graceful-restart/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enabled is not None:
                        return True

                    if self.restart_time is not None:
                        return True

                    if self.stale_routes_time is not None:
                        return True

                    if self.helper_only is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.GracefulRestart.State']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:graceful-restart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.GracefulRestart']['meta_info']


        class AfiSafis(object):
            """
            Address family specific configuration
            
            .. attribute:: afi_safi
            
            	AFI,SAFI configuration available for the neighbour or group
            	**type**\: list of :py:class:`AfiSafi <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.afi_safi = YList()
                self.afi_safi.parent = self
                self.afi_safi.name = 'afi_safi'


            class AfiSafi(object):
                """
                AFI,SAFI configuration available for the
                neighbour or group
                
                .. attribute:: afi_safi_name  <key>
                
                	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                	**type**\: str
                
                .. attribute:: graceful_restart
                
                	Parameters relating to BGP graceful\-restart
                	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart>`
                
                .. attribute:: config
                
                	Configuration parameters for the AFI\-SAFI
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Config>`
                
                .. attribute:: state
                
                	State information relating to the AFI\-SAFI
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.State>`
                
                .. attribute:: apply_policy
                
                	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy>`
                
                .. attribute:: ipv4_unicast
                
                	IPv4 unicast configuration options
                	**type**\: :py:class:`Ipv4Unicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast>`
                
                .. attribute:: ipv6_unicast
                
                	IPv6 unicast configuration options
                	**type**\: :py:class:`Ipv6Unicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast>`
                
                .. attribute:: ipv4_labelled_unicast
                
                	IPv4 Labelled Unicast configuration options
                	**type**\: :py:class:`Ipv4LabelledUnicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast>`
                
                .. attribute:: ipv6_labelled_unicast
                
                	IPv6 Labelled Unicast configuration options
                	**type**\: :py:class:`Ipv6LabelledUnicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast>`
                
                .. attribute:: l3vpn_ipv4_unicast
                
                	Unicast IPv4 L3VPN configuration options
                	**type**\: :py:class:`L3VpnIpv4Unicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                
                .. attribute:: l3vpn_ipv6_unicast
                
                	Unicast IPv6 L3VPN configuration options
                	**type**\: :py:class:`L3VpnIpv6Unicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                
                .. attribute:: l3vpn_ipv4_multicast
                
                	Multicast IPv4 L3VPN configuration options
                	**type**\: :py:class:`L3VpnIpv4Multicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                
                .. attribute:: l3vpn_ipv6_multicast
                
                	Multicast IPv6 L3VPN configuration options
                	**type**\: :py:class:`L3VpnIpv6Multicast <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                
                .. attribute:: l2vpn_vpls
                
                	BGP\-signalled VPLS configuration options
                	**type**\: :py:class:`L2VpnVpls <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls>`
                
                .. attribute:: l2vpn_evpn
                
                	BGP EVPN configuration options
                	**type**\: :py:class:`L2VpnEvpn <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn>`
                
                .. attribute:: route_selection_options
                
                	Parameters relating to options for route selection
                	**type**\: :py:class:`RouteSelectionOptions <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions>`
                
                .. attribute:: use_multiple_paths
                
                	Parameters related to the use of multiple paths for the same NLRI
                	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.afi_safi_name = None
                    self.graceful_restart = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart()
                    self.graceful_restart.parent = self
                    self.config = Bgp.Global.AfiSafis.AfiSafi.Config()
                    self.config.parent = self
                    self.state = Bgp.Global.AfiSafis.AfiSafi.State()
                    self.state.parent = self
                    self.apply_policy = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy()
                    self.apply_policy.parent = self
                    self.ipv4_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast()
                    self.ipv4_unicast.parent = self
                    self.ipv6_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast()
                    self.ipv6_unicast.parent = self
                    self.ipv4_labelled_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast()
                    self.ipv4_labelled_unicast.parent = self
                    self.ipv6_labelled_unicast = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast()
                    self.ipv6_labelled_unicast.parent = self
                    self.l3vpn_ipv4_unicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                    self.l3vpn_ipv4_unicast.parent = self
                    self.l3vpn_ipv6_unicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                    self.l3vpn_ipv6_unicast.parent = self
                    self.l3vpn_ipv4_multicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                    self.l3vpn_ipv4_multicast.parent = self
                    self.l3vpn_ipv6_multicast = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                    self.l3vpn_ipv6_multicast.parent = self
                    self.l2vpn_vpls = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls()
                    self.l2vpn_vpls.parent = self
                    self.l2vpn_evpn = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn()
                    self.l2vpn_evpn.parent = self
                    self.route_selection_options = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions()
                    self.route_selection_options.parent = self
                    self.use_multiple_paths = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths()
                    self.use_multiple_paths.parent = self


                class GracefulRestart(object):
                    """
                    Parameters relating to BGP graceful\-restart
                    
                    .. attribute:: config
                    
                    	Configuration options for BGP graceful\-restart
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config>`
                    
                    .. attribute:: state
                    
                    	State information for BGP graceful\-restart
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration options for BGP graceful\-restart
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info']


                    class State(object):
                        """
                        State information for BGP graceful\-restart
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:graceful-restart'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.GracefulRestart']['meta_info']


                class Config(object):
                    """
                    Configuration parameters for the AFI\-SAFI
                    
                    .. attribute:: afi_safi_name
                    
                    	AFI,SAFI
                    	**type**\: str
                    
                    .. attribute:: enabled
                    
                    	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.afi_safi_name = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.afi_safi_name is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Config']['meta_info']


                class State(object):
                    """
                    State information relating to the AFI\-SAFI
                    
                    .. attribute:: afi_safi_name
                    
                    	AFI,SAFI
                    	**type**\: str
                    
                    .. attribute:: enabled
                    
                    	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                    	**type**\: bool
                    
                    .. attribute:: total_paths
                    
                    	Total number of BGP paths within the context
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_prefixes
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.afi_safi_name = None
                        self.enabled = None
                        self.total_paths = None
                        self.total_prefixes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.afi_safi_name is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.total_paths is not None:
                            return True

                        if self.total_prefixes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.State']['meta_info']


                class ApplyPolicy(object):
                    """
                    Anchor point for routing policies in the model.
                    Import and export policies are with respect to the local
                    routing table, i.e., export (send) and import (receive),
                    depending on the context.
                    
                    .. attribute:: config
                    
                    	Policy configuration data
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state for routing policy
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Policy configuration data.
                        
                        .. attribute:: import_policy
                        
                        	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        .. attribute:: default_import_policy
                        
                        	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                        	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                        
                        .. attribute:: export_policy
                        
                        	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        .. attribute:: default_export_policy
                        
                        	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                        	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.import_policy = YLeafList()
                            self.import_policy.parent = self
                            self.import_policy.name = 'import_policy'
                            self.default_import_policy = None
                            self.export_policy = YLeafList()
                            self.export_policy.parent = self
                            self.export_policy.name = 'export_policy'
                            self.default_export_policy = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.import_policy is not None:
                                for child in self.import_policy:
                                    if child is not None:
                                        return True

                            if self.default_import_policy is not None:
                                return True

                            if self.export_policy is not None:
                                for child in self.export_policy:
                                    if child is not None:
                                        return True

                            if self.default_export_policy is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info']


                    class State(object):
                        """
                        Operational state for routing policy
                        
                        .. attribute:: import_policy
                        
                        	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        .. attribute:: default_import_policy
                        
                        	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                        	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                        
                        .. attribute:: export_policy
                        
                        	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                        	**type**\: list of str
                        
                        .. attribute:: default_export_policy
                        
                        	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                        	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.import_policy = YLeafList()
                            self.import_policy.parent = self
                            self.import_policy.name = 'import_policy'
                            self.default_import_policy = None
                            self.export_policy = YLeafList()
                            self.export_policy.parent = self
                            self.export_policy.name = 'export_policy'
                            self.default_export_policy = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.import_policy is not None:
                                for child in self.import_policy:
                                    if child is not None:
                                        return True

                            if self.default_import_policy is not None:
                                return True

                            if self.export_policy is not None:
                                for child in self.export_policy:
                                    if child is not None:
                                        return True

                            if self.default_export_policy is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:apply-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']


                class Ipv4Unicast(object):
                    """
                    IPv4 unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                    
                    .. attribute:: state
                    
                    	State information for common IPv4 and IPv6 unicast parameters
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State()
                        self.state.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']


                    class Config(object):
                        """
                        Configuration parameters for common IPv4 and IPv6 unicast
                        AFI\-SAFI options
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.send_default_route = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.send_default_route is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info']


                    class State(object):
                        """
                        State information for common IPv4 and IPv6 unicast
                        parameters
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.send_default_route = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.send_default_route is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ipv4-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']


                class Ipv6Unicast(object):
                    """
                    IPv6 unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                    
                    .. attribute:: state
                    
                    	State information for common IPv4 and IPv6 unicast parameters
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                        self.prefix_limit.parent = self
                        self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State()
                        self.state.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']


                    class Config(object):
                        """
                        Configuration parameters for common IPv4 and IPv6 unicast
                        AFI\-SAFI options
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.send_default_route = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.send_default_route is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info']


                    class State(object):
                        """
                        State information for common IPv4 and IPv6 unicast
                        parameters
                        
                        .. attribute:: send_default_route
                        
                        	If set to true, send the default\-route to the neighbour(s)
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.send_default_route = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.send_default_route is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ipv6-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']


                class Ipv4LabelledUnicast(object):
                    """
                    IPv4 Labelled Unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ipv4-labelled-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']


                class Ipv6LabelledUnicast(object):
                    """
                    IPv6 Labelled Unicast configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ipv6-labelled-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']


                class L3VpnIpv4Unicast(object):
                    """
                    Unicast IPv4 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l3vpn-ipv4-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']


                class L3VpnIpv6Unicast(object):
                    """
                    Unicast IPv6 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l3vpn-ipv6-unicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']


                class L3VpnIpv4Multicast(object):
                    """
                    Multicast IPv4 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l3vpn-ipv4-multicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']


                class L3VpnIpv6Multicast(object):
                    """
                    Multicast IPv6 L3VPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l3vpn-ipv6-multicast'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']


                class L2VpnVpls(object):
                    """
                    BGP\-signalled VPLS configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l2vpn-vpls'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']


                class L2VpnEvpn(object):
                    """
                    BGP EVPN configuration options
                    
                    .. attribute:: prefix_limit
                    
                    	Configure the maximum number of prefixes that will be accepted from a peer
                    	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.prefix_limit = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                        self.prefix_limit.parent = self


                    class PrefixLimit(object):
                        """
                        Configure the maximum number of prefixes that will be
                        accepted from a peer
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the prefix\-limit for the AFI\-SAFI
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                            self.state.parent = self


                        class Config(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info']


                        class State(object):
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
                            	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.max_prefixes = None
                                self.shutdown_threshold_pct = None
                                self.restart_timer = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.max_prefixes is not None:
                                    return True

                                if self.shutdown_threshold_pct is not None:
                                    return True

                                if self.restart_timer is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:prefix-limit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:l2vpn-evpn'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix_limit is not None and self.prefix_limit._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']


                class RouteSelectionOptions(object):
                    """
                    Parameters relating to options for route selection
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to route selection options
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config>`
                    
                    .. attribute:: state
                    
                    	State information for the route selection options
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to route selection
                        options
                        
                        .. attribute:: always_compare_med
                        
                        	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                        	**type**\: bool
                        
                        .. attribute:: ignore_as_path_length
                        
                        	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                        	**type**\: bool
                        
                        .. attribute:: external_compare_router_id
                        
                        	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                        	**type**\: bool
                        
                        .. attribute:: advertise_inactive_routes
                        
                        	Advertise inactive routes to external peers.  The default is to only advertise active routes
                        	**type**\: bool
                        
                        .. attribute:: enable_aigp
                        
                        	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                        	**type**\: bool
                        
                        .. attribute:: ignore_next_hop_igp_metric
                        
                        	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.always_compare_med = None
                            self.ignore_as_path_length = None
                            self.external_compare_router_id = None
                            self.advertise_inactive_routes = None
                            self.enable_aigp = None
                            self.ignore_next_hop_igp_metric = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.always_compare_med is not None:
                                return True

                            if self.ignore_as_path_length is not None:
                                return True

                            if self.external_compare_router_id is not None:
                                return True

                            if self.advertise_inactive_routes is not None:
                                return True

                            if self.enable_aigp is not None:
                                return True

                            if self.ignore_next_hop_igp_metric is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.Config']['meta_info']


                    class State(object):
                        """
                        State information for the route selection options
                        
                        .. attribute:: always_compare_med
                        
                        	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                        	**type**\: bool
                        
                        .. attribute:: ignore_as_path_length
                        
                        	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                        	**type**\: bool
                        
                        .. attribute:: external_compare_router_id
                        
                        	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                        	**type**\: bool
                        
                        .. attribute:: advertise_inactive_routes
                        
                        	Advertise inactive routes to external peers.  The default is to only advertise active routes
                        	**type**\: bool
                        
                        .. attribute:: enable_aigp
                        
                        	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                        	**type**\: bool
                        
                        .. attribute:: ignore_next_hop_igp_metric
                        
                        	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.always_compare_med = None
                            self.ignore_as_path_length = None
                            self.external_compare_router_id = None
                            self.advertise_inactive_routes = None
                            self.enable_aigp = None
                            self.ignore_next_hop_igp_metric = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.always_compare_med is not None:
                                return True

                            if self.ignore_as_path_length is not None:
                                return True

                            if self.external_compare_router_id is not None:
                                return True

                            if self.advertise_inactive_routes is not None:
                                return True

                            if self.enable_aigp is not None:
                                return True

                            if self.ignore_next_hop_igp_metric is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:route-selection-options'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']


                class UseMultiplePaths(object):
                    """
                    Parameters related to the use of multiple paths for the
                    same NLRI
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to multipath
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to multipath
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                    
                    .. attribute:: ebgp
                    
                    	Multipath parameters for eBGP
                    	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                    
                    .. attribute:: ibgp
                    
                    	Multipath parameters for iBGP
                    	**type**\: :py:class:`Ibgp <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                        self.config.parent = self
                        self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State()
                        self.state.parent = self
                        self.ebgp = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                        self.ebgp.parent = self
                        self.ibgp = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp()
                        self.ibgp.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to multipath
                        
                        .. attribute:: enabled
                        
                        	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info']


                    class State(object):
                        """
                        State parameters relating to multipath
                        
                        .. attribute:: enabled
                        
                        	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info']


                    class Ebgp(object):
                        """
                        Multipath parameters for eBGP
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to eBGP multipath
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to eBGP multipath
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to eBGP multipath
                            
                            .. attribute:: allow_multiple_as
                            
                            	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                            	**type**\: bool
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.allow_multiple_as = None
                                self.maximum_paths = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.allow_multiple_as is not None:
                                    return True

                                if self.maximum_paths is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info']


                        class State(object):
                            """
                            State information relating to eBGP multipath
                            
                            .. attribute:: allow_multiple_as
                            
                            	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                            	**type**\: bool
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.allow_multiple_as = None
                                self.maximum_paths = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.allow_multiple_as is not None:
                                    return True

                                if self.maximum_paths is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ebgp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']


                    class Ibgp(object):
                        """
                        Multipath parameters for iBGP
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to iBGP multipath
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to iBGP multipath
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config()
                            self.config.parent = self
                            self.state = Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to iBGP multipath
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.maximum_paths = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.maximum_paths is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config']['meta_info']


                        class State(object):
                            """
                            State information relating to iBGP multipath
                            
                            .. attribute:: maximum_paths
                            
                            	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.maximum_paths = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.maximum_paths is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ibgp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:use-multiple-paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.ebgp is not None and self.ebgp._has_data():
                            return True

                        if self.ibgp is not None and self.ibgp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']

                @property
                def _common_path(self):
                    if self.afi_safi_name is None:
                        raise YPYDataValidationError('Key property afi_safi_name is None')

                    return '/bgp:bgp/bgp:global/bgp:afi-safis/bgp:afi-safi[bgp:afi-safi-name = ' + str(self.afi_safi_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.afi_safi_name is not None:
                        return True

                    if self.graceful_restart is not None and self.graceful_restart._has_data():
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.apply_policy is not None and self.apply_policy._has_data():
                        return True

                    if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                        return True

                    if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                        return True

                    if self.ipv4_labelled_unicast is not None and self.ipv4_labelled_unicast._has_data():
                        return True

                    if self.ipv6_labelled_unicast is not None and self.ipv6_labelled_unicast._has_data():
                        return True

                    if self.l3vpn_ipv4_unicast is not None and self.l3vpn_ipv4_unicast._has_data():
                        return True

                    if self.l3vpn_ipv6_unicast is not None and self.l3vpn_ipv6_unicast._has_data():
                        return True

                    if self.l3vpn_ipv4_multicast is not None and self.l3vpn_ipv4_multicast._has_data():
                        return True

                    if self.l3vpn_ipv6_multicast is not None and self.l3vpn_ipv6_multicast._has_data():
                        return True

                    if self.l2vpn_vpls is not None and self.l2vpn_vpls._has_data():
                        return True

                    if self.l2vpn_evpn is not None and self.l2vpn_evpn._has_data():
                        return True

                    if self.route_selection_options is not None and self.route_selection_options._has_data():
                        return True

                    if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.AfiSafis.AfiSafi']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:afi-safis'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.afi_safi is not None:
                    for child_ref in self.afi_safi:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.AfiSafis']['meta_info']


        class ApplyPolicy(object):
            """
            Anchor point for routing policies in the model.
            Import and export policies are with respect to the local
            routing table, i.e., export (send) and import (receive),
            depending on the context.
            
            .. attribute:: config
            
            	Policy configuration data
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Global.ApplyPolicy.Config>`
            
            .. attribute:: state
            
            	Operational state for routing policy
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Global.ApplyPolicy.State>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.config = Bgp.Global.ApplyPolicy.Config()
                self.config.parent = self
                self.state = Bgp.Global.ApplyPolicy.State()
                self.state.parent = self


            class Config(object):
                """
                Policy configuration data.
                
                .. attribute:: import_policy
                
                	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                .. attribute:: default_import_policy
                
                	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                
                .. attribute:: export_policy
                
                	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                .. attribute:: default_export_policy
                
                	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.import_policy = YLeafList()
                    self.import_policy.parent = self
                    self.import_policy.name = 'import_policy'
                    self.default_import_policy = None
                    self.export_policy = YLeafList()
                    self.export_policy.parent = self
                    self.export_policy.name = 'export_policy'
                    self.default_export_policy = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:apply-policy/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.import_policy is not None:
                        for child in self.import_policy:
                            if child is not None:
                                return True

                    if self.default_import_policy is not None:
                        return True

                    if self.export_policy is not None:
                        for child in self.export_policy:
                            if child is not None:
                                return True

                    if self.default_export_policy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.ApplyPolicy.Config']['meta_info']


            class State(object):
                """
                Operational state for routing policy
                
                .. attribute:: import_policy
                
                	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                .. attribute:: default_import_policy
                
                	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                
                .. attribute:: export_policy
                
                	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                	**type**\: list of str
                
                .. attribute:: default_export_policy
                
                	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.import_policy = YLeafList()
                    self.import_policy.parent = self
                    self.import_policy.name = 'import_policy'
                    self.default_import_policy = None
                    self.export_policy = YLeafList()
                    self.export_policy.parent = self
                    self.export_policy.name = 'export_policy'
                    self.default_export_policy = None

                @property
                def _common_path(self):

                    return '/bgp:bgp/bgp:global/bgp:apply-policy/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.import_policy is not None:
                        for child in self.import_policy:
                            if child is not None:
                                return True

                    if self.default_import_policy is not None:
                        return True

                    if self.export_policy is not None:
                        for child in self.export_policy:
                            if child is not None:
                                return True

                    if self.default_export_policy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Global.ApplyPolicy.State']['meta_info']

            @property
            def _common_path(self):

                return '/bgp:bgp/bgp:global/bgp:apply-policy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Global.ApplyPolicy']['meta_info']

        @property
        def _common_path(self):

            return '/bgp:bgp/bgp:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.config is not None and self.config._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            if self.route_selection_options is not None and self.route_selection_options._has_data():
                return True

            if self.default_route_distance is not None and self.default_route_distance._has_data():
                return True

            if self.confederation is not None and self.confederation._has_data():
                return True

            if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                return True

            if self.graceful_restart is not None and self.graceful_restart._has_data():
                return True

            if self.afi_safis is not None and self.afi_safis._has_data():
                return True

            if self.apply_policy is not None and self.apply_policy._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp._meta import _bgp as meta
            return meta._meta_table['Bgp.Global']['meta_info']


    class Neighbors(object):
        """
        Configuration for BGP neighbors
        
        .. attribute:: neighbor
        
        	List of BGP neighbors configured on the local system, uniquely identified by peer IPv[46] address
        	**type**\: list of :py:class:`Neighbor <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'bgp'
        _revision = '2015-05-15'

        def __init__(self):
            self.parent = None
            self.neighbor = YList()
            self.neighbor.parent = self
            self.neighbor.name = 'neighbor'


        class Neighbor(object):
            """
            List of BGP neighbors configured on the local system,
            uniquely identified by peer IPv[46] address
            
            .. attribute:: neighbor_address  <key>
            
            	Reference to the address of the BGP neighbor used as a key in the neighbor list
            	**type**\: one of the below types:
            
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: config
            
            	Configuration parameters relating to the BGP neighbor or group
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP neighbor or group
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State>`
            
            .. attribute:: timers
            
            	Timers related to a BGP neighbor or group
            	**type**\: :py:class:`Timers <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Timers>`
            
            .. attribute:: transport
            
            	Transport session parameters for the BGP neighbor or group
            	**type**\: :py:class:`Transport <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Transport>`
            
            .. attribute:: error_handling
            
            	Error handling parameters used for the BGP neighbor or group
            	**type**\: :py:class:`ErrorHandling <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ErrorHandling>`
            
            .. attribute:: logging_options
            
            	Logging options for events related to the BGP neighbor or group
            	**type**\: :py:class:`LoggingOptions <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.LoggingOptions>`
            
            .. attribute:: ebgp_multihop
            
            	eBGP multi\-hop parameters for the BGP neighbor or group
            	**type**\: :py:class:`EbgpMultihop <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.EbgpMultihop>`
            
            .. attribute:: route_reflector
            
            	Route reflector parameters for the BGP neighbor or group
            	**type**\: :py:class:`RouteReflector <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.RouteReflector>`
            
            .. attribute:: as_path_options
            
            	AS\_PATH manipulation parameters for the BGP neighbor or group
            	**type**\: :py:class:`AsPathOptions <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AsPathOptions>`
            
            .. attribute:: add_paths
            
            	Parameters relating to the advertisement and receipt of multiple paths for a single NLRI (add\-paths)
            	**type**\: :py:class:`AddPaths <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AddPaths>`
            
            .. attribute:: afi_safis
            
            	Per\-address\-family configuration parameters associated with the neighbor or group
            	**type**\: :py:class:`AfiSafis <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis>`
            
            .. attribute:: graceful_restart
            
            	Parameters relating the graceful restart mechanism for BGP
            	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.GracefulRestart>`
            
            .. attribute:: apply_policy
            
            	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
            	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ApplyPolicy>`
            
            .. attribute:: use_multiple_paths
            
            	Parameters related to the use of multiple\-paths for the same NLRI when they are received only from this neighbor
            	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.neighbor_address = None
                self.config = Bgp.Neighbors.Neighbor.Config()
                self.config.parent = self
                self.state = Bgp.Neighbors.Neighbor.State()
                self.state.parent = self
                self.timers = Bgp.Neighbors.Neighbor.Timers()
                self.timers.parent = self
                self.transport = Bgp.Neighbors.Neighbor.Transport()
                self.transport.parent = self
                self.error_handling = Bgp.Neighbors.Neighbor.ErrorHandling()
                self.error_handling.parent = self
                self.logging_options = Bgp.Neighbors.Neighbor.LoggingOptions()
                self.logging_options.parent = self
                self.ebgp_multihop = Bgp.Neighbors.Neighbor.EbgpMultihop()
                self.ebgp_multihop.parent = self
                self.route_reflector = Bgp.Neighbors.Neighbor.RouteReflector()
                self.route_reflector.parent = self
                self.as_path_options = Bgp.Neighbors.Neighbor.AsPathOptions()
                self.as_path_options.parent = self
                self.add_paths = Bgp.Neighbors.Neighbor.AddPaths()
                self.add_paths.parent = self
                self.afi_safis = Bgp.Neighbors.Neighbor.AfiSafis()
                self.afi_safis.parent = self
                self.graceful_restart = Bgp.Neighbors.Neighbor.GracefulRestart()
                self.graceful_restart.parent = self
                self.apply_policy = Bgp.Neighbors.Neighbor.ApplyPolicy()
                self.apply_policy.parent = self
                self.use_multiple_paths = Bgp.Neighbors.Neighbor.UseMultiplePaths()
                self.use_multiple_paths.parent = self


            class Config(object):
                """
                Configuration parameters relating to the BGP neighbor or
                group
                
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
                	**type**\: :py:class:`PeerTypeEnum <ydk.models.bgp.bgp_types.PeerTypeEnum>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers
                	**type**\: :py:class:`RemovePrivateAsOptionEnum <ydk.models.bgp.bgp_types.RemovePrivateAsOptionEnum>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\: :py:class:`CommunityTypeEnum <ydk.models.bgp.bgp_types.CommunityTypeEnum>`
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: peer_group
                
                	The peer\-group with which this neighbor is associated
                	**type**\: str
                
                .. attribute:: neighbor_address
                
                	Address of the BGP peer, either in IPv4 or IPv6
                	**type**\: one of the below types:
                
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.peer_group = None
                    self.neighbor_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer_as is not None:
                        return True

                    if self.local_as is not None:
                        return True

                    if self.peer_type is not None:
                        return True

                    if self.auth_password is not None:
                        return True

                    if self.remove_private_as is not None:
                        return True

                    if self.route_flap_damping is not None:
                        return True

                    if self.send_community is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.peer_group is not None:
                        return True

                    if self.neighbor_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.Config']['meta_info']


            class State(object):
                """
                State information relating to the BGP neighbor or group
                
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
                	**type**\: :py:class:`PeerTypeEnum <ydk.models.bgp.bgp_types.PeerTypeEnum>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers
                	**type**\: :py:class:`RemovePrivateAsOptionEnum <ydk.models.bgp.bgp_types.RemovePrivateAsOptionEnum>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\: :py:class:`CommunityTypeEnum <ydk.models.bgp.bgp_types.CommunityTypeEnum>`
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: peer_group
                
                	The peer\-group with which this neighbor is associated
                	**type**\: str
                
                .. attribute:: neighbor_address
                
                	Address of the BGP peer, either in IPv4 or IPv6
                	**type**\: one of the below types:
                
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: session_state
                
                	Operational state of the BGP peer
                	**type**\: :py:class:`SessionStateEnum <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State.SessionStateEnum>`
                
                .. attribute:: supported_capabilities
                
                	BGP capabilities negotiated as supported with the peer
                	**type**\: list of str
                
                .. attribute:: messages
                
                	Counters for BGP messages sent and received from the neighbor
                	**type**\: :py:class:`Messages <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State.Messages>`
                
                .. attribute:: queues
                
                	Counters related to queued messages associated with the BGP neighbor
                	**type**\: :py:class:`Queues <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State.Queues>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.peer_group = None
                    self.neighbor_address = None
                    self.session_state = None
                    self.supported_capabilities = YLeafList()
                    self.supported_capabilities.parent = self
                    self.supported_capabilities.name = 'supported_capabilities'
                    self.messages = Bgp.Neighbors.Neighbor.State.Messages()
                    self.messages.parent = self
                    self.queues = Bgp.Neighbors.Neighbor.State.Queues()
                    self.queues.parent = self

                class SessionStateEnum(Enum):
                    """
                    SessionStateEnum

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

                    IDLE = 0

                    CONNECT = 1

                    ACTIVE = 2

                    OPENSENT = 3

                    OPENCONFIRM = 4

                    ESTABLISHED = 5


                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.State.SessionStateEnum']



                class Messages(object):
                    """
                    Counters for BGP messages sent and received from the
                    neighbor
                    
                    .. attribute:: sent
                    
                    	Counters relating to BGP messages sent to the neighbor
                    	**type**\: :py:class:`Sent <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State.Messages.Sent>`
                    
                    .. attribute:: received
                    
                    	Counters for BGP messages received from the neighbor
                    	**type**\: :py:class:`Received <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.State.Messages.Received>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.sent = Bgp.Neighbors.Neighbor.State.Messages.Sent()
                        self.sent.parent = self
                        self.received = Bgp.Neighbors.Neighbor.State.Messages.Received()
                        self.received.parent = self


                    class Sent(object):
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

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.update = None
                            self.notification = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.update is not None:
                                return True

                            if self.notification is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.State.Messages.Sent']['meta_info']


                    class Received(object):
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

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.update = None
                            self.notification = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.update is not None:
                                return True

                            if self.notification is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.State.Messages.Received']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:messages'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.sent is not None and self.sent._has_data():
                            return True

                        if self.received is not None and self.received._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.State.Messages']['meta_info']


                class Queues(object):
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

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.input = None
                        self.output = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:queues'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.input is not None:
                            return True

                        if self.output is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.State.Queues']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer_as is not None:
                        return True

                    if self.local_as is not None:
                        return True

                    if self.peer_type is not None:
                        return True

                    if self.auth_password is not None:
                        return True

                    if self.remove_private_as is not None:
                        return True

                    if self.route_flap_damping is not None:
                        return True

                    if self.send_community is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.peer_group is not None:
                        return True

                    if self.neighbor_address is not None:
                        return True

                    if self.session_state is not None:
                        return True

                    if self.supported_capabilities is not None:
                        for child in self.supported_capabilities:
                            if child is not None:
                                return True

                    if self.messages is not None and self.messages._has_data():
                        return True

                    if self.queues is not None and self.queues._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.State']['meta_info']


            class Timers(object):
                """
                Timers related to a BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to timers used for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Timers.Config>`
                
                .. attribute:: state
                
                	State information relating to the timers used for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Timers.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.Timers.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.Timers.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to timers used for the
                    BGP neighbor or group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connect_retry is not None:
                            return True

                        if self.hold_time is not None:
                            return True

                        if self.keepalive_interval is not None:
                            return True

                        if self.minimum_advertisement_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.Timers.Config']['meta_info']


                class State(object):
                    """
                    State information relating to the timers used for the BGP
                    neighbor or group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: uptime
                    
                    	This timer determines the amount of time since the BGP last transitioned in or out of the Established state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: negotiated_hold_time
                    
                    	The negotiated hold\-time for the BGP session
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None
                        self.uptime = None
                        self.negotiated_hold_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connect_retry is not None:
                            return True

                        if self.hold_time is not None:
                            return True

                        if self.keepalive_interval is not None:
                            return True

                        if self.minimum_advertisement_interval is not None:
                            return True

                        if self.uptime is not None:
                            return True

                        if self.negotiated_hold_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.Timers.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.Timers']['meta_info']


            class Transport(object):
                """
                Transport session parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to the transport session(s) used for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Transport.Config>`
                
                .. attribute:: state
                
                	State information relating to the transport session(s) used for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.Transport.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.Transport.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.Transport.State()
                    self.state.parent = self


                class Config(object):
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
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    
                    ----
                    	**type**\: str
                    
                    
                    ----
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_mss is not None:
                            return True

                        if self.mtu_discovery is not None:
                            return True

                        if self.passive_mode is not None:
                            return True

                        if self.local_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.Transport.Config']['meta_info']


                class State(object):
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
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    
                    ----
                    	**type**\: str
                    
                    
                    ----
                    .. attribute:: local_port
                    
                    	Local TCP port being used for the TCP session supporting the BGP session
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: remote_address
                    
                    	Remote address to which the BGP session has been established
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: remote_port
                    
                    	Remote port being used by the peer for the TCP session supporting the BGP session
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None
                        self.local_port = None
                        self.remote_address = None
                        self.remote_port = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_mss is not None:
                            return True

                        if self.mtu_discovery is not None:
                            return True

                        if self.passive_mode is not None:
                            return True

                        if self.local_address is not None:
                            return True

                        if self.local_port is not None:
                            return True

                        if self.remote_address is not None:
                            return True

                        if self.remote_port is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.Transport.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:transport'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.Transport']['meta_info']


            class ErrorHandling(object):
                """
                Error handling parameters used for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying the behavior or enhanced error handling mechanisms for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ErrorHandling.Config>`
                
                .. attribute:: state
                
                	State information relating to enhanced error handling mechanisms for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ErrorHandling.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.ErrorHandling.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.ErrorHandling.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters enabling or modifying the
                    behavior or enhanced error handling mechanisms for the BGP
                    neighbor or group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.treat_as_withdraw = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.treat_as_withdraw is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.ErrorHandling.Config']['meta_info']


                class State(object):
                    """
                    State information relating to enhanced error handling
                    mechanisms for the BGP neighbor or group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    .. attribute:: erroneous_update_messages
                    
                    	The number of BGP UPDATE messages for which the treat\-as\-withdraw mechanism has been applied based on erroneous message contents
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.treat_as_withdraw = None
                        self.erroneous_update_messages = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.treat_as_withdraw is not None:
                            return True

                        if self.erroneous_update_messages is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.ErrorHandling.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:error-handling'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.ErrorHandling']['meta_info']


            class LoggingOptions(object):
                """
                Logging options for events related to the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying logging for events relating to the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.LoggingOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to logging for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.LoggingOptions.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.LoggingOptions.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.LoggingOptions.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters enabling or modifying logging
                    for events relating to the BGP neighbor or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.log_neighbor_state_changes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.log_neighbor_state_changes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.LoggingOptions.Config']['meta_info']


                class State(object):
                    """
                    State information relating to logging for the BGP neighbor
                    or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.log_neighbor_state_changes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.log_neighbor_state_changes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.LoggingOptions.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:logging-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.LoggingOptions']['meta_info']


            class EbgpMultihop(object):
                """
                eBGP multi\-hop parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multihop for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.EbgpMultihop.Config>`
                
                .. attribute:: state
                
                	State information for eBGP multihop, for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.EbgpMultihop.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.EbgpMultihop.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.EbgpMultihop.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to eBGP multihop for the
                    BGP neighbor or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.multihop_ttl = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.multihop_ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop.Config']['meta_info']


                class State(object):
                    """
                    State information for eBGP multihop, for the BGP neighbor
                    or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.multihop_ttl = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.multihop_ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:ebgp-multihop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop']['meta_info']


            class RouteReflector(object):
                """
                Route reflector parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuraton parameters relating to route reflection for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.RouteReflector.Config>`
                
                .. attribute:: state
                
                	State information relating to route reflection for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.RouteReflector.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.RouteReflector.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.RouteReflector.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuraton parameters relating to route reflection
                    for the BGP neighbor or group
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: one of the below types:
                    
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_reflector_cluster_id is not None:
                            return True

                        if self.route_reflector_client is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.RouteReflector.Config']['meta_info']


                class State(object):
                    """
                    State information relating to route reflection for the
                    BGP neighbor or group
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: one of the below types:
                    
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_reflector_cluster_id is not None:
                            return True

                        if self.route_reflector_client is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.RouteReflector.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:route-reflector'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.RouteReflector']['meta_info']


            class AsPathOptions(object):
                """
                AS\_PATH manipulation parameters for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters relating to AS\_PATH manipulation for the BGP peer or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AsPathOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to the AS\_PATH manipulation mechanisms for the BGP peer or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AsPathOptions.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.AsPathOptions.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.AsPathOptions.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to AS\_PATH manipulation
                    for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_own_as = None
                        self.replace_peer_as = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_own_as is not None:
                            return True

                        if self.replace_peer_as is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.AsPathOptions.Config']['meta_info']


                class State(object):
                    """
                    State information relating to the AS\_PATH manipulation
                    mechanisms for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_own_as = None
                        self.replace_peer_as = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_own_as is not None:
                            return True

                        if self.replace_peer_as is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.AsPathOptions.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:as-path-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.AsPathOptions']['meta_info']


            class AddPaths(object):
                """
                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add\-paths)
                
                .. attribute:: config
                
                	Configuration parameters relating to ADD\_PATHS
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AddPaths.Config>`
                
                .. attribute:: state
                
                	State information associated with ADD\_PATHS
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AddPaths.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.AddPaths.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.AddPaths.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.receive = None
                        self.send_max = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.receive is not None:
                            return True

                        if self.send_max is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.AddPaths.Config']['meta_info']


                class State(object):
                    """
                    State information associated with ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.receive = None
                        self.send_max = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.receive is not None:
                            return True

                        if self.send_max is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.AddPaths.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:add-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.AddPaths']['meta_info']


            class AfiSafis(object):
                """
                Per\-address\-family configuration parameters associated with
                the neighbor or group
                
                .. attribute:: afi_safi
                
                	AFI,SAFI configuration available for the neighbour or group
                	**type**\: list of :py:class:`AfiSafi <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.afi_safi = YList()
                    self.afi_safi.parent = self
                    self.afi_safi.name = 'afi_safi'


                class AfiSafi(object):
                    """
                    AFI,SAFI configuration available for the
                    neighbour or group
                    
                    .. attribute:: afi_safi_name  <key>
                    
                    	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                    	**type**\: str
                    
                    .. attribute:: graceful_restart
                    
                    	Parameters relating to BGP graceful\-restart
                    	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the AFI\-SAFI
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to the AFI\-SAFI
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State>`
                    
                    .. attribute:: apply_policy
                    
                    	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                    	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy>`
                    
                    .. attribute:: ipv4_unicast
                    
                    	IPv4 unicast configuration options
                    	**type**\: :py:class:`Ipv4Unicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast>`
                    
                    .. attribute:: ipv6_unicast
                    
                    	IPv6 unicast configuration options
                    	**type**\: :py:class:`Ipv6Unicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast>`
                    
                    .. attribute:: ipv4_labelled_unicast
                    
                    	IPv4 Labelled Unicast configuration options
                    	**type**\: :py:class:`Ipv4LabelledUnicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast>`
                    
                    .. attribute:: ipv6_labelled_unicast
                    
                    	IPv6 Labelled Unicast configuration options
                    	**type**\: :py:class:`Ipv6LabelledUnicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast>`
                    
                    .. attribute:: l3vpn_ipv4_unicast
                    
                    	Unicast IPv4 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv4Unicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                    
                    .. attribute:: l3vpn_ipv6_unicast
                    
                    	Unicast IPv6 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv6Unicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                    
                    .. attribute:: l3vpn_ipv4_multicast
                    
                    	Multicast IPv4 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv4Multicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                    
                    .. attribute:: l3vpn_ipv6_multicast
                    
                    	Multicast IPv6 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv6Multicast <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                    
                    .. attribute:: l2vpn_vpls
                    
                    	BGP\-signalled VPLS configuration options
                    	**type**\: :py:class:`L2VpnVpls <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls>`
                    
                    .. attribute:: l2vpn_evpn
                    
                    	BGP EVPN configuration options
                    	**type**\: :py:class:`L2VpnEvpn <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn>`
                    
                    .. attribute:: use_multiple_paths
                    
                    	Parameters related to the use of multiple\-paths for the same NLRI when they are received only from this neighbor
                    	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.afi_safi_name = None
                        self.graceful_restart = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart()
                        self.graceful_restart.parent = self
                        self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config()
                        self.config.parent = self
                        self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State()
                        self.state.parent = self
                        self.apply_policy = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy()
                        self.apply_policy.parent = self
                        self.ipv4_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self.ipv6_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self.ipv4_labelled_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast()
                        self.ipv4_labelled_unicast.parent = self
                        self.ipv6_labelled_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast()
                        self.ipv6_labelled_unicast.parent = self
                        self.l3vpn_ipv4_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                        self.l3vpn_ipv4_unicast.parent = self
                        self.l3vpn_ipv6_unicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                        self.l3vpn_ipv6_unicast.parent = self
                        self.l3vpn_ipv4_multicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                        self.l3vpn_ipv4_multicast.parent = self
                        self.l3vpn_ipv6_multicast = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                        self.l3vpn_ipv6_multicast.parent = self
                        self.l2vpn_vpls = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls()
                        self.l2vpn_vpls.parent = self
                        self.l2vpn_evpn = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn()
                        self.l2vpn_evpn.parent = self
                        self.use_multiple_paths = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths()
                        self.use_multiple_paths.parent = self


                    class GracefulRestart(object):
                        """
                        Parameters relating to BGP graceful\-restart
                        
                        .. attribute:: config
                        
                        	Configuration options for BGP graceful\-restart
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config>`
                        
                        .. attribute:: state
                        
                        	State information for BGP graceful\-restart
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config()
                            self.config.parent = self
                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration options for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info']


                        class State(object):
                            """
                            State information for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            .. attribute:: received
                            
                            	This leaf indicates whether the neighbor advertised the ability to support graceful\-restart for this AFI\-SAFI
                            	**type**\: bool
                            
                            .. attribute:: advertised
                            
                            	This leaf indicates whether the ability to support graceful\-restart has been advertised to the peer
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None
                                self.received = None
                                self.advertised = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                if self.received is not None:
                                    return True

                                if self.advertised is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:graceful-restart'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart']['meta_info']


                    class Config(object):
                        """
                        Configuration parameters for the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\: str
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.afi_safi_name = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.afi_safi_name is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config']['meta_info']


                    class State(object):
                        """
                        State information relating to the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\: str
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        .. attribute:: active
                        
                        	This value indicates whether a particular AFI\-SAFI has been succesfully negotiated with the peer. An AFI\-SAFI may be enabled in the current running configuration, but a session restart may be required in order to negotiate the new capability
                        	**type**\: bool
                        
                        .. attribute:: prefixes
                        
                        	Prefix counters for the BGP session
                        	**type**\: :py:class:`Prefixes <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.afi_safi_name = None
                            self.enabled = None
                            self.active = None
                            self.prefixes = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes()
                            self.prefixes.parent = self


                        class Prefixes(object):
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

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.received = None
                                self.sent = None
                                self.installed = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefixes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.received is not None:
                                    return True

                                if self.sent is not None:
                                    return True

                                if self.installed is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.afi_safi_name is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            if self.active is not None:
                                return True

                            if self.prefixes is not None and self.prefixes._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State']['meta_info']


                    class ApplyPolicy(object):
                        """
                        Anchor point for routing policies in the model.
                        Import and export policies are with respect to the local
                        routing table, i.e., export (send) and import (receive),
                        depending on the context.
                        
                        .. attribute:: config
                        
                        	Policy configuration data
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for routing policy
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config()
                            self.config.parent = self
                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Policy configuration data.
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.import_policy = YLeafList()
                                self.import_policy.parent = self
                                self.import_policy.name = 'import_policy'
                                self.default_import_policy = None
                                self.export_policy = YLeafList()
                                self.export_policy.parent = self
                                self.export_policy.name = 'export_policy'
                                self.default_export_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.import_policy is not None:
                                    for child in self.import_policy:
                                        if child is not None:
                                            return True

                                if self.default_import_policy is not None:
                                    return True

                                if self.export_policy is not None:
                                    for child in self.export_policy:
                                        if child is not None:
                                            return True

                                if self.default_export_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info']


                        class State(object):
                            """
                            Operational state for routing policy
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.import_policy = YLeafList()
                                self.import_policy.parent = self
                                self.import_policy.name = 'import_policy'
                                self.default_import_policy = None
                                self.export_policy = YLeafList()
                                self.export_policy.parent = self
                                self.export_policy.name = 'export_policy'
                                self.default_export_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.import_policy is not None:
                                    for child in self.import_policy:
                                        if child is not None:
                                            return True

                                if self.default_import_policy is not None:
                                    return True

                                if self.export_policy is not None:
                                    for child in self.export_policy:
                                        if child is not None:
                                            return True

                                if self.default_export_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:apply-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']


                    class Ipv4Unicast(object):
                        """
                        IPv4 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                            self.config.parent = self
                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State()
                            self.state.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info']


                        class State(object):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv4-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']


                    class Ipv6Unicast(object):
                        """
                        IPv6 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                            self.config.parent = self
                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State()
                            self.state.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info']


                        class State(object):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv6-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']


                    class Ipv4LabelledUnicast(object):
                        """
                        IPv4 Labelled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv4-labelled-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']


                    class Ipv6LabelledUnicast(object):
                        """
                        IPv6 Labelled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv6-labelled-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']


                    class L3VpnIpv4Unicast(object):
                        """
                        Unicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv4-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']


                    class L3VpnIpv6Unicast(object):
                        """
                        Unicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv6-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']


                    class L3VpnIpv4Multicast(object):
                        """
                        Multicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv4-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']


                    class L3VpnIpv6Multicast(object):
                        """
                        Multicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv6-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']


                    class L2VpnVpls(object):
                        """
                        BGP\-signalled VPLS configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l2vpn-vpls'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']


                    class L2VpnEvpn(object):
                        """
                        BGP EVPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l2vpn-evpn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']


                    class UseMultiplePaths(object):
                        """
                        Parameters related to the use of multiple\-paths for the same
                        NLRI when they are received only from this neighbor
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to multipath
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to multipath
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                        
                        .. attribute:: ebgp
                        
                        	Multipath configuration for eBGP
                        	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                            self.config.parent = self
                            self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State()
                            self.state.parent = self
                            self.ebgp = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                            self.ebgp.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info']


                        class State(object):
                            """
                            State parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info']


                        class Ebgp(object):
                            """
                            Multipath configuration for eBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to eBGP multipath
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to eBGP multipath
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                                self.config.parent = self
                                self.state = Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration parameters relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.allow_multiple_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.allow_multiple_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info']


                            class State(object):
                                """
                                State information relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.allow_multiple_as = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.allow_multiple_as is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:ebgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:use-multiple-paths'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.ebgp is not None and self.ebgp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.afi_safi_name is None:
                            raise YPYDataValidationError('Key property afi_safi_name is None')

                        return self.parent._common_path +'/bgp:afi-safi[bgp:afi-safi-name = ' + str(self.afi_safi_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.afi_safi_name is not None:
                            return True

                        if self.graceful_restart is not None and self.graceful_restart._has_data():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.apply_policy is not None and self.apply_policy._has_data():
                            return True

                        if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                            return True

                        if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                            return True

                        if self.ipv4_labelled_unicast is not None and self.ipv4_labelled_unicast._has_data():
                            return True

                        if self.ipv6_labelled_unicast is not None and self.ipv6_labelled_unicast._has_data():
                            return True

                        if self.l3vpn_ipv4_unicast is not None and self.l3vpn_ipv4_unicast._has_data():
                            return True

                        if self.l3vpn_ipv6_unicast is not None and self.l3vpn_ipv6_unicast._has_data():
                            return True

                        if self.l3vpn_ipv4_multicast is not None and self.l3vpn_ipv4_multicast._has_data():
                            return True

                        if self.l3vpn_ipv6_multicast is not None and self.l3vpn_ipv6_multicast._has_data():
                            return True

                        if self.l2vpn_vpls is not None and self.l2vpn_vpls._has_data():
                            return True

                        if self.l2vpn_evpn is not None and self.l2vpn_evpn._has_data():
                            return True

                        if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:afi-safis'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.afi_safi is not None:
                        for child_ref in self.afi_safi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.AfiSafis']['meta_info']


            class GracefulRestart(object):
                """
                Parameters relating the graceful restart mechanism for BGP
                
                .. attribute:: config
                
                	Configuration parameters relating to graceful\-restart
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.GracefulRestart.Config>`
                
                .. attribute:: state
                
                	State information associated with graceful\-restart
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.GracefulRestart.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.GracefulRestart.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.GracefulRestart.State()
                    self.state.parent = self


                class Config(object):
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
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.restart_time is not None:
                            return True

                        if self.stale_routes_time is not None:
                            return True

                        if self.helper_only is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.GracefulRestart.Config']['meta_info']


                class State(object):
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
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
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
                    	**type**\: :py:class:`ModeEnum <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.GracefulRestart.State.ModeEnum>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None
                        self.peer_restart_time = None
                        self.peer_restarting = None
                        self.local_restarting = None
                        self.mode = None

                    class ModeEnum(Enum):
                        """
                        ModeEnum

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

                        HELPER_ONLY = 0

                        BILATERAL = 1

                        REMOTE_HELPER = 2


                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.GracefulRestart.State.ModeEnum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.restart_time is not None:
                            return True

                        if self.stale_routes_time is not None:
                            return True

                        if self.helper_only is not None:
                            return True

                        if self.peer_restart_time is not None:
                            return True

                        if self.peer_restarting is not None:
                            return True

                        if self.local_restarting is not None:
                            return True

                        if self.mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.GracefulRestart.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:graceful-restart'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.GracefulRestart']['meta_info']


            class ApplyPolicy(object):
                """
                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                
                .. attribute:: config
                
                	Policy configuration data
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ApplyPolicy.Config>`
                
                .. attribute:: state
                
                	Operational state for routing policy
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.ApplyPolicy.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.ApplyPolicy.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.ApplyPolicy.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Policy configuration data.
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.import_policy = YLeafList()
                        self.import_policy.parent = self
                        self.import_policy.name = 'import_policy'
                        self.default_import_policy = None
                        self.export_policy = YLeafList()
                        self.export_policy.parent = self
                        self.export_policy.name = 'export_policy'
                        self.default_export_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.import_policy is not None:
                            for child in self.import_policy:
                                if child is not None:
                                    return True

                        if self.default_import_policy is not None:
                            return True

                        if self.export_policy is not None:
                            for child in self.export_policy:
                                if child is not None:
                                    return True

                        if self.default_export_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy.Config']['meta_info']


                class State(object):
                    """
                    Operational state for routing policy
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.import_policy = YLeafList()
                        self.import_policy.parent = self
                        self.import_policy.name = 'import_policy'
                        self.default_import_policy = None
                        self.export_policy = YLeafList()
                        self.export_policy.parent = self
                        self.export_policy.name = 'export_policy'
                        self.default_export_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.import_policy is not None:
                            for child in self.import_policy:
                                if child is not None:
                                    return True

                        if self.default_import_policy is not None:
                            return True

                        if self.export_policy is not None:
                            for child in self.export_policy:
                                if child is not None:
                                    return True

                        if self.default_export_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:apply-policy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy']['meta_info']


            class UseMultiplePaths(object):
                """
                Parameters related to the use of multiple\-paths for the same
                NLRI when they are received only from this neighbor
                
                .. attribute:: config
                
                	Configuration parameters relating to multipath
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Config>`
                
                .. attribute:: state
                
                	State parameters relating to multipath
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.State>`
                
                .. attribute:: ebgp
                
                	Multipath configuration for eBGP
                	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.Neighbors.Neighbor.UseMultiplePaths.Config()
                    self.config.parent = self
                    self.state = Bgp.Neighbors.Neighbor.UseMultiplePaths.State()
                    self.state.parent = self
                    self.ebgp = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp()
                    self.ebgp.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Config']['meta_info']


                class State(object):
                    """
                    State parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.State']['meta_info']


                class Ebgp(object):
                    """
                    Multipath configuration for eBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to eBGP multipath
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to eBGP multipath
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config()
                        self.config.parent = self
                        self.state = Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.allow_multiple_as = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allow_multiple_as is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config']['meta_info']


                    class State(object):
                        """
                        State information relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.allow_multiple_as = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allow_multiple_as is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ebgp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:use-multiple-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.ebgp is not None and self.ebgp._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths']['meta_info']

            @property
            def _common_path(self):
                if self.neighbor_address is None:
                    raise YPYDataValidationError('Key property neighbor_address is None')

                return '/bgp:bgp/bgp:neighbors/bgp:neighbor[bgp:neighbor-address = ' + str(self.neighbor_address) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.neighbor_address is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.timers is not None and self.timers._has_data():
                    return True

                if self.transport is not None and self.transport._has_data():
                    return True

                if self.error_handling is not None and self.error_handling._has_data():
                    return True

                if self.logging_options is not None and self.logging_options._has_data():
                    return True

                if self.ebgp_multihop is not None and self.ebgp_multihop._has_data():
                    return True

                if self.route_reflector is not None and self.route_reflector._has_data():
                    return True

                if self.as_path_options is not None and self.as_path_options._has_data():
                    return True

                if self.add_paths is not None and self.add_paths._has_data():
                    return True

                if self.afi_safis is not None and self.afi_safis._has_data():
                    return True

                if self.graceful_restart is not None and self.graceful_restart._has_data():
                    return True

                if self.apply_policy is not None and self.apply_policy._has_data():
                    return True

                if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.Neighbors.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/bgp:bgp/bgp:neighbors'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp._meta import _bgp as meta
            return meta._meta_table['Bgp.Neighbors']['meta_info']


    class PeerGroups(object):
        """
        Configuration for BGP peer\-groups
        
        .. attribute:: peer_group
        
        	List of BGP peer\-groups configured on the local system \- uniquely identified by peer\-group name
        	**type**\: list of :py:class:`PeerGroup <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup>`
        
        

        """

        _prefix = 'bgp'
        _revision = '2015-05-15'

        def __init__(self):
            self.parent = None
            self.peer_group = YList()
            self.peer_group.parent = self
            self.peer_group.name = 'peer_group'


        class PeerGroup(object):
            """
            List of BGP peer\-groups configured on the local system \-
            uniquely identified by peer\-group name
            
            .. attribute:: peer_group_name  <key>
            
            	Reference to the name of the BGP peer\-group used as a key in the peer\-group list
            	**type**\: str
            
            .. attribute:: config
            
            	Configuration parameters relating to the BGP neighbor or group
            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Config>`
            
            .. attribute:: state
            
            	State information relating to the BGP neighbor or group
            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.State>`
            
            .. attribute:: timers
            
            	Timers related to a BGP neighbor or group
            	**type**\: :py:class:`Timers <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Timers>`
            
            .. attribute:: transport
            
            	Transport session parameters for the BGP neighbor or group
            	**type**\: :py:class:`Transport <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Transport>`
            
            .. attribute:: error_handling
            
            	Error handling parameters used for the BGP neighbor or group
            	**type**\: :py:class:`ErrorHandling <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling>`
            
            .. attribute:: logging_options
            
            	Logging options for events related to the BGP neighbor or group
            	**type**\: :py:class:`LoggingOptions <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions>`
            
            .. attribute:: ebgp_multihop
            
            	eBGP multi\-hop parameters for the BGP neighbor or group
            	**type**\: :py:class:`EbgpMultihop <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop>`
            
            .. attribute:: route_reflector
            
            	Route reflector parameters for the BGP neighbor or group
            	**type**\: :py:class:`RouteReflector <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.RouteReflector>`
            
            .. attribute:: as_path_options
            
            	AS\_PATH manipulation parameters for the BGP neighbor or group
            	**type**\: :py:class:`AsPathOptions <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions>`
            
            .. attribute:: add_paths
            
            	Parameters relating to the advertisement and receipt of multiple paths for a single NLRI (add\-paths)
            	**type**\: :py:class:`AddPaths <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AddPaths>`
            
            .. attribute:: afi_safis
            
            	Per\-address\-family configuration parameters associated with the neighbor or group
            	**type**\: :py:class:`AfiSafis <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis>`
            
            .. attribute:: graceful_restart
            
            	Parameters relating the graceful restart mechanism for BGP
            	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart>`
            
            .. attribute:: apply_policy
            
            	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
            	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy>`
            
            .. attribute:: use_multiple_paths
            
            	Parameters related to the use of multiple paths for the same NLRI
            	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths>`
            
            

            """

            _prefix = 'bgp'
            _revision = '2015-05-15'

            def __init__(self):
                self.parent = None
                self.peer_group_name = None
                self.config = Bgp.PeerGroups.PeerGroup.Config()
                self.config.parent = self
                self.state = Bgp.PeerGroups.PeerGroup.State()
                self.state.parent = self
                self.timers = Bgp.PeerGroups.PeerGroup.Timers()
                self.timers.parent = self
                self.transport = Bgp.PeerGroups.PeerGroup.Transport()
                self.transport.parent = self
                self.error_handling = Bgp.PeerGroups.PeerGroup.ErrorHandling()
                self.error_handling.parent = self
                self.logging_options = Bgp.PeerGroups.PeerGroup.LoggingOptions()
                self.logging_options.parent = self
                self.ebgp_multihop = Bgp.PeerGroups.PeerGroup.EbgpMultihop()
                self.ebgp_multihop.parent = self
                self.route_reflector = Bgp.PeerGroups.PeerGroup.RouteReflector()
                self.route_reflector.parent = self
                self.as_path_options = Bgp.PeerGroups.PeerGroup.AsPathOptions()
                self.as_path_options.parent = self
                self.add_paths = Bgp.PeerGroups.PeerGroup.AddPaths()
                self.add_paths.parent = self
                self.afi_safis = Bgp.PeerGroups.PeerGroup.AfiSafis()
                self.afi_safis.parent = self
                self.graceful_restart = Bgp.PeerGroups.PeerGroup.GracefulRestart()
                self.graceful_restart.parent = self
                self.apply_policy = Bgp.PeerGroups.PeerGroup.ApplyPolicy()
                self.apply_policy.parent = self
                self.use_multiple_paths = Bgp.PeerGroups.PeerGroup.UseMultiplePaths()
                self.use_multiple_paths.parent = self


            class Config(object):
                """
                Configuration parameters relating to the BGP neighbor or
                group
                
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
                	**type**\: :py:class:`PeerTypeEnum <ydk.models.bgp.bgp_types.PeerTypeEnum>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers
                	**type**\: :py:class:`RemovePrivateAsOptionEnum <ydk.models.bgp.bgp_types.RemovePrivateAsOptionEnum>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\: :py:class:`CommunityTypeEnum <ydk.models.bgp.bgp_types.CommunityTypeEnum>`
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: peer_group_name
                
                	Name of the BGP peer\-group
                	**type**\: str
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.peer_group_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer_as is not None:
                        return True

                    if self.local_as is not None:
                        return True

                    if self.peer_type is not None:
                        return True

                    if self.auth_password is not None:
                        return True

                    if self.remove_private_as is not None:
                        return True

                    if self.route_flap_damping is not None:
                        return True

                    if self.send_community is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.peer_group_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.Config']['meta_info']


            class State(object):
                """
                State information relating to the BGP neighbor or group
                
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
                	**type**\: :py:class:`PeerTypeEnum <ydk.models.bgp.bgp_types.PeerTypeEnum>`
                
                .. attribute:: auth_password
                
                	Configures an MD5 authentication password for use with neighboring devices
                	**type**\: str
                
                .. attribute:: remove_private_as
                
                	Remove private AS numbers from updates sent to peers
                	**type**\: :py:class:`RemovePrivateAsOptionEnum <ydk.models.bgp.bgp_types.RemovePrivateAsOptionEnum>`
                
                .. attribute:: route_flap_damping
                
                	Enable route flap damping
                	**type**\: bool
                
                .. attribute:: send_community
                
                	Specify which types of community should be sent to the neighbor or group. The default is to not send the community attribute
                	**type**\: :py:class:`CommunityTypeEnum <ydk.models.bgp.bgp_types.CommunityTypeEnum>`
                
                .. attribute:: description
                
                	An optional textual description (intended primarily for use with a peer or group
                	**type**\: str
                
                .. attribute:: peer_group_name
                
                	Name of the BGP peer\-group
                	**type**\: str
                
                .. attribute:: total_paths
                
                	Total number of BGP paths within the context
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_prefixes
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.peer_as = None
                    self.local_as = None
                    self.peer_type = None
                    self.auth_password = None
                    self.remove_private_as = None
                    self.route_flap_damping = None
                    self.send_community = None
                    self.description = None
                    self.peer_group_name = None
                    self.total_paths = None
                    self.total_prefixes = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer_as is not None:
                        return True

                    if self.local_as is not None:
                        return True

                    if self.peer_type is not None:
                        return True

                    if self.auth_password is not None:
                        return True

                    if self.remove_private_as is not None:
                        return True

                    if self.route_flap_damping is not None:
                        return True

                    if self.send_community is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.peer_group_name is not None:
                        return True

                    if self.total_paths is not None:
                        return True

                    if self.total_prefixes is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.State']['meta_info']


            class Timers(object):
                """
                Timers related to a BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to timers used for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Timers.Config>`
                
                .. attribute:: state
                
                	State information relating to the timers used for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Timers.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.Timers.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.Timers.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to timers used for the
                    BGP neighbor or group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connect_retry is not None:
                            return True

                        if self.hold_time is not None:
                            return True

                        if self.keepalive_interval is not None:
                            return True

                        if self.minimum_advertisement_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.Timers.Config']['meta_info']


                class State(object):
                    """
                    State information relating to the timers used for the BGP
                    neighbor or group
                    
                    .. attribute:: connect_retry
                    
                    	Time interval in seconds between attempts to establish a session with the peer
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: hold_time
                    
                    	Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  The hold\-time is typically set to 3x the keepalive\-interval
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: keepalive_interval
                    
                    	Time interval in seconds between transmission of keepalive messages to the neighbor.  Typically set to 1/3 the hold\-time
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: minimum_advertisement_interval
                    
                    	Minimum time which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.connect_retry = None
                        self.hold_time = None
                        self.keepalive_interval = None
                        self.minimum_advertisement_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.connect_retry is not None:
                            return True

                        if self.hold_time is not None:
                            return True

                        if self.keepalive_interval is not None:
                            return True

                        if self.minimum_advertisement_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.Timers.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.Timers']['meta_info']


            class Transport(object):
                """
                Transport session parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to the transport session(s) used for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Transport.Config>`
                
                .. attribute:: state
                
                	State information relating to the transport session(s) used for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.Transport.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.Transport.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.Transport.State()
                    self.state.parent = self


                class Config(object):
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
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    
                    ----
                    	**type**\: str
                    
                    
                    ----
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_mss is not None:
                            return True

                        if self.mtu_discovery is not None:
                            return True

                        if self.passive_mode is not None:
                            return True

                        if self.local_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.Transport.Config']['meta_info']


                class State(object):
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
                    
                    .. attribute:: passive_mode
                    
                    	Wait for peers to issue requests to open a BGP session, rather than initiating sessions from the local router
                    	**type**\: bool
                    
                    .. attribute:: local_address
                    
                    	Set the local IP (either IPv4 or IPv6) address to use for the session when sending BGP update messages.  This may be expressed as either an IP address or reference to the name of an interface
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    
                    ----
                    	**type**\: str
                    
                    
                    ----
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.tcp_mss = None
                        self.mtu_discovery = None
                        self.passive_mode = None
                        self.local_address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_mss is not None:
                            return True

                        if self.mtu_discovery is not None:
                            return True

                        if self.passive_mode is not None:
                            return True

                        if self.local_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.Transport.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:transport'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.Transport']['meta_info']


            class ErrorHandling(object):
                """
                Error handling parameters used for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying the behavior or enhanced error handling mechanisms for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling.Config>`
                
                .. attribute:: state
                
                	State information relating to enhanced error handling mechanisms for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ErrorHandling.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.ErrorHandling.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.ErrorHandling.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters enabling or modifying the
                    behavior or enhanced error handling mechanisms for the BGP
                    neighbor or group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.treat_as_withdraw = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.treat_as_withdraw is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling.Config']['meta_info']


                class State(object):
                    """
                    State information relating to enhanced error handling
                    mechanisms for the BGP neighbor or group
                    
                    .. attribute:: treat_as_withdraw
                    
                    	Specify whether erroneous UPDATE messages for which the NLRI can be extracted are reated as though the NLRI is withdrawn \- avoiding session reset
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.treat_as_withdraw = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.treat_as_withdraw is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:error-handling'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling']['meta_info']


            class LoggingOptions(object):
                """
                Logging options for events related to the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters enabling or modifying logging for events relating to the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to logging for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.LoggingOptions.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.LoggingOptions.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.LoggingOptions.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters enabling or modifying logging
                    for events relating to the BGP neighbor or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.log_neighbor_state_changes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.log_neighbor_state_changes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions.Config']['meta_info']


                class State(object):
                    """
                    State information relating to logging for the BGP neighbor
                    or group
                    
                    .. attribute:: log_neighbor_state_changes
                    
                    	Configure logging of peer state changes.  Default is to enable logging of peer state changes
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.log_neighbor_state_changes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.log_neighbor_state_changes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:logging-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions']['meta_info']


            class EbgpMultihop(object):
                """
                eBGP multi\-hop parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuration parameters relating to eBGP multihop for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config>`
                
                .. attribute:: state
                
                	State information for eBGP multihop, for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.EbgpMultihop.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.EbgpMultihop.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to eBGP multihop for the
                    BGP neighbor or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.multihop_ttl = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.multihop_ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config']['meta_info']


                class State(object):
                    """
                    State information for eBGP multihop, for the BGP neighbor
                    or group
                    
                    .. attribute:: enabled
                    
                    	When enabled the referenced group or neighbors are permitted to be indirectly connected \- including cases where the TTL can be decremented between the BGP peers
                    	**type**\: bool
                    
                    .. attribute:: multihop_ttl
                    
                    	Time\-to\-live value to use when packets are sent to the referenced group or neighbors and ebgp\-multihop is enabled
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.multihop_ttl = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.multihop_ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:ebgp-multihop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop']['meta_info']


            class RouteReflector(object):
                """
                Route reflector parameters for the BGP neighbor or group
                
                .. attribute:: config
                
                	Configuraton parameters relating to route reflection for the BGP neighbor or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.RouteReflector.Config>`
                
                .. attribute:: state
                
                	State information relating to route reflection for the BGP neighbor or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.RouteReflector.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.RouteReflector.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.RouteReflector.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuraton parameters relating to route reflection
                    for the BGP neighbor or group
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: one of the below types:
                    
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_reflector_cluster_id is not None:
                            return True

                        if self.route_reflector_client is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector.Config']['meta_info']


                class State(object):
                    """
                    State information relating to route reflection for the
                    BGP neighbor or group
                    
                    .. attribute:: route_reflector_cluster_id
                    
                    	route\-reflector cluster id to use when local router is configured as a route reflector.  Commonly set at the group level, but allows a different cluster id to be set for each neighbor
                    	**type**\: one of the below types:
                    
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: route_reflector_client
                    
                    	Configure the neighbor as a route reflector client
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.route_reflector_cluster_id = None
                        self.route_reflector_client = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.route_reflector_cluster_id is not None:
                            return True

                        if self.route_reflector_client is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:route-reflector'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector']['meta_info']


            class AsPathOptions(object):
                """
                AS\_PATH manipulation parameters for the BGP neighbor or
                group
                
                .. attribute:: config
                
                	Configuration parameters relating to AS\_PATH manipulation for the BGP peer or group
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions.Config>`
                
                .. attribute:: state
                
                	State information relating to the AS\_PATH manipulation mechanisms for the BGP peer or group
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AsPathOptions.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.AsPathOptions.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.AsPathOptions.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to AS\_PATH manipulation
                    for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_own_as = None
                        self.replace_peer_as = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_own_as is not None:
                            return True

                        if self.replace_peer_as is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions.Config']['meta_info']


                class State(object):
                    """
                    State information relating to the AS\_PATH manipulation
                    mechanisms for the BGP peer or group
                    
                    .. attribute:: allow_own_as
                    
                    	Specify the number of occurrences of the local BGP speaker's AS that can occur within the AS\_PATH before it is rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: replace_peer_as
                    
                    	Replace occurrences of the peer's AS in the AS\_PATH with the local autonomous system number
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.allow_own_as = None
                        self.replace_peer_as = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.allow_own_as is not None:
                            return True

                        if self.replace_peer_as is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:as-path-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions']['meta_info']


            class AddPaths(object):
                """
                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add\-paths)
                
                .. attribute:: config
                
                	Configuration parameters relating to ADD\_PATHS
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AddPaths.Config>`
                
                .. attribute:: state
                
                	State information associated with ADD\_PATHS
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AddPaths.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.AddPaths.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.AddPaths.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.receive = None
                        self.send_max = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.receive is not None:
                            return True

                        if self.send_max is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.AddPaths.Config']['meta_info']


                class State(object):
                    """
                    State information associated with ADD\_PATHS
                    
                    .. attribute:: receive
                    
                    	Enable ability to receive multiple path advertisements for an NLRI from the neighbor or group
                    	**type**\: bool
                    
                    .. attribute:: send_max
                    
                    	The maximum number of paths to advertise to neighbors for a single NLRI
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.receive = None
                        self.send_max = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.receive is not None:
                            return True

                        if self.send_max is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.AddPaths.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:add-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AddPaths']['meta_info']


            class AfiSafis(object):
                """
                Per\-address\-family configuration parameters associated with
                the neighbor or group
                
                .. attribute:: afi_safi
                
                	AFI,SAFI configuration available for the neighbour or group
                	**type**\: list of :py:class:`AfiSafi <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.afi_safi = YList()
                    self.afi_safi.parent = self
                    self.afi_safi.name = 'afi_safi'


                class AfiSafi(object):
                    """
                    AFI,SAFI configuration available for the
                    neighbour or group
                    
                    .. attribute:: afi_safi_name  <key>
                    
                    	Reference to the AFI\-SAFI name used as a key for the AFI\-SAFI list
                    	**type**\: str
                    
                    .. attribute:: graceful_restart
                    
                    	Parameters relating to BGP graceful\-restart
                    	**type**\: :py:class:`GracefulRestart <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the AFI\-SAFI
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to the AFI\-SAFI
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State>`
                    
                    .. attribute:: apply_policy
                    
                    	Anchor point for routing policies in the model. Import and export policies are with respect to the local routing table, i.e., export (send) and import (receive), depending on the context
                    	**type**\: :py:class:`ApplyPolicy <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy>`
                    
                    .. attribute:: ipv4_unicast
                    
                    	IPv4 unicast configuration options
                    	**type**\: :py:class:`Ipv4Unicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast>`
                    
                    .. attribute:: ipv6_unicast
                    
                    	IPv6 unicast configuration options
                    	**type**\: :py:class:`Ipv6Unicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast>`
                    
                    .. attribute:: ipv4_labelled_unicast
                    
                    	IPv4 Labelled Unicast configuration options
                    	**type**\: :py:class:`Ipv4LabelledUnicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast>`
                    
                    .. attribute:: ipv6_labelled_unicast
                    
                    	IPv6 Labelled Unicast configuration options
                    	**type**\: :py:class:`Ipv6LabelledUnicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast>`
                    
                    .. attribute:: l3vpn_ipv4_unicast
                    
                    	Unicast IPv4 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv4Unicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast>`
                    
                    .. attribute:: l3vpn_ipv6_unicast
                    
                    	Unicast IPv6 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv6Unicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast>`
                    
                    .. attribute:: l3vpn_ipv4_multicast
                    
                    	Multicast IPv4 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv4Multicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast>`
                    
                    .. attribute:: l3vpn_ipv6_multicast
                    
                    	Multicast IPv6 L3VPN configuration options
                    	**type**\: :py:class:`L3VpnIpv6Multicast <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast>`
                    
                    .. attribute:: l2vpn_vpls
                    
                    	BGP\-signalled VPLS configuration options
                    	**type**\: :py:class:`L2VpnVpls <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls>`
                    
                    .. attribute:: l2vpn_evpn
                    
                    	BGP EVPN configuration options
                    	**type**\: :py:class:`L2VpnEvpn <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn>`
                    
                    .. attribute:: use_multiple_paths
                    
                    	Parameters related to the use of multiple paths for the same NLRI
                    	**type**\: :py:class:`UseMultiplePaths <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths>`
                    
                    .. attribute:: route_selection_options
                    
                    	Parameters relating to options for route selection
                    	**type**\: :py:class:`RouteSelectionOptions <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.afi_safi_name = None
                        self.graceful_restart = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart()
                        self.graceful_restart.parent = self
                        self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config()
                        self.config.parent = self
                        self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State()
                        self.state.parent = self
                        self.apply_policy = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy()
                        self.apply_policy.parent = self
                        self.ipv4_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self.ipv6_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self.ipv4_labelled_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast()
                        self.ipv4_labelled_unicast.parent = self
                        self.ipv6_labelled_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast()
                        self.ipv6_labelled_unicast.parent = self
                        self.l3vpn_ipv4_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast()
                        self.l3vpn_ipv4_unicast.parent = self
                        self.l3vpn_ipv6_unicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast()
                        self.l3vpn_ipv6_unicast.parent = self
                        self.l3vpn_ipv4_multicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast()
                        self.l3vpn_ipv4_multicast.parent = self
                        self.l3vpn_ipv6_multicast = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast()
                        self.l3vpn_ipv6_multicast.parent = self
                        self.l2vpn_vpls = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls()
                        self.l2vpn_vpls.parent = self
                        self.l2vpn_evpn = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn()
                        self.l2vpn_evpn.parent = self
                        self.use_multiple_paths = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths()
                        self.use_multiple_paths.parent = self
                        self.route_selection_options = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions()
                        self.route_selection_options.parent = self


                    class GracefulRestart(object):
                        """
                        Parameters relating to BGP graceful\-restart
                        
                        .. attribute:: config
                        
                        	Configuration options for BGP graceful\-restart
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config>`
                        
                        .. attribute:: state
                        
                        	State information for BGP graceful\-restart
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration options for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info']


                        class State(object):
                            """
                            State information for BGP graceful\-restart
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates whether graceful\-restart is enabled for this AFI\-SAFI
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:graceful-restart'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart']['meta_info']


                    class Config(object):
                        """
                        Configuration parameters for the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\: str
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.afi_safi_name = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.afi_safi_name is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config']['meta_info']


                    class State(object):
                        """
                        State information relating to the AFI\-SAFI
                        
                        .. attribute:: afi_safi_name
                        
                        	AFI,SAFI
                        	**type**\: str
                        
                        .. attribute:: enabled
                        
                        	This leaf indicates whether the IPv4 Unicast AFI,SAFI is enabled for the neighbour or group
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.afi_safi_name = None
                            self.enabled = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.afi_safi_name is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State']['meta_info']


                    class ApplyPolicy(object):
                        """
                        Anchor point for routing policies in the model.
                        Import and export policies are with respect to the local
                        routing table, i.e., export (send) and import (receive),
                        depending on the context.
                        
                        .. attribute:: config
                        
                        	Policy configuration data
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for routing policy
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Policy configuration data.
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.import_policy = YLeafList()
                                self.import_policy.parent = self
                                self.import_policy.name = 'import_policy'
                                self.default_import_policy = None
                                self.export_policy = YLeafList()
                                self.export_policy.parent = self
                                self.export_policy.name = 'export_policy'
                                self.default_export_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.import_policy is not None:
                                    for child in self.import_policy:
                                        if child is not None:
                                            return True

                                if self.default_import_policy is not None:
                                    return True

                                if self.export_policy is not None:
                                    for child in self.export_policy:
                                        if child is not None:
                                            return True

                                if self.default_export_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info']


                        class State(object):
                            """
                            Operational state for routing policy
                            
                            .. attribute:: import_policy
                            
                            	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_import_policy
                            
                            	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            .. attribute:: export_policy
                            
                            	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                            	**type**\: list of str
                            
                            .. attribute:: default_export_policy
                            
                            	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                            	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.import_policy = YLeafList()
                                self.import_policy.parent = self
                                self.import_policy.name = 'import_policy'
                                self.default_import_policy = None
                                self.export_policy = YLeafList()
                                self.export_policy.parent = self
                                self.export_policy.name = 'export_policy'
                                self.default_export_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.import_policy is not None:
                                    for child in self.import_policy:
                                        if child is not None:
                                            return True

                                if self.default_import_policy is not None:
                                    return True

                                if self.export_policy is not None:
                                    for child in self.export_policy:
                                        if child is not None:
                                            return True

                                if self.default_export_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:apply-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']


                    class Ipv4Unicast(object):
                        """
                        IPv4 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State()
                            self.state.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info']


                        class State(object):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv4-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']


                    class Ipv6Unicast(object):
                        """
                        IPv6 unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters for common IPv4 and IPv6 unicast AFI\-SAFI options
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config>`
                        
                        .. attribute:: state
                        
                        	State information for common IPv4 and IPv6 unicast parameters
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State()
                            self.state.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']


                        class Config(object):
                            """
                            Configuration parameters for common IPv4 and IPv6 unicast
                            AFI\-SAFI options
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info']


                        class State(object):
                            """
                            State information for common IPv4 and IPv6 unicast
                            parameters
                            
                            .. attribute:: send_default_route
                            
                            	If set to true, send the default\-route to the neighbour(s)
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.send_default_route = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.send_default_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv6-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']


                    class Ipv4LabelledUnicast(object):
                        """
                        IPv4 Labelled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv4-labelled-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']


                    class Ipv6LabelledUnicast(object):
                        """
                        IPv6 Labelled Unicast configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:ipv6-labelled-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']


                    class L3VpnIpv4Unicast(object):
                        """
                        Unicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv4-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']


                    class L3VpnIpv6Unicast(object):
                        """
                        Unicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv6-unicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']


                    class L3VpnIpv4Multicast(object):
                        """
                        Multicast IPv4 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv4-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']


                    class L3VpnIpv6Multicast(object):
                        """
                        Multicast IPv6 L3VPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l3vpn-ipv6-multicast'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']


                    class L2VpnVpls(object):
                        """
                        BGP\-signalled VPLS configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l2vpn-vpls'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']


                    class L2VpnEvpn(object):
                        """
                        BGP EVPN configuration options
                        
                        .. attribute:: prefix_limit
                        
                        	Configure the maximum number of prefixes that will be accepted from a peer
                        	**type**\: :py:class:`PrefixLimit <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.prefix_limit = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit()
                            self.prefix_limit.parent = self


                        class PrefixLimit(object):
                            """
                            Configure the maximum number of prefixes that will be
                            accepted from a peer
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to the prefix limit for the AFI\-SAFI
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to the prefix\-limit for the AFI\-SAFI
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State()
                                self.state.parent = self


                            class Config(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info']


                            class State(object):
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
                                	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.max_prefixes = None
                                    self.shutdown_threshold_pct = None
                                    self.restart_timer = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.max_prefixes is not None:
                                        return True

                                    if self.shutdown_threshold_pct is not None:
                                        return True

                                    if self.restart_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:prefix-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:l2vpn-evpn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix_limit is not None and self.prefix_limit._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']


                    class UseMultiplePaths(object):
                        """
                        Parameters related to the use of multiple paths for the
                        same NLRI
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to multipath
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to multipath
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State>`
                        
                        .. attribute:: ebgp
                        
                        	Multipath parameters for eBGP
                        	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp>`
                        
                        .. attribute:: ibgp
                        
                        	Multipath parameters for iBGP
                        	**type**\: :py:class:`Ibgp <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State()
                            self.state.parent = self
                            self.ebgp = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp()
                            self.ebgp.parent = self
                            self.ibgp = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp()
                            self.ibgp.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info']


                        class State(object):
                            """
                            State parameters relating to multipath
                            
                            .. attribute:: enabled
                            
                            	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info']


                        class Ebgp(object):
                            """
                            Multipath parameters for eBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to eBGP multipath
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to eBGP multipath
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration parameters relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.allow_multiple_as = None
                                    self.maximum_paths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.allow_multiple_as is not None:
                                        return True

                                    if self.maximum_paths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info']


                            class State(object):
                                """
                                State information relating to eBGP multipath
                                
                                .. attribute:: allow_multiple_as
                                
                                	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                                	**type**\: bool
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.allow_multiple_as = None
                                    self.maximum_paths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.allow_multiple_as is not None:
                                        return True

                                    if self.maximum_paths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:ebgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']


                        class Ibgp(object):
                            """
                            Multipath parameters for iBGP
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to iBGP multipath
                            	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config>`
                            
                            .. attribute:: state
                            
                            	State information relating to iBGP multipath
                            	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State>`
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config()
                                self.config.parent = self
                                self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration parameters relating to iBGP multipath
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.maximum_paths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.maximum_paths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config']['meta_info']


                            class State(object):
                                """
                                State information relating to iBGP multipath
                                
                                .. attribute:: maximum_paths
                                
                                	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'bgp'
                                _revision = '2015-05-15'

                                def __init__(self):
                                    self.parent = None
                                    self.maximum_paths = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/bgp:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.maximum_paths is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.bgp._meta import _bgp as meta
                                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:ibgp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:use-multiple-paths'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.ebgp is not None and self.ebgp._has_data():
                                return True

                            if self.ibgp is not None and self.ibgp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']


                    class RouteSelectionOptions(object):
                        """
                        Parameters relating to options for route selection
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to route selection options
                        	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config>`
                        
                        .. attribute:: state
                        
                        	State information for the route selection options
                        	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State>`
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.config = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config()
                            self.config.parent = self
                            self.state = Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration parameters relating to route selection
                            options
                            
                            .. attribute:: always_compare_med
                            
                            	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                            	**type**\: bool
                            
                            .. attribute:: ignore_as_path_length
                            
                            	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                            	**type**\: bool
                            
                            .. attribute:: external_compare_router_id
                            
                            	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                            	**type**\: bool
                            
                            .. attribute:: advertise_inactive_routes
                            
                            	Advertise inactive routes to external peers.  The default is to only advertise active routes
                            	**type**\: bool
                            
                            .. attribute:: enable_aigp
                            
                            	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                            	**type**\: bool
                            
                            .. attribute:: ignore_next_hop_igp_metric
                            
                            	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.always_compare_med = None
                                self.ignore_as_path_length = None
                                self.external_compare_router_id = None
                                self.advertise_inactive_routes = None
                                self.enable_aigp = None
                                self.ignore_next_hop_igp_metric = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.always_compare_med is not None:
                                    return True

                                if self.ignore_as_path_length is not None:
                                    return True

                                if self.external_compare_router_id is not None:
                                    return True

                                if self.advertise_inactive_routes is not None:
                                    return True

                                if self.enable_aigp is not None:
                                    return True

                                if self.ignore_next_hop_igp_metric is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config']['meta_info']


                        class State(object):
                            """
                            State information for the route selection options
                            
                            .. attribute:: always_compare_med
                            
                            	Compare multi\-exit discriminator (MED) value from different ASes when selecting the best route.  The default behavior is to only compare MEDs for paths received from the same AS
                            	**type**\: bool
                            
                            .. attribute:: ignore_as_path_length
                            
                            	Ignore the AS path length when selecting the best path. The default is to use the AS path length and prefer paths with shorter length
                            	**type**\: bool
                            
                            .. attribute:: external_compare_router_id
                            
                            	When comparing similar routes received from external BGP peers, use the router\-id as a criterion to select the active path
                            	**type**\: bool
                            
                            .. attribute:: advertise_inactive_routes
                            
                            	Advertise inactive routes to external peers.  The default is to only advertise active routes
                            	**type**\: bool
                            
                            .. attribute:: enable_aigp
                            
                            	Flag to enable sending / receiving accumulated IGP attribute in routing updates
                            	**type**\: bool
                            
                            .. attribute:: ignore_next_hop_igp_metric
                            
                            	Ignore the IGP metric to the next\-hop when calculating BGP best\-path. The default is to select the route for which the metric to the next\-hop is lowest
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp'
                            _revision = '2015-05-15'

                            def __init__(self):
                                self.parent = None
                                self.always_compare_med = None
                                self.ignore_as_path_length = None
                                self.external_compare_router_id = None
                                self.advertise_inactive_routes = None
                                self.enable_aigp = None
                                self.ignore_next_hop_igp_metric = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/bgp:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.always_compare_med is not None:
                                    return True

                                if self.ignore_as_path_length is not None:
                                    return True

                                if self.external_compare_router_id is not None:
                                    return True

                                if self.advertise_inactive_routes is not None:
                                    return True

                                if self.enable_aigp is not None:
                                    return True

                                if self.ignore_next_hop_igp_metric is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.bgp._meta import _bgp as meta
                                return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:route-selection-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.afi_safi_name is None:
                            raise YPYDataValidationError('Key property afi_safi_name is None')

                        return self.parent._common_path +'/bgp:afi-safi[bgp:afi-safi-name = ' + str(self.afi_safi_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.afi_safi_name is not None:
                            return True

                        if self.graceful_restart is not None and self.graceful_restart._has_data():
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.apply_policy is not None and self.apply_policy._has_data():
                            return True

                        if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                            return True

                        if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                            return True

                        if self.ipv4_labelled_unicast is not None and self.ipv4_labelled_unicast._has_data():
                            return True

                        if self.ipv6_labelled_unicast is not None and self.ipv6_labelled_unicast._has_data():
                            return True

                        if self.l3vpn_ipv4_unicast is not None and self.l3vpn_ipv4_unicast._has_data():
                            return True

                        if self.l3vpn_ipv6_unicast is not None and self.l3vpn_ipv6_unicast._has_data():
                            return True

                        if self.l3vpn_ipv4_multicast is not None and self.l3vpn_ipv4_multicast._has_data():
                            return True

                        if self.l3vpn_ipv6_multicast is not None and self.l3vpn_ipv6_multicast._has_data():
                            return True

                        if self.l2vpn_vpls is not None and self.l2vpn_vpls._has_data():
                            return True

                        if self.l2vpn_evpn is not None and self.l2vpn_evpn._has_data():
                            return True

                        if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                            return True

                        if self.route_selection_options is not None and self.route_selection_options._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:afi-safis'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.afi_safi is not None:
                        for child_ref in self.afi_safi:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis']['meta_info']


            class GracefulRestart(object):
                """
                Parameters relating the graceful restart mechanism for BGP
                
                .. attribute:: config
                
                	Configuration parameters relating to graceful\-restart
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart.Config>`
                
                .. attribute:: state
                
                	State information associated with graceful\-restart
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.GracefulRestart.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.GracefulRestart.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.GracefulRestart.State()
                    self.state.parent = self


                class Config(object):
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
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.restart_time is not None:
                            return True

                        if self.stale_routes_time is not None:
                            return True

                        if self.helper_only is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart.Config']['meta_info']


                class State(object):
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
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: helper_only
                    
                    	Enable graceful\-restart in helper mode only. When this leaf is set, the local system does not retain forwarding its own state during a restart, but supports procedures for the receiving speaker, as defined in RFC4724
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.restart_time = None
                        self.stale_routes_time = None
                        self.helper_only = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        if self.restart_time is not None:
                            return True

                        if self.stale_routes_time is not None:
                            return True

                        if self.helper_only is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:graceful-restart'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart']['meta_info']


            class ApplyPolicy(object):
                """
                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                
                .. attribute:: config
                
                	Policy configuration data
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config>`
                
                .. attribute:: state
                
                	Operational state for routing policy
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.ApplyPolicy.State>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.ApplyPolicy.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Policy configuration data.
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.import_policy = YLeafList()
                        self.import_policy.parent = self
                        self.import_policy.name = 'import_policy'
                        self.default_import_policy = None
                        self.export_policy = YLeafList()
                        self.export_policy.parent = self
                        self.export_policy.name = 'export_policy'
                        self.default_export_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.import_policy is not None:
                            for child in self.import_policy:
                                if child is not None:
                                    return True

                        if self.default_import_policy is not None:
                            return True

                        if self.export_policy is not None:
                            for child in self.export_policy:
                                if child is not None:
                                    return True

                        if self.default_export_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config']['meta_info']


                class State(object):
                    """
                    Operational state for routing policy
                    
                    .. attribute:: import_policy
                    
                    	list of policy names in sequence to be applied on receiving a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_import_policy
                    
                    	explicitly set a default policy if no policy definition in the import policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    .. attribute:: export_policy
                    
                    	list of policy names in sequence to be applied on sending a routing update in the current context, e.g., for the current peer group, neighbor, address family, etc
                    	**type**\: list of str
                    
                    .. attribute:: default_export_policy
                    
                    	explicitly set a default policy if no policy definition in the export policy chain is satisfied
                    	**type**\: :py:class:`DefaultPolicyTypeEnum <ydk.models.routing.routing_policy.DefaultPolicyTypeEnum>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.import_policy = YLeafList()
                        self.import_policy.parent = self
                        self.import_policy.name = 'import_policy'
                        self.default_import_policy = None
                        self.export_policy = YLeafList()
                        self.export_policy.parent = self
                        self.export_policy.name = 'export_policy'
                        self.default_export_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.import_policy is not None:
                            for child in self.import_policy:
                                if child is not None:
                                    return True

                        if self.default_import_policy is not None:
                            return True

                        if self.export_policy is not None:
                            for child in self.export_policy:
                                if child is not None:
                                    return True

                        if self.default_export_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:apply-policy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy']['meta_info']


            class UseMultiplePaths(object):
                """
                Parameters related to the use of multiple paths for the
                same NLRI
                
                .. attribute:: config
                
                	Configuration parameters relating to multipath
                	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config>`
                
                .. attribute:: state
                
                	State parameters relating to multipath
                	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State>`
                
                .. attribute:: ebgp
                
                	Multipath parameters for eBGP
                	**type**\: :py:class:`Ebgp <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp>`
                
                .. attribute:: ibgp
                
                	Multipath parameters for iBGP
                	**type**\: :py:class:`Ibgp <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp>`
                
                

                """

                _prefix = 'bgp'
                _revision = '2015-05-15'

                def __init__(self):
                    self.parent = None
                    self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config()
                    self.config.parent = self
                    self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State()
                    self.state.parent = self
                    self.ebgp = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp()
                    self.ebgp.parent = self
                    self.ibgp = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp()
                    self.ibgp.parent = self


                class Config(object):
                    """
                    Configuration parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config']['meta_info']


                class State(object):
                    """
                    State parameters relating to multipath
                    
                    .. attribute:: enabled
                    
                    	Whether the use of multiple paths for the same NLRI is enabled for the neighbor. This value is overridden by any more specific configuration value
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.enabled is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State']['meta_info']


                class Ebgp(object):
                    """
                    Multipath parameters for eBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to eBGP multipath
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to eBGP multipath
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config()
                        self.config.parent = self
                        self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.allow_multiple_as = None
                            self.maximum_paths = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allow_multiple_as is not None:
                                return True

                            if self.maximum_paths is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config']['meta_info']


                    class State(object):
                        """
                        State information relating to eBGP multipath
                        
                        .. attribute:: allow_multiple_as
                        
                        	Allow multipath to use paths from different neighbouring ASes.  The default is to only consider multiple paths from the same neighbouring AS
                        	**type**\: bool
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using BGP multipath. The default is use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.allow_multiple_as = None
                            self.maximum_paths = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allow_multiple_as is not None:
                                return True

                            if self.maximum_paths is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ebgp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp']['meta_info']


                class Ibgp(object):
                    """
                    Multipath parameters for iBGP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to iBGP multipath
                    	**type**\: :py:class:`Config <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config>`
                    
                    .. attribute:: state
                    
                    	State information relating to iBGP multipath
                    	**type**\: :py:class:`State <ydk.models.bgp.bgp.Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State>`
                    
                    

                    """

                    _prefix = 'bgp'
                    _revision = '2015-05-15'

                    def __init__(self):
                        self.parent = None
                        self.config = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config()
                        self.config.parent = self
                        self.state = Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to iBGP multipath
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.maximum_paths = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.maximum_paths is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config']['meta_info']


                    class State(object):
                        """
                        State information relating to iBGP multipath
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of parallel paths to consider when using iBGP multipath. The default is to use a single path
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'bgp'
                        _revision = '2015-05-15'

                        def __init__(self):
                            self.parent = None
                            self.maximum_paths = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/bgp:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.maximum_paths is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.bgp._meta import _bgp as meta
                            return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/bgp:ibgp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.bgp._meta import _bgp as meta
                        return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/bgp:use-multiple-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.ebgp is not None and self.ebgp._has_data():
                        return True

                    if self.ibgp is not None and self.ibgp._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.bgp._meta import _bgp as meta
                    return meta._meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info']

            @property
            def _common_path(self):
                if self.peer_group_name is None:
                    raise YPYDataValidationError('Key property peer_group_name is None')

                return '/bgp:bgp/bgp:peer-groups/bgp:peer-group[bgp:peer-group-name = ' + str(self.peer_group_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.peer_group_name is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.timers is not None and self.timers._has_data():
                    return True

                if self.transport is not None and self.transport._has_data():
                    return True

                if self.error_handling is not None and self.error_handling._has_data():
                    return True

                if self.logging_options is not None and self.logging_options._has_data():
                    return True

                if self.ebgp_multihop is not None and self.ebgp_multihop._has_data():
                    return True

                if self.route_reflector is not None and self.route_reflector._has_data():
                    return True

                if self.as_path_options is not None and self.as_path_options._has_data():
                    return True

                if self.add_paths is not None and self.add_paths._has_data():
                    return True

                if self.afi_safis is not None and self.afi_safis._has_data():
                    return True

                if self.graceful_restart is not None and self.graceful_restart._has_data():
                    return True

                if self.apply_policy is not None and self.apply_policy._has_data():
                    return True

                if self.use_multiple_paths is not None and self.use_multiple_paths._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.bgp._meta import _bgp as meta
                return meta._meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']

        @property
        def _common_path(self):

            return '/bgp:bgp/bgp:peer-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.peer_group is not None:
                for child_ref in self.peer_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.bgp._meta import _bgp as meta
            return meta._meta_table['Bgp.PeerGroups']['meta_info']

    @property
    def _common_path(self):

        return '/bgp:bgp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.neighbors is not None and self.neighbors._has_data():
            return True

        if self.peer_groups is not None and self.peer_groups._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.bgp._meta import _bgp as meta
        return meta._meta_table['Bgp']['meta_info']


