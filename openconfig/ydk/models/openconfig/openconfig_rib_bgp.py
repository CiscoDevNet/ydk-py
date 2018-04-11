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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpRib(Entity):
    """
    Top level container for BGP RIBs
    
    .. attribute:: afi_safis
    
    	Enclosing container for address family list
    	**type**\:  :py:class:`AfiSafis <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis>`
    
    

    """

    _prefix = 'oc-bgprib'
    _revision = '2016-04-11'

    def __init__(self):
        super(BgpRib, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp-rib"
        self.yang_parent_name = "openconfig-rib-bgp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("afi-safis", ("afi_safis", BgpRib.AfiSafis))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.afi_safis = BgpRib.AfiSafis()
        self.afi_safis.parent = self
        self._children_name_map["afi_safis"] = "afi-safis"
        self._children_yang_names.add("afi-safis")
        self._segment_path = lambda: "openconfig-rib-bgp:bgp-rib"


    class AfiSafis(Entity):
        """
        Enclosing container for address family list
        
        .. attribute:: afi_safi
        
        	list of afi\-safi types
        	**type**\: list of  		 :py:class:`AfiSafi <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi>`
        
        

        """

        _prefix = 'oc-bgprib'
        _revision = '2016-04-11'

        def __init__(self):
            super(BgpRib.AfiSafis, self).__init__()

            self.yang_name = "afi-safis"
            self.yang_parent_name = "bgp-rib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("afi-safi", ("afi_safi", BgpRib.AfiSafis.AfiSafi))])
            self._leafs = OrderedDict()

            self.afi_safi = YList(self)
            self._segment_path = lambda: "afi-safis"
            self._absolute_path = lambda: "openconfig-rib-bgp:bgp-rib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpRib.AfiSafis, [], name, value)


        class AfiSafi(Entity):
            """
            list of afi\-safi types
            
            .. attribute:: afi_safi_name  (key)
            
            	AFI,SAFI
            	**type**\:  :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
            
            .. attribute:: ipv4_unicast
            
            	Routing tables for IPv4 unicast \-\- active when the afi\-safi name is ipv4\-unicast
            	**type**\:  :py:class:`Ipv4Unicast <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast>`
            
            .. attribute:: ipv6_unicast
            
            	Routing tables for IPv6 unicast \-\- active when the afi\-safi name is ipv6\-unicast
            	**type**\:  :py:class:`Ipv6Unicast <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast>`
            
            

            """

            _prefix = 'oc-bgprib'
            _revision = '2016-04-11'

            def __init__(self):
                super(BgpRib.AfiSafis.AfiSafi, self).__init__()

                self.yang_name = "afi-safi"
                self.yang_parent_name = "afi-safis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['afi_safi_name']
                self._child_container_classes = OrderedDict([("ipv4-unicast", ("ipv4_unicast", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast)), ("ipv6-unicast", ("ipv6_unicast", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('afi_safi_name', YLeaf(YType.identityref, 'afi-safi-name')),
                ])
                self.afi_safi_name = None

                self.ipv4_unicast = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast()
                self.ipv4_unicast.parent = self
                self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                self._children_yang_names.add("ipv4-unicast")

                self.ipv6_unicast = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast()
                self.ipv6_unicast.parent = self
                self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                self._children_yang_names.add("ipv6-unicast")
                self._segment_path = lambda: "afi-safi" + "[afi-safi-name='" + str(self.afi_safi_name) + "']"
                self._absolute_path = lambda: "openconfig-rib-bgp:bgp-rib/afi-safis/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpRib.AfiSafis.AfiSafi, ['afi_safi_name'], name, value)


            class Ipv4Unicast(Entity):
                """
                Routing tables for IPv4 unicast \-\- active when the
                afi\-safi name is ipv4\-unicast
                
                .. attribute:: loc_rib
                
                	Main routing table on the router, containing best\-path selections for each prefix.  The loc\-rib may contain multiple routes for the same prefix (it is a read\-only, unkeyed list).  The best\-path leaf should be set to true for the route selected by the best\-path selection process. Note that multiple paths may be used or advertised even if only one path is marked as best, e.g., when using BGP add\-paths.  An implementation may choose to mark multiple paths in the RIB as best path by setting the flag to true for multiple entries
                	**type**\:  :py:class:`LocRib <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib>`
                
                .. attribute:: neighbors
                
                	Enclosing container for neighbor list
                	**type**\:  :py:class:`Neighbors <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors>`
                
                

                """

                _prefix = 'oc-bgprib'
                _revision = '2016-04-11'

                def __init__(self):
                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast, self).__init__()

                    self.yang_name = "ipv4-unicast"
                    self.yang_parent_name = "afi-safi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("loc-rib", ("loc_rib", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib)), ("neighbors", ("neighbors", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"
                    self._children_yang_names.add("loc-rib")

                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")
                    self._segment_path = lambda: "ipv4-unicast"


                class LocRib(Entity):
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
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv4-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                        ])
                        self.num_routes = None

                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                        self._children_yang_names.add("routes")
                        self._segment_path = lambda: "loc-rib"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib, ['num_routes'], name, value)


                    class Routes(Entity):
                        """
                        Enclosing container for list of routes in the routing
                        table.
                        
                        .. attribute:: route
                        
                        	List of routes in the table
                        	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "routes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes, [], name, value)


                        class Route(Entity):
                            """
                            List of routes in the table
                            
                            .. attribute:: prefix
                            
                            	Prefix for the route
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            .. attribute:: attributes
                            
                            	Base BGP route attributes associated with this route
                            	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes>`
                            
                            .. attribute:: ext_attributes
                            
                            	Extended BGP route attributes associated with this route
                            	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes>`
                            
                            .. attribute:: last_modified_date
                            
                            	Timestamp of when this path was last changed
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: last_update_received
                            
                            	Timestamp of when the last BGP update message was received for this path / prefix
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: valid_route
                            
                            	Indicates that the route is considered valid by the local router
                            	**type**\: bool
                            
                            .. attribute:: invalid_reason
                            
                            	If the route is rejected as invalid, this indicates the reason
                            	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                            
                            .. attribute:: best_path
                            
                            	Current path was selected as the best path
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                    ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                    ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                    ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                    ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                    ('best_path', YLeaf(YType.boolean, 'best-path')),
                                ])
                                self.prefix = None
                                self.last_modified_date = None
                                self.last_update_received = None
                                self.valid_route = None
                                self.invalid_reason = None
                                self.best_path = None

                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                                self._children_yang_names.add("attributes")

                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                self._children_yang_names.add("ext-attributes")
                                self._segment_path = lambda: "route"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                            class Attributes(Entity):
                                """
                                Base BGP route attributes associated with this route
                                
                                .. attribute:: origin
                                
                                	BGP attribute defining the origin of the path information
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: as_path
                                
                                	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                	**type**\: str
                                
                                .. attribute:: as4_path
                                
                                	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                	**type**\: str
                                
                                .. attribute:: next_hop
                                
                                	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: med
                                
                                	BGP multi\-exit discriminator attribute used in BGP route selection process
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_pref
                                
                                	BGP local preference attribute sent to internal peers to indicate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: atomic_aggr
                                
                                	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                	**type**\: bool
                                
                                .. attribute:: aggregator
                                
                                	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator>`
                                
                                .. attribute:: community
                                
                                	List of standard BGP community attributes
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 65536..4294901759
                                
                                		**type**\: list of str
                                
                                			**pattern:** ([0\-9]+\:[0\-9]+)
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes, self).__init__()

                                    self.yang_name = "attributes"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('origin', YLeaf(YType.enumeration, 'origin')),
                                        ('as_path', YLeaf(YType.str, 'as-path')),
                                        ('as4_path', YLeaf(YType.str, 'as4-path')),
                                        ('next_hop', YLeaf(YType.str, 'next-hop')),
                                        ('med', YLeaf(YType.uint32, 'med')),
                                        ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                        ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                        ('community', YLeafList(YType.str, 'community')),
                                    ])
                                    self.origin = None
                                    self.as_path = None
                                    self.as4_path = None
                                    self.next_hop = None
                                    self.med = None
                                    self.local_pref = None
                                    self.atomic_aggr = None
                                    self.community = []

                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self._children_name_map["aggregator"] = "aggregator"
                                    self._children_yang_names.add("aggregator")
                                    self._segment_path = lambda: "attributes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                class Aggregator(Entity):
                                    """
                                    BGP attribute indicating the prefix has been aggregated by
                                    the specified AS and router.
                                    
                                    .. attribute:: as_
                                    
                                    	AS number of the autnonomous system that performed the aggregation
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as4
                                    
                                    	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address
                                    
                                    	IP address of the router that performed the aggregation
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__init__()

                                        self.yang_name = "aggregator"
                                        self.yang_parent_name = "attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_', YLeaf(YType.uint32, 'as')),
                                            ('as4', YLeaf(YType.uint32, 'as4')),
                                            ('address', YLeaf(YType.str, 'address')),
                                        ])
                                        self.as_ = None
                                        self.as4 = None
                                        self.address = None
                                        self._segment_path = lambda: "aggregator"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                            class ExtAttributes(Entity):
                                """
                                Extended BGP route attributes associated with this
                                route
                                
                                .. attribute:: originator_id
                                
                                	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: cluster_list
                                
                                	Represents the reflection path that the route has passed
                                	**type**\: list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	List of BGP extended community attributes
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                .. attribute:: aigp
                                
                                	BGP path attribute representing the accumulated IGP metric for the path
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: path_id
                                
                                	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attribute
                                
                                	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes, self).__init__()

                                    self.yang_name = "ext-attributes"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute))])
                                    self._leafs = OrderedDict([
                                        ('originator_id', YLeaf(YType.str, 'originator-id')),
                                        ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                        ('ext_community', YLeafList(YType.str, 'ext-community')),
                                        ('aigp', YLeaf(YType.uint64, 'aigp')),
                                        ('path_id', YLeaf(YType.uint32, 'path-id')),
                                    ])
                                    self.originator_id = None
                                    self.cluster_list = []
                                    self.ext_community = []
                                    self.aigp = None
                                    self.path_id = None

                                    self.unknown_attribute = YList(self)
                                    self._segment_path = lambda: "ext-attributes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                class UnknownAttribute(Entity):
                                    """
                                    This list contains received attributes that are unrecognized
                                    or unsupported by the local router.  The list may be empty.
                                    
                                    .. attribute:: attr_type  (key)
                                    
                                    	2\-octet value encoding the attribute flags and the attribute type code
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_len
                                    
                                    	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_value
                                    
                                    	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                    	**type**\: str
                                    
                                    	**length:** 1..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                        self.yang_name = "unknown-attribute"
                                        self.yang_parent_name = "ext-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['attr_type']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                            ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                            ('attr_value', YLeaf(YType.str, 'attr-value')),
                                        ])
                                        self.attr_type = None
                                        self.attr_len = None
                                        self.attr_value = None
                                        self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                class Neighbors(Entity):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv4-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("neighbor", ("neighbor", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor))])
                        self._leafs = OrderedDict()

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        List of neighbors (peers) of the local BGP speaker
                        
                        .. attribute:: neighbor_address  (key)
                        
                        	IP address of the BGP neighbor or peer
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Per\-neighbor table containing the NLRI updates received from the neighbor before any local input policy rules or filters have been applied.  This can be considered the 'raw' updates from the neighbor
                        	**type**\:  :py:class:`AdjRibInPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_in_post
                        
                        	Per\-neighbor table containing the paths received from the neighbor that are eligible for best\-path selection after local input policy rules have been applied
                        	**type**\:  :py:class:`AdjRibInPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor before output policy rules have been applied
                        	**type**\:  :py:class:`AdjRibOutPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor after output policy rules have been applied
                        	**type**\:  :py:class:`AdjRibOutPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_address']
                            self._child_container_classes = OrderedDict([("adj-rib-in-pre", ("adj_rib_in_pre", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre)), ("adj-rib-in-post", ("adj_rib_in_post", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost)), ("adj-rib-out-pre", ("adj_rib_out_pre", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre)), ("adj-rib-out-post", ("adj_rib_out_post", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                            ])
                            self.neighbor_address = None

                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._children_yang_names.add("adj-rib-in-pre")

                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                            self._children_yang_names.add("adj-rib-in-post")

                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                            self._children_yang_names.add("adj-rib-out-pre")

                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                            self._children_yang_names.add("adj-rib-out-post")
                            self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor, ['neighbor_address'], name, value)


                        class AdjRibInPre(Entity):
                            """
                            Per\-neighbor table containing the NLRI updates
                            received from the neighbor before any local input
                            policy rules or filters have been applied.  This can
                            be considered the 'raw' updates from the neighbor.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-in-pre"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibInPost(Entity):
                            """
                            Per\-neighbor table containing the paths received from
                            the neighbor that are eligible for best\-path selection
                            after local input policy rules have been applied.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-in-post"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibOutPre(Entity):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor before output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-out-pre"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibOutPost(Entity):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor after output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-out-post"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


            class Ipv6Unicast(Entity):
                """
                Routing tables for IPv6 unicast \-\- active when the
                afi\-safi name is ipv6\-unicast
                
                .. attribute:: loc_rib
                
                	Main routing table on the router, containing best\-path selections for each prefix.  The loc\-rib may contain multiple routes for the same prefix (it is a read\-only, unkeyed list).  The best\-path leaf should be set to true for the route selected by the best\-path selection process. Note that multiple paths may be used or advertised even if only one path is marked as best, e.g., when using BGP add\-paths.  An implementation may choose to mark multiple paths in the RIB as best path by setting the flag to true for multiple entries
                	**type**\:  :py:class:`LocRib <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib>`
                
                .. attribute:: neighbors
                
                	Enclosing container for neighbor list
                	**type**\:  :py:class:`Neighbors <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors>`
                
                

                """

                _prefix = 'oc-bgprib'
                _revision = '2016-04-11'

                def __init__(self):
                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast, self).__init__()

                    self.yang_name = "ipv6-unicast"
                    self.yang_parent_name = "afi-safi"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("loc-rib", ("loc_rib", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib)), ("neighbors", ("neighbors", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"
                    self._children_yang_names.add("loc-rib")

                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")
                    self._segment_path = lambda: "ipv6-unicast"


                class LocRib(Entity):
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
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv6-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                        ])
                        self.num_routes = None

                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                        self._children_yang_names.add("routes")
                        self._segment_path = lambda: "loc-rib"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib, ['num_routes'], name, value)


                    class Routes(Entity):
                        """
                        Enclosing container for list of routes in the routing
                        table.
                        
                        .. attribute:: route
                        
                        	List of routes in the table
                        	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "routes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes, [], name, value)


                        class Route(Entity):
                            """
                            List of routes in the table
                            
                            .. attribute:: prefix
                            
                            	Prefix for the route
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            .. attribute:: attributes
                            
                            	Base BGP route attributes associated with this route
                            	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes>`
                            
                            .. attribute:: ext_attributes
                            
                            	Extended BGP route attributes associated with this route
                            	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes>`
                            
                            .. attribute:: last_modified_date
                            
                            	Timestamp of when this path was last changed
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: last_update_received
                            
                            	Timestamp of when the last BGP update message was received for this path / prefix
                            	**type**\: str
                            
                            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                            
                            .. attribute:: valid_route
                            
                            	Indicates that the route is considered valid by the local router
                            	**type**\: bool
                            
                            .. attribute:: invalid_reason
                            
                            	If the route is rejected as invalid, this indicates the reason
                            	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                            
                            .. attribute:: best_path
                            
                            	Current path was selected as the best path
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                    ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                    ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                    ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                    ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                    ('best_path', YLeaf(YType.boolean, 'best-path')),
                                ])
                                self.prefix = None
                                self.last_modified_date = None
                                self.last_update_received = None
                                self.valid_route = None
                                self.invalid_reason = None
                                self.best_path = None

                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                                self._children_yang_names.add("attributes")

                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                self._children_yang_names.add("ext-attributes")
                                self._segment_path = lambda: "route"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                            class Attributes(Entity):
                                """
                                Base BGP route attributes associated with this route
                                
                                .. attribute:: origin
                                
                                	BGP attribute defining the origin of the path information
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: as_path
                                
                                	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                	**type**\: str
                                
                                .. attribute:: as4_path
                                
                                	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                	**type**\: str
                                
                                .. attribute:: next_hop
                                
                                	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: med
                                
                                	BGP multi\-exit discriminator attribute used in BGP route selection process
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_pref
                                
                                	BGP local preference attribute sent to internal peers to indicate
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: atomic_aggr
                                
                                	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                	**type**\: bool
                                
                                .. attribute:: aggregator
                                
                                	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator>`
                                
                                .. attribute:: community
                                
                                	List of standard BGP community attributes
                                	**type**\: union of the below types:
                                
                                		**type**\: list of int
                                
                                			**range:** 65536..4294901759
                                
                                		**type**\: list of str
                                
                                			**pattern:** ([0\-9]+\:[0\-9]+)
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes, self).__init__()

                                    self.yang_name = "attributes"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('origin', YLeaf(YType.enumeration, 'origin')),
                                        ('as_path', YLeaf(YType.str, 'as-path')),
                                        ('as4_path', YLeaf(YType.str, 'as4-path')),
                                        ('next_hop', YLeaf(YType.str, 'next-hop')),
                                        ('med', YLeaf(YType.uint32, 'med')),
                                        ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                        ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                        ('community', YLeafList(YType.str, 'community')),
                                    ])
                                    self.origin = None
                                    self.as_path = None
                                    self.as4_path = None
                                    self.next_hop = None
                                    self.med = None
                                    self.local_pref = None
                                    self.atomic_aggr = None
                                    self.community = []

                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self._children_name_map["aggregator"] = "aggregator"
                                    self._children_yang_names.add("aggregator")
                                    self._segment_path = lambda: "attributes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                class Aggregator(Entity):
                                    """
                                    BGP attribute indicating the prefix has been aggregated by
                                    the specified AS and router.
                                    
                                    .. attribute:: as_
                                    
                                    	AS number of the autnonomous system that performed the aggregation
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as4
                                    
                                    	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address
                                    
                                    	IP address of the router that performed the aggregation
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__init__()

                                        self.yang_name = "aggregator"
                                        self.yang_parent_name = "attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_', YLeaf(YType.uint32, 'as')),
                                            ('as4', YLeaf(YType.uint32, 'as4')),
                                            ('address', YLeaf(YType.str, 'address')),
                                        ])
                                        self.as_ = None
                                        self.as4 = None
                                        self.address = None
                                        self._segment_path = lambda: "aggregator"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                            class ExtAttributes(Entity):
                                """
                                Extended BGP route attributes associated with this
                                route
                                
                                .. attribute:: originator_id
                                
                                	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: cluster_list
                                
                                	Represents the reflection path that the route has passed
                                	**type**\: list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	List of BGP extended community attributes
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                
                                		**type**\: list of str
                                
                                			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                
                                .. attribute:: aigp
                                
                                	BGP path attribute representing the accumulated IGP metric for the path
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: path_id
                                
                                	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attribute
                                
                                	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes, self).__init__()

                                    self.yang_name = "ext-attributes"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute))])
                                    self._leafs = OrderedDict([
                                        ('originator_id', YLeaf(YType.str, 'originator-id')),
                                        ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                        ('ext_community', YLeafList(YType.str, 'ext-community')),
                                        ('aigp', YLeaf(YType.uint64, 'aigp')),
                                        ('path_id', YLeaf(YType.uint32, 'path-id')),
                                    ])
                                    self.originator_id = None
                                    self.cluster_list = []
                                    self.ext_community = []
                                    self.aigp = None
                                    self.path_id = None

                                    self.unknown_attribute = YList(self)
                                    self._segment_path = lambda: "ext-attributes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                class UnknownAttribute(Entity):
                                    """
                                    This list contains received attributes that are unrecognized
                                    or unsupported by the local router.  The list may be empty.
                                    
                                    .. attribute:: attr_type  (key)
                                    
                                    	2\-octet value encoding the attribute flags and the attribute type code
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_len
                                    
                                    	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attr_value
                                    
                                    	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                    	**type**\: str
                                    
                                    	**length:** 1..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                        self.yang_name = "unknown-attribute"
                                        self.yang_parent_name = "ext-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['attr_type']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                            ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                            ('attr_value', YLeaf(YType.str, 'attr-value')),
                                        ])
                                        self.attr_type = None
                                        self.attr_len = None
                                        self.attr_value = None
                                        self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                class Neighbors(Entity):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv6-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("neighbor", ("neighbor", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor))])
                        self._leafs = OrderedDict()

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        List of neighbors (peers) of the local BGP speaker
                        
                        .. attribute:: neighbor_address  (key)
                        
                        	IP address of the BGP neighbor or peer
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Per\-neighbor table containing the NLRI updates received from the neighbor before any local input policy rules or filters have been applied.  This can be considered the 'raw' updates from the neighbor
                        	**type**\:  :py:class:`AdjRibInPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_in_post
                        
                        	Per\-neighbor table containing the paths received from the neighbor that are eligible for best\-path selection after local input policy rules have been applied
                        	**type**\:  :py:class:`AdjRibInPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor before output policy rules have been applied
                        	**type**\:  :py:class:`AdjRibOutPre <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Per\-neighbor table containing paths eligble for sending (advertising) to the neighbor after output policy rules have been applied
                        	**type**\:  :py:class:`AdjRibOutPost <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost>`
                        
                        

                        """

                        _prefix = 'oc-bgprib'
                        _revision = '2016-04-11'

                        def __init__(self):
                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_address']
                            self._child_container_classes = OrderedDict([("adj-rib-in-pre", ("adj_rib_in_pre", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre)), ("adj-rib-in-post", ("adj_rib_in_post", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost)), ("adj-rib-out-pre", ("adj_rib_out_pre", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre)), ("adj-rib-out-post", ("adj_rib_out_post", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('neighbor_address', YLeaf(YType.str, 'neighbor-address')),
                            ])
                            self.neighbor_address = None

                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._children_yang_names.add("adj-rib-in-pre")

                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                            self._children_yang_names.add("adj-rib-in-post")

                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                            self._children_yang_names.add("adj-rib-out-pre")

                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                            self._children_yang_names.add("adj-rib-out-post")
                            self._segment_path = lambda: "neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor, ['neighbor_address'], name, value)


                        class AdjRibInPre(Entity):
                            """
                            Per\-neighbor table containing the NLRI updates
                            received from the neighbor before any local input
                            policy rules or filters have been applied.  This can
                            be considered the 'raw' updates from the neighbor.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-in-pre"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibInPost(Entity):
                            """
                            Per\-neighbor table containing the paths received from
                            the neighbor that are eligible for best\-path selection
                            after local input policy rules have been applied.
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-in-post"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibOutPre(Entity):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor before output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-out-pre"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)


                        class AdjRibOutPost(Entity):
                            """
                            Per\-neighbor table containing paths eligble for
                            sending (advertising) to the neighbor after output
                            policy rules have been applied
                            
                            .. attribute:: num_routes
                            
                            	Number of route entries in the table
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: routes
                            
                            	Enclosing container for list of routes in the routing table
                            	**type**\:  :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'oc-bgprib'
                            _revision = '2016-04-11'

                            def __init__(self):
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("routes", ("routes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_routes', YLeaf(YType.uint64, 'num-routes')),
                                ])
                                self.num_routes = None

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")
                                self._segment_path = lambda: "adj-rib-out-post"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost, ['num_routes'], name, value)


                            class Routes(Entity):
                                """
                                Enclosing container for list of routes in the routing
                                table.
                                
                                .. attribute:: route
                                
                                	List of routes in the table
                                	**type**\: list of  		 :py:class:`Route <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("route", ("route", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, [], name, value)


                                class Route(Entity):
                                    """
                                    List of routes in the table
                                    
                                    .. attribute:: prefix
                                    
                                    	Prefix for the route
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    .. attribute:: attributes
                                    
                                    	Base BGP route attributes associated with this route
                                    	**type**\:  :py:class:`Attributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes>`
                                    
                                    .. attribute:: ext_attributes
                                    
                                    	Extended BGP route attributes associated with this route
                                    	**type**\:  :py:class:`ExtAttributes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	Timestamp of when this path was last changed
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: last_update_received
                                    
                                    	Timestamp of when the last BGP update message was received for this path / prefix
                                    	**type**\: str
                                    
                                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                                    
                                    .. attribute:: valid_route
                                    
                                    	Indicates that the route is considered valid by the local router
                                    	**type**\: bool
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	If the route is rejected as invalid, this indicates the reason
                                    	**type**\:  :py:class:`INVALIDROUTEREASON <ydk.models.openconfig.openconfig_rib_bgp_types.INVALIDROUTEREASON>`
                                    
                                    .. attribute:: best_path
                                    
                                    	Current path was selected as the best path
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'oc-bgprib'
                                    _revision = '2016-04-11'

                                    def __init__(self):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("attributes", ("attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes)), ("ext-attributes", ("ext_attributes", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('last_modified_date', YLeaf(YType.str, 'last-modified-date')),
                                            ('last_update_received', YLeaf(YType.str, 'last-update-received')),
                                            ('valid_route', YLeaf(YType.boolean, 'valid-route')),
                                            ('invalid_reason', YLeaf(YType.identityref, 'invalid-reason')),
                                            ('best_path', YLeaf(YType.boolean, 'best-path')),
                                        ])
                                        self.prefix = None
                                        self.last_modified_date = None
                                        self.last_update_received = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")
                                        self._segment_path = lambda: "route"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, ['prefix', 'last_modified_date', 'last_update_received', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class Attributes(Entity):
                                        """
                                        Base BGP route attributes associated with this route
                                        
                                        .. attribute:: origin
                                        
                                        	BGP attribute defining the origin of the path information
                                        	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        .. attribute:: as_path
                                        
                                        	String representation of the BGP AS path attribute as concatenated AS path segments.  Each segment of the AS\_PATH should be formatted as follows based on the segment type (#### denotes a single AS number)\:   AS\_SEQ\: #### #### #####  AS\_SET\: { #### #### }  AS\_CONFED\_SEQUENCE\: ( #### #### )  AS\_CONFED\_SET\: [ #### #### ]  AS\_PATH segment types are described in RFC 5065.  In the Adj\-RIB\-In or Adj\-RIB\-Out, this leaf should show the received or sent AS\_PATH value, respectively.  For example, if the local router is not 4\-byte capable, this value should consist of 2\-octet ASNs or the AS\_TRANS (AS 23456) values received or sent in route updates.  In the Loc\-RIB, this leaf should reflect the effective AS path for the route, e.g., a 4\-octet value if the local router is 4\-octet capable
                                        	**type**\: str
                                        
                                        .. attribute:: as4_path
                                        
                                        	This string represents the AS path encoded with 4\-octet AS numbers in the optional transitive AS4\_PATH attribute. This value is populated with the received or sent attribute in Adj\-RIB\-In or Adj\-RIB\-Out, respectively.  It should not be populated in Loc\-RIB since the Loc\-RIB is expected to store the effective AS\-Path in the as\-path leaf regardless of being 4\-octet or 2\-octet
                                        	**type**\: str
                                        
                                        .. attribute:: next_hop
                                        
                                        	BGP next hop attribute defining the IP address of the router that should be used as the next hop to the destination
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: med
                                        
                                        	BGP multi\-exit discriminator attribute used in BGP route selection process
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: local_pref
                                        
                                        	BGP local preference attribute sent to internal peers to indicate
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	BGP attribute indicating that the prefix is an atomic aggregate, i.e., the peer selected a less specific route without selecting a more specific route that is included in it
                                        	**type**\: bool
                                        
                                        .. attribute:: aggregator
                                        
                                        	BGP attribute indicating the prefix has been aggregated by the specified AS and router
                                        	**type**\:  :py:class:`Aggregator <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator>`
                                        
                                        .. attribute:: community
                                        
                                        	List of standard BGP community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("aggregator", ("aggregator", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('origin', YLeaf(YType.enumeration, 'origin')),
                                                ('as_path', YLeaf(YType.str, 'as-path')),
                                                ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                                ('med', YLeaf(YType.uint32, 'med')),
                                                ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                ('atomic_aggr', YLeaf(YType.boolean, 'atomic-aggr')),
                                                ('community', YLeafList(YType.str, 'community')),
                                            ])
                                            self.origin = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.next_hop = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None
                                            self.community = []

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")
                                            self._segment_path = lambda: "attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, ['origin', 'as_path', 'as4_path', 'next_hop', 'med', 'local_pref', 'atomic_aggr', 'community'], name, value)


                                        class Aggregator(Entity):
                                            """
                                            BGP attribute indicating the prefix has been aggregated by
                                            the specified AS and router.
                                            
                                            .. attribute:: as_
                                            
                                            	AS number of the autnonomous system that performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4
                                            
                                            	AS number of the autnonomous system that performed the aggregation (4\-octet representation).  This value is populated if an upstream router is not 4\-octet capable. Its semantics are similar to the AS4\_PATH optional transitive attribute
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', YLeaf(YType.uint32, 'as')),
                                                    ('as4', YLeaf(YType.uint32, 'as4')),
                                                    ('address', YLeaf(YType.str, 'address')),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregator"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, ['as_', 'as4', 'address'], name, value)


                                    class ExtAttributes(Entity):
                                        """
                                        Extended BGP route attributes associated with this
                                        route
                                        
                                        .. attribute:: originator_id
                                        
                                        	BGP attribute that provides the id as an IPv4 address of the route reflector that created the announcement
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cluster_list
                                        
                                        	Represents the reflection path that the route has passed
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	List of BGP extended community attributes
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-target\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])\:(4[0\-2][0\-9][0\-4][0\-9][0\-6][0\-7][0\-2][0\-9][0\-6]\|[1\-3][0\-9]{9}\|[1\-9]([0\-9]{1,7})?[0\-9]\|[1\-9])
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** route\\\-origin\:(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\:(6[0\-5][0\-5][0\-3][0\-5]\|[1\-5][0\-9]{4}\|[1\-9][0\-9]{1,4}\|[0\-9])
                                        
                                        .. attribute:: aigp
                                        
                                        	BGP path attribute representing the accumulated IGP metric for the path
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: path_id
                                        
                                        	When the BGP speaker supports advertisement of multiple paths for a prefix, the path identifier is used to uniquely identify a route based on the combination of the prefix and path id.  In the Adj\-RIB\-In, the path\-id value is the value received in the update message.   In the Loc\-RIB, if used, it should represent a locally generated path\-id value for the corresponding route.  In Adj\-RIB\-Out, it should be the value sent to a neighbor when add\-paths is used, i.e., the capability has been negotiated
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attribute
                                        
                                        	This list contains received attributes that are unrecognized or unsupported by the local router.  The list may be empty
                                        	**type**\: list of  		 :py:class:`UnknownAttribute <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("unknown-attribute", ("unknown_attribute", BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                ('cluster_list', YLeafList(YType.str, 'cluster-list')),
                                                ('ext_community', YLeafList(YType.str, 'ext-community')),
                                                ('aigp', YLeaf(YType.uint64, 'aigp')),
                                                ('path_id', YLeaf(YType.uint32, 'path-id')),
                                            ])
                                            self.originator_id = None
                                            self.cluster_list = []
                                            self.ext_community = []
                                            self.aigp = None
                                            self.path_id = None

                                            self.unknown_attribute = YList(self)
                                            self._segment_path = lambda: "ext-attributes"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, ['originator_id', 'cluster_list', 'ext_community', 'aigp', 'path_id'], name, value)


                                        class UnknownAttribute(Entity):
                                            """
                                            This list contains received attributes that are unrecognized
                                            or unsupported by the local router.  The list may be empty.
                                            
                                            .. attribute:: attr_type  (key)
                                            
                                            	2\-octet value encoding the attribute flags and the attribute type code
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_len
                                            
                                            	One or two octet attribute length field indicating the length of the attribute data in octets.  If the Extended Length attribute flag in the attribute type field is set, the length field is 2 octets, otherwise it is 1 octet
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attr_value
                                            
                                            	Raw attribute value data, not to exceed the length indicated in the attr\-len field.  The maximum length of the attribute data is 2^16\-1 per the max value of the attr\-len field (2 octets)
                                            	**type**\: str
                                            
                                            	**length:** 1..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-bgprib'
                                            _revision = '2016-04-11'

                                            def __init__(self):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['attr_type']
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attr_type', YLeaf(YType.uint16, 'attr-type')),
                                                    ('attr_len', YLeaf(YType.uint16, 'attr-len')),
                                                    ('attr_value', YLeaf(YType.str, 'attr-value')),
                                                ])
                                                self.attr_type = None
                                                self.attr_len = None
                                                self.attr_value = None
                                                self._segment_path = lambda: "unknown-attribute" + "[attr-type='" + str(self.attr_type) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, ['attr_type', 'attr_len', 'attr_value'], name, value)

    def clone_ptr(self):
        self._top_entity = BgpRib()
        return self._top_entity

