""" openconfig_rib_bgp 

Defines a data model for representing BGP routing table (RIB)
contents.  The model supports 5 logical RIBs per address family\:

loc\-rib\: This is the main BGP routing table for the local routing
instance, containing best\-path selections for each prefix. The
loc\-rib table may contain multiple routes for a given prefix,
with an attribute to indicate which was selected as the best
path.

adj\-rib\-in\-pre\: This is a per\-neighbor table containing the NLRI
updates received from the neighbor before any local input policy
rules or filters have been applied.  This can be considered the
'raw' updates from a given neighbor.

adj\-rib\-in\-post\: This is a per\-neighbor table containing the
routes received from the neighbor that are eligible for
best\-path selection after local input policy rules have been
applied.

adj\-rib\-out\-pre\: This is a per\-neighbor table containing routes
eligible for sending (advertising) to the neighbor before output
policy rules have been applied.

adj\-rib\-out\-post\: This is a per\-neighbor table containing routes
eligible for sending (advertising) to the neighbor after output
policy rules have been applied.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class BgpRib(object):
    """
    Top level container for BGP RIBs
    
    .. attribute:: afi_safis
    
    	Enclosing container for address family list
    	**type**\:   :py:class:`AfiSafis <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis>`
    
    

    """

    _prefix = 'oc-bgprib'
    _revision = '2016-04-11'

    def __init__(self):
        self.afi_safis = BgpRib.AfiSafis()
        self.afi_safis.parent = self


    class AfiSafis(object):
        """
        Enclosing container for address family list
        
        .. attribute:: afi_safi
        
        	list of afi\-safi types
        	**type**\: list of    :py:class:`AfiSafi <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi>`
        
        

        """

        _prefix = 'oc-bgprib'
        _revision = '2016-04-11'

        def __init__(self):
            self.parent = None
            self.afi_safi = YList()
            self.afi_safi.parent = self
            self.afi_safi.name = 'afi_safi'


        class AfiSafi(object):
            """
            list of afi\-safi types
            
            .. attribute:: afi_safi_name  <key>
            
            	AFI,SAFI
            	**type**\:   :py:class:`Afi_Safi_TypeIdentity <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.Afi_Safi_TypeIdentity>`
            
            .. attribute:: ipv4_unicast
            
            	Routing tables for IPv4 unicast \-\- active when the afi\-safi name is ipv4\-unicast
            	**type**\:   :py:class:`Ipv4Unicast <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast>`
            
            .. attribute:: ipv6_unicast
            
            	Routing tables for IPv6 unicast \-\- active when the afi\-safi name is ipv6\-unicast
            	**type**\:   :py:class:`Ipv6Unicast <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast>`
            
            

            """

            _prefix = 'oc-bgprib'
            _revision = '2016-04-11'

            def __init__(self):
                self.parent = None
                self.afi_safi_name = None
                self.ipv4_unicast = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast()
                self.ipv4_unicast.parent = self
                self.ipv6_unicast = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast()
                self.ipv6_unicast.parent = self


            class Ipv4Unicast(object):
                """
                Routing tables for IPv4 unicast \-\- active when the
                afi\-safi name is ipv4\-unicast
                
                .. attribute:: loc_rib
                
                	Main routing table on the router, containing best\-path selections for each prefix.  The loc\-rib may contain multiple routes for the same prefix (it is a read\-only, unkeyed list).  The best\-path leaf should be set to true for the route selected by the best\-path selection process. Note that multiple paths may be used or advertised even if only one path is marked as best, e.g., when using BGP add\-paths.  An implementation may choose to mark multiple paths in the RIB as best path by setting the flag to true for multiple entries
                	**type**\:   :py:class:`LocRib <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib>`
                
                .. attribute:: neighbors
                
                	Enclosing container for neighbor list
                	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors>`
                
                

                """

                _prefix = 'oc-bgprib'
                _revision = '2016-04-11'

                def __init__(self):
                    self.parent = None
                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib()
                    self.loc_rib.parent = self
                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors()
                    self.neighbors.parent = self


                class LocRib(object):
                    """
                    Main routing table on the router, containing best\-path
                    selections for each prefix.  The loc\-rib may contain
                    multiple routes for the same prefix (it is a read\-only,
                    unkeyed list).  The best\-path leaf should be set to true
                    for the route selected by the best\-path selection process.
                    Note that multiple paths may be used or advertised even if
                    only one path is marked as best, e.g., when using BGP
                    add\-paths.  An implementation may choose to mark multiple
                    paths in the RIB as best path by setting the flag to true for
                    multiple entries.
                    
                    .. attribute:: num_routes
                    
                    	Number of route entries in the table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        self.parent = None
                        self.num_routes = None
                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes()
                        self.routes.parent = self


                    class Routes(object):
                        """
                        Enclosing container for list of routes in the routing
                        table.
                        
                        .. attribute:: route
                        
                        	List of routes in the table
                        	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
                            """
                            List of routes in the table
                            
                            .. attribute:: attributes
                            
                            	Base BGP route attributes associated with this route
                            	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes>`
                            
                            .. attribute:: best_path
                            
                            	Current path was selected as the best path
                            	**type**\:  bool
                            
                            .. attribute:: ext_attributes
                            
                            	Extended BGP route attributes associated with this route
                            	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes>`
                            
                            .. attribute:: invalid_reason
                            
                            	If the route is rejected as invalid, this indicates the reason
                            	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                            
                            .. attribute:: last_modified_date
                            
                            	Timestamp of when this path was last changed
                            	**type**\:  str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: last_update_received
                            
                            	Timestamp of when the last BGP update message was received for this path / prefix
                            	**type**\:  str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: prefix
                            
                            	Prefix for the route
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            .. attribute:: valid_route
                            
                            	Indicates that the route is considered valid by the local router
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self.best_path = None
                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self.invalid_reason = None
                                self.last_modified_date = None
                                self.last_update_received = None
                                self.prefix = None
                                self.valid_route = None


                            class Attributes(object):
                                """
                                Base BGP route attributes associated with this route
                                
                                .. attribute:: aggregator
                                
                                	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator>`
                                
                                .. attribute:: as4_path
                                
                                	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                	**type**\:  str
                                
                                .. attribute:: as_path
                                
                                	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                	**type**\:  str
                                
                                .. attribute:: atomic_aggr
                                
                                	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                	**type**\:  bool
                                
                                .. attribute:: community
                                
                                	List of standard BGP community attributes
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 65536..4294901759
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ([0\-9]+\:[0\-9]+)
                                
                                
                                ----
                                .. attribute:: local_pref
                                
                                	BGP local preference attribute sent to internal peers to indicate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med
                                
                                	BGP multi\-exit discriminator attribute used in BGP route selection process
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop
                                
                                	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: origin
                                
                                	BGP attribute defining the origin of the path information
                                	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self.as4_path = None
                                    self.as_path = None
                                    self.atomic_aggr = None
                                    self.community = YLeafList()
                                    self.community.parent = self
                                    self.community.name = 'community'
                                    self.local_pref = None
                                    self.med = None
                                    self.next_hop = None
                                    self.origin = None


                                class Aggregator(object):
                                    """
                                    BGP attribute indicating the prefix has been aggregated by
                                    the specified AS and router.
                                    
                                    .. attribute:: address
                                    
                                    	IP address of the router that performed the aggregation
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: as4
                                    
                                    	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_
                                    
                                    	AS number of the autnonomous system that performed the aggregation
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.as4 = None
                                        self.as_ = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.as4 is not None:
                                            return True

                                        if self.as_ is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregator is not None and self.aggregator._has_data():
                                        return True

                                    if self.as4_path is not None:
                                        return True

                                    if self.as_path is not None:
                                        return True

                                    if self.atomic_aggr is not None:
                                        return True

                                    if self.community is not None:
                                        for child in self.community:
                                            if child is not None:
                                                return True

                                    if self.local_pref is not None:
                                        return True

                                    if self.med is not None:
                                        return True

                                    if self.next_hop is not None:
                                        return True

                                    if self.origin is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes']['meta_info']


                            class ExtAttributes(object):
                                """
                                Extended BGP route attributes associated with this
                                route
                                
                                .. attribute:: aigp
                                
                                	BGP path attribute representing the accumulated IGP metric for the path
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: cluster_list
                                
                                	Represents the reflection path that the route has passed
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	List of BGP extended community attributes
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                .. attribute:: originator_id
                                
                                	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: path_id
                                
                                	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attribute
                                
                                	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.aigp = None
                                    self.cluster_list = YLeafList()
                                    self.cluster_list.parent = self
                                    self.cluster_list.name = 'cluster_list'
                                    self.ext_community = YLeafList()
                                    self.ext_community.parent = self
                                    self.ext_community.name = 'ext_community'
                                    self.originator_id = None
                                    self.path_id = None
                                    self.unknown_attribute = YList()
                                    self.unknown_attribute.parent = self
                                    self.unknown_attribute.name = 'unknown_attribute'


                                class UnknownAttribute(object):
                                    """
                                    This list contains received attributes that are unrecognized
                                    or unsupported by the local router.  The list may be empty.
                                    
                                    .. attribute:: attr_type  <key>
                                    
                                    	2\-octet value encoding the attribute flags and the attribute type code
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_len
                                    
                                    	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_value
                                    
                                    	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                    	**type**\:  str
                                    
                                    	**length:** 1..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attr_type = None
                                        self.attr_len = None
                                        self.attr_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.attr_type is None:
                                            raise YPYModelError('Key property attr_type is None')

                                        return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attr_type is not None:
                                            return True

                                        if self.attr_len is not None:
                                            return True

                                        if self.attr_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aigp is not None:
                                        return True

                                    if self.cluster_list is not None:
                                        for child in self.cluster_list:
                                            if child is not None:
                                                return True

                                    if self.ext_community is not None:
                                        for child in self.ext_community:
                                            if child is not None:
                                                return True

                                    if self.originator_id is not None:
                                        return True

                                    if self.path_id is not None:
                                        return True

                                    if self.unknown_attribute is not None:
                                        for child_ref in self.unknown_attribute:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:route'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.attributes is not None and self.attributes._has_data():
                                    return True

                                if self.best_path is not None:
                                    return True

                                if self.ext_attributes is not None and self.ext_attributes._has_data():
                                    return True

                                if self.invalid_reason is not None:
                                    return True

                                if self.last_modified_date is not None:
                                    return True

                                if self.last_update_received is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.valid_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-rib-bgp:routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.route is not None:
                                for child_ref in self.route:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-rib-bgp:loc-rib'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.num_routes is not None:
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib']['meta_info']


                class Neighbors(object):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        List of neighbors (peers) of the local BGP speaker
                        
                        .. attribute:: neighbor_address  <key>
                        
                        	IP address of the BGP neighbor or peer
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: adj_rib_in_post
                        
                        	Per\-neighbor table containing the paths received from the neighbor that are eligible for best\-path selection after local input policy rules have been applied
                        	**type**\:   :py:class:`AdjRibInPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Per\-neighbor table containing the NLRI updates received from the neighbor before any local input policy rules or filters have been applied.  This can be considered the 'raw' updates from the neighbor
                        	**type**\:   :py:class:`AdjRibInPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor after output policy rules have been applied
                        	**type**\:   :py:class:`AdjRibOutPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor before output policy rules have been applied
                        	**type**\:   :py:class:`AdjRibOutPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None
                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self


                        class AdjRibInPre(object):
                            """
                            Per\-neighbor table containing the NLRI updates
                            received from the neighbor before any local input
                            policy rules or filters have been applied.  This can
                            be considered the 'raw' updates from the neighbor.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-in-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info']


                        class AdjRibInPost(object):
                            """
                            Per\-neighbor table containing the paths received from
                            the neighbor that are eligible for best\-path selection
                            after local input policy rules have been applied.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-in-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPre(object):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor before output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-out-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info']


                        class AdjRibOutPost(object):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor after output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-out-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.neighbor_address is None:
                                raise YPYModelError('Key property neighbor_address is None')

                            return self.parent._common_path +'/openconfig-rib-bgp:neighbor[openconfig-rib-bgp:neighbor-address = ' + str(self.neighbor_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.neighbor_address is not None:
                                return True

                            if self.adj_rib_in_post is not None and self.adj_rib_in_post._has_data():
                                return True

                            if self.adj_rib_in_pre is not None and self.adj_rib_in_pre._has_data():
                                return True

                            if self.adj_rib_out_post is not None and self.adj_rib_out_post._has_data():
                                return True

                            if self.adj_rib_out_pre is not None and self.adj_rib_out_pre._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-rib-bgp:neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-rib-bgp:ipv4-unicast'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.loc_rib is not None and self.loc_rib._has_data():
                        return True

                    if self.neighbors is not None and self.neighbors._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']


            class Ipv6Unicast(object):
                """
                Routing tables for IPv6 unicast \-\- active when the
                afi\-safi name is ipv6\-unicast
                
                .. attribute:: loc_rib
                
                	Main routing table on the router, containing best\-path selections for each prefix.  The loc\-rib may contain multiple routes for the same prefix (it is a read\-only, unkeyed list).  The best\-path leaf should be set to true for the route selected by the best\-path selection process. Note that multiple paths may be used or advertised even if only one path is marked as best, e.g., when using BGP add\-paths.  An implementation may choose to mark multiple paths in the RIB as best path by setting the flag to true for multiple entries
                	**type**\:   :py:class:`LocRib <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib>`
                
                .. attribute:: neighbors
                
                	Enclosing container for neighbor list
                	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors>`
                
                

                """

                _prefix = 'oc-bgprib'
                _revision = '2016-04-11'

                def __init__(self):
                    self.parent = None
                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib()
                    self.loc_rib.parent = self
                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors()
                    self.neighbors.parent = self


                class LocRib(object):
                    """
                    Main routing table on the router, containing best\-path
                    selections for each prefix.  The loc\-rib may contain
                    multiple routes for the same prefix (it is a read\-only,
                    unkeyed list).  The best\-path leaf should be set to true
                    for the route selected by the best\-path selection process.
                    Note that multiple paths may be used or advertised even if
                    only one path is marked as best, e.g., when using BGP
                    add\-paths.  An implementation may choose to mark multiple
                    paths in the RIB as best path by setting the flag to true for
                    multiple entries.
                    
                    .. attribute:: num_routes
                    
                    	Number of route entries in the table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        self.parent = None
                        self.num_routes = None
                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes()
                        self.routes.parent = self


                    class Routes(object):
                        """
                        Enclosing container for list of routes in the routing
                        table.
                        
                        .. attribute:: route
                        
                        	List of routes in the table
                        	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
                            """
                            List of routes in the table
                            
                            .. attribute:: attributes
                            
                            	Base BGP route attributes associated with this route
                            	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes>`
                            
                            .. attribute:: best_path
                            
                            	Current path was selected as the best path
                            	**type**\:  bool
                            
                            .. attribute:: ext_attributes
                            
                            	Extended BGP route attributes associated with this route
                            	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes>`
                            
                            .. attribute:: invalid_reason
                            
                            	If the route is rejected as invalid, this indicates the reason
                            	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                            
                            .. attribute:: last_modified_date
                            
                            	Timestamp of when this path was last changed
                            	**type**\:  str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: last_update_received
                            
                            	Timestamp of when the last BGP update message was received for this path / prefix
                            	**type**\:  str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: prefix
                            
                            	Prefix for the route
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            .. attribute:: valid_route
                            
                            	Indicates that the route is considered valid by the local router
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self.best_path = None
                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self.invalid_reason = None
                                self.last_modified_date = None
                                self.last_update_received = None
                                self.prefix = None
                                self.valid_route = None


                            class Attributes(object):
                                """
                                Base BGP route attributes associated with this route
                                
                                .. attribute:: aggregator
                                
                                	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator>`
                                
                                .. attribute:: as4_path
                                
                                	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                	**type**\:  str
                                
                                .. attribute:: as_path
                                
                                	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                	**type**\:  str
                                
                                .. attribute:: atomic_aggr
                                
                                	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                	**type**\:  bool
                                
                                .. attribute:: community
                                
                                	List of standard BGP community attributes
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of int
                                
                                	**range:** 65536..4294901759
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ([0\-9]+\:[0\-9]+)
                                
                                
                                ----
                                .. attribute:: local_pref
                                
                                	BGP local preference attribute sent to internal peers to indicate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med
                                
                                	BGP multi\-exit discriminator attribute used in BGP route selection process
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop
                                
                                	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: origin
                                
                                	BGP attribute defining the origin of the path information
                                	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self.as4_path = None
                                    self.as_path = None
                                    self.atomic_aggr = None
                                    self.community = YLeafList()
                                    self.community.parent = self
                                    self.community.name = 'community'
                                    self.local_pref = None
                                    self.med = None
                                    self.next_hop = None
                                    self.origin = None


                                class Aggregator(object):
                                    """
                                    BGP attribute indicating the prefix has been aggregated by
                                    the specified AS and router.
                                    
                                    .. attribute:: address
                                    
                                    	IP address of the router that performed the aggregation
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: as4
                                    
                                    	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_
                                    
                                    	AS number of the autnonomous system that performed the aggregation
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.as4 = None
                                        self.as_ = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.as4 is not None:
                                            return True

                                        if self.as_ is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregator is not None and self.aggregator._has_data():
                                        return True

                                    if self.as4_path is not None:
                                        return True

                                    if self.as_path is not None:
                                        return True

                                    if self.atomic_aggr is not None:
                                        return True

                                    if self.community is not None:
                                        for child in self.community:
                                            if child is not None:
                                                return True

                                    if self.local_pref is not None:
                                        return True

                                    if self.med is not None:
                                        return True

                                    if self.next_hop is not None:
                                        return True

                                    if self.origin is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes']['meta_info']


                            class ExtAttributes(object):
                                """
                                Extended BGP route attributes associated with this
                                route
                                
                                .. attribute:: aigp
                                
                                	BGP path attribute representing the accumulated IGP metric for the path
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: cluster_list
                                
                                	Represents the reflection path that the route has passed
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	List of BGP extended community attributes
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                
                                ----
                                .. attribute:: originator_id
                                
                                	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: path_id
                                
                                	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attribute
                                
                                	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.aigp = None
                                    self.cluster_list = YLeafList()
                                    self.cluster_list.parent = self
                                    self.cluster_list.name = 'cluster_list'
                                    self.ext_community = YLeafList()
                                    self.ext_community.parent = self
                                    self.ext_community.name = 'ext_community'
                                    self.originator_id = None
                                    self.path_id = None
                                    self.unknown_attribute = YList()
                                    self.unknown_attribute.parent = self
                                    self.unknown_attribute.name = 'unknown_attribute'


                                class UnknownAttribute(object):
                                    """
                                    This list contains received attributes that are unrecognized
                                    or unsupported by the local router.  The list may be empty.
                                    
                                    .. attribute:: attr_type  <key>
                                    
                                    	2\-octet value encoding the attribute flags and the attribute type code
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_len
                                    
                                    	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_value
                                    
                                    	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                    	**type**\:  str
                                    
                                    	**length:** 1..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attr_type = None
                                        self.attr_len = None
                                        self.attr_value = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.attr_type is None:
                                            raise YPYModelError('Key property attr_type is None')

                                        return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attr_type is not None:
                                            return True

                                        if self.attr_len is not None:
                                            return True

                                        if self.attr_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aigp is not None:
                                        return True

                                    if self.cluster_list is not None:
                                        for child in self.cluster_list:
                                            if child is not None:
                                                return True

                                    if self.ext_community is not None:
                                        for child in self.ext_community:
                                            if child is not None:
                                                return True

                                    if self.originator_id is not None:
                                        return True

                                    if self.path_id is not None:
                                        return True

                                    if self.unknown_attribute is not None:
                                        for child_ref in self.unknown_attribute:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:route'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.attributes is not None and self.attributes._has_data():
                                    return True

                                if self.best_path is not None:
                                    return True

                                if self.ext_attributes is not None and self.ext_attributes._has_data():
                                    return True

                                if self.invalid_reason is not None:
                                    return True

                                if self.last_modified_date is not None:
                                    return True

                                if self.last_update_received is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.valid_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-rib-bgp:routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.route is not None:
                                for child_ref in self.route:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-rib-bgp:loc-rib'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.num_routes is not None:
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib']['meta_info']


                class Neighbors(object):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        List of neighbors (peers) of the local BGP speaker
                        
                        .. attribute:: neighbor_address  <key>
                        
                        	IP address of the BGP neighbor or peer
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: adj_rib_in_post
                        
                        	Per\-neighbor table containing the paths received from the neighbor that are eligible for best\-path selection after local input policy rules have been applied
                        	**type**\:   :py:class:`AdjRibInPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Per\-neighbor table containing the NLRI updates received from the neighbor before any local input policy rules or filters have been applied.  This can be considered the 'raw' updates from the neighbor
                        	**type**\:   :py:class:`AdjRibInPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor after output policy rules have been applied
                        	**type**\:   :py:class:`AdjRibOutPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor before output policy rules have been applied
                        	**type**\:   :py:class:`AdjRibOutPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None
                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self


                        class AdjRibInPre(object):
                            """
                            Per\-neighbor table containing the NLRI updates
                            received from the neighbor before any local input
                            policy rules or filters have been applied.  This can
                            be considered the 'raw' updates from the neighbor.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-in-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info']


                        class AdjRibInPost(object):
                            """
                            Per\-neighbor table containing the paths received from
                            the neighbor that are eligible for best\-path selection
                            after local input policy rules have been applied.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-in-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPre(object):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor before output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-out-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info']


                        class AdjRibOutPost(object):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor after output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = None
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of    :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:   :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:   :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:   :py:class:`Invalid_Route_ReasonIdentity <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_ReasonIdentity>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\:  str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        self.parent = None
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self.best_path = None
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.prefix = None
                                        self.valid_route = None


                                    class Attributes(object):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:   :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.cisco_xr_openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YLeafList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = None
                                            self.origin = None


                                        class Aggregator(object):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/openconfig-rib-bgp:aggregator'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.address is not None:
                                                    return True

                                                if self.as4 is not None:
                                                    return True

                                                if self.as_ is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregator is not None and self.aggregator._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child in self.community:
                                                    if child is not None:
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None:
                                                return True

                                            if self.origin is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info']


                                    class ExtAttributes(object):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        
                                        ----
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of    :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster_list = YLeafList()
                                            self.cluster_list.parent = self
                                            self.cluster_list.name = 'cluster_list'
                                            self.ext_community = YLeafList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attribute = YList()
                                            self.unknown_attribute.parent = self
                                            self.unknown_attribute.name = 'unknown_attribute'


                                        class UnknownAttribute(object):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  <key>
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\:  str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                self.parent = None
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.attr_type is None:
                                                    raise YPYModelError('Key property attr_type is None')

                                                return self.parent._common_path +'/openconfig-rib-bgp:unknown-attribute[openconfig-rib-bgp:attr-type = ' + str(self.attr_type) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attr_type is not None:
                                                    return True

                                                if self.attr_len is not None:
                                                    return True

                                                if self.attr_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-rib-bgp:ext-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster_list is not None:
                                                for child in self.cluster_list:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child in self.ext_community:
                                                    if child is not None:
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attribute is not None:
                                                for child_ref in self.unknown_attribute:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-rib-bgp:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attributes is not None and self.attributes._has_data():
                                            return True

                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes is not None and self.ext_attributes._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None:
                                            return True

                                        if self.last_update_received is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-rib-bgp:routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.route is not None:
                                        for child_ref in self.route:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-rib-bgp:adj-rib-out-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None:
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                                return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.neighbor_address is None:
                                raise YPYModelError('Key property neighbor_address is None')

                            return self.parent._common_path +'/openconfig-rib-bgp:neighbor[openconfig-rib-bgp:neighbor-address = ' + str(self.neighbor_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.neighbor_address is not None:
                                return True

                            if self.adj_rib_in_post is not None and self.adj_rib_in_post._has_data():
                                return True

                            if self.adj_rib_in_pre is not None and self.adj_rib_in_pre._has_data():
                                return True

                            if self.adj_rib_out_post is not None and self.adj_rib_out_post._has_data():
                                return True

                            if self.adj_rib_out_pre is not None and self.adj_rib_out_pre._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                            return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-rib-bgp:neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                        return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-rib-bgp:ipv6-unicast'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.loc_rib is not None and self.loc_rib._has_data():
                        return True

                    if self.neighbors is not None and self.neighbors._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                    return meta._meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']

            @property
            def _common_path(self):
                if self.afi_safi_name is None:
                    raise YPYModelError('Key property afi_safi_name is None')

                return '/openconfig-rib-bgp:bgp-rib/openconfig-rib-bgp:afi-safis/openconfig-rib-bgp:afi-safi[openconfig-rib-bgp:afi-safi-name = ' + str(self.afi_safi_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.afi_safi_name is not None:
                    return True

                if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                    return True

                if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
                return meta._meta_table['BgpRib.AfiSafis.AfiSafi']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-rib-bgp:bgp-rib/openconfig-rib-bgp:afi-safis'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.afi_safi is not None:
                for child_ref in self.afi_safi:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
            return meta._meta_table['BgpRib.AfiSafis']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-rib-bgp:bgp-rib'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.afi_safis is not None and self.afi_safis._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_rib_bgp as meta
        return meta._meta_table['BgpRib']['meta_info']


