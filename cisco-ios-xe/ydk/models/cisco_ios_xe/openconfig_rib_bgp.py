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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpRib(Entity):
    """
    Top level container for BGP RIBs
    
    .. attribute:: afi_safis
    
    	Enclosing container for address family list
    	**type**\:   :py:class:`AfiSafis <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis>`
    
    

    """

    _prefix = 'oc-bgprib'
    _revision = '2016-04-11'

    def __init__(self):
        super(BgpRib, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp-rib"
        self.yang_parent_name = "openconfig-rib-bgp"

        self.afi_safis = BgpRib.AfiSafis()
        self.afi_safis.parent = self
        self._children_name_map["afi_safis"] = "afi-safis"
        self._children_yang_names.add("afi-safis")


    class AfiSafis(Entity):
        """
        Enclosing container for address family list
        
        .. attribute:: afi_safi
        
        	list of afi\-safi types
        	**type**\: list of    :py:class:`AfiSafi <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi>`
        
        

        """

        _prefix = 'oc-bgprib'
        _revision = '2016-04-11'

        def __init__(self):
            super(BgpRib.AfiSafis, self).__init__()

            self.yang_name = "afi-safis"
            self.yang_parent_name = "bgp-rib"

            self.afi_safi = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BgpRib.AfiSafis, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BgpRib.AfiSafis, self).__setattr__(name, value)


        class AfiSafi(Entity):
            """
            list of afi\-safi types
            
            .. attribute:: afi_safi_name  <key>
            
            	AFI,SAFI
            	**type**\:   :py:class:`Afi_Safi_Type <ydk.models.openconfig.openconfig_bgp_types.Afi_Safi_Type>`
            
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
                super(BgpRib.AfiSafis.AfiSafi, self).__init__()

                self.yang_name = "afi-safi"
                self.yang_parent_name = "afi-safis"

                self.afi_safi_name = YLeaf(YType.identityref, "afi-safi-name")

                self.ipv4_unicast = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast()
                self.ipv4_unicast.parent = self
                self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                self._children_yang_names.add("ipv4-unicast")

                self.ipv6_unicast = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast()
                self.ipv6_unicast.parent = self
                self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                self._children_yang_names.add("ipv6-unicast")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("afi_safi_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BgpRib.AfiSafis.AfiSafi, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BgpRib.AfiSafis.AfiSafi, self).__setattr__(name, value)


            class Ipv4Unicast(Entity):
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
                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast, self).__init__()

                    self.yang_name = "ipv4-unicast"
                    self.yang_parent_name = "afi-safi"

                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"
                    self._children_yang_names.add("loc-rib")

                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")


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
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv4-unicast"

                        self.num_routes = YLeaf(YType.uint64, "num-routes")

                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                        self._children_yang_names.add("routes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("num_routes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib, self).__setattr__(name, value)


                    class Routes(Entity):
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
                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"

                            self.route = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes, self).__setattr__(name, value)


                        class Route(Entity):
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
                            	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                            
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"

                                self.best_path = YLeaf(YType.boolean, "best-path")

                                self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                self.last_update_received = YLeaf(YType.str, "last-update-received")

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.valid_route = YLeaf(YType.boolean, "valid-route")

                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                                self._children_yang_names.add("attributes")

                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                self._children_yang_names.add("ext-attributes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("best_path",
                                                "invalid_reason",
                                                "last_modified_date",
                                                "last_update_received",
                                                "prefix",
                                                "valid_route") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route, self).__setattr__(name, value)


                            class Attributes(Entity):
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
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes, self).__init__()

                                    self.yang_name = "attributes"
                                    self.yang_parent_name = "route"

                                    self.as4_path = YLeaf(YType.str, "as4-path")

                                    self.as_path = YLeaf(YType.str, "as-path")

                                    self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                    self.community = YLeafList(YType.str, "community")

                                    self.local_pref = YLeaf(YType.uint32, "local-pref")

                                    self.med = YLeaf(YType.uint32, "med")

                                    self.next_hop = YLeaf(YType.str, "next-hop")

                                    self.origin = YLeaf(YType.enumeration, "origin")

                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self._children_name_map["aggregator"] = "aggregator"
                                    self._children_yang_names.add("aggregator")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("as4_path",
                                                    "as_path",
                                                    "atomic_aggr",
                                                    "community",
                                                    "local_pref",
                                                    "med",
                                                    "next_hop",
                                                    "origin") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes, self).__setattr__(name, value)


                                class Aggregator(Entity):
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__init__()

                                        self.yang_name = "aggregator"
                                        self.yang_parent_name = "attributes"

                                        self.address = YLeaf(YType.str, "address")

                                        self.as4 = YLeaf(YType.uint32, "as4")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address",
                                                        "as4",
                                                        "as_") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.as4.is_set or
                                            self.as_.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.as4.yfilter != YFilter.not_set or
                                            self.as_.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregator" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as4.get_name_leafdata())
                                        if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "as4" or name == "as"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as4"):
                                            self.as4 = value
                                            self.as4.value_namespace = name_space
                                            self.as4.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as"):
                                            self.as_ = value
                                            self.as_.value_namespace = name_space
                                            self.as_.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for leaf in self.community.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.as4_path.is_set or
                                        self.as_path.is_set or
                                        self.atomic_aggr.is_set or
                                        self.local_pref.is_set or
                                        self.med.is_set or
                                        self.next_hop.is_set or
                                        self.origin.is_set or
                                        (self.aggregator is not None and self.aggregator.has_data()))

                                def has_operation(self):
                                    for leaf in self.community.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.as4_path.yfilter != YFilter.not_set or
                                        self.as_path.yfilter != YFilter.not_set or
                                        self.atomic_aggr.yfilter != YFilter.not_set or
                                        self.community.yfilter != YFilter.not_set or
                                        self.local_pref.yfilter != YFilter.not_set or
                                        self.med.yfilter != YFilter.not_set or
                                        self.next_hop.yfilter != YFilter.not_set or
                                        self.origin.yfilter != YFilter.not_set or
                                        (self.aggregator is not None and self.aggregator.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.as4_path.get_name_leafdata())
                                    if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.as_path.get_name_leafdata())
                                    if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                    if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_pref.get_name_leafdata())
                                    if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.med.get_name_leafdata())
                                    if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.next_hop.get_name_leafdata())
                                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.origin.get_name_leafdata())

                                    leaf_name_data.extend(self.community.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregator"):
                                        if (self.aggregator is None):
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                        return self.aggregator

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "as4-path"):
                                        self.as4_path = value
                                        self.as4_path.value_namespace = name_space
                                        self.as4_path.value_namespace_prefix = name_space_prefix
                                    if(value_path == "as-path"):
                                        self.as_path = value
                                        self.as_path.value_namespace = name_space
                                        self.as_path.value_namespace_prefix = name_space_prefix
                                    if(value_path == "atomic-aggr"):
                                        self.atomic_aggr = value
                                        self.atomic_aggr.value_namespace = name_space
                                        self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                    if(value_path == "community"):
                                        self.community.append(value)
                                    if(value_path == "local-pref"):
                                        self.local_pref = value
                                        self.local_pref.value_namespace = name_space
                                        self.local_pref.value_namespace_prefix = name_space_prefix
                                    if(value_path == "med"):
                                        self.med = value
                                        self.med.value_namespace = name_space
                                        self.med.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop"):
                                        self.next_hop = value
                                        self.next_hop.value_namespace = name_space
                                        self.next_hop.value_namespace_prefix = name_space_prefix
                                    if(value_path == "origin"):
                                        self.origin = value
                                        self.origin.value_namespace = name_space
                                        self.origin.value_namespace_prefix = name_space_prefix


                            class ExtAttributes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes, self).__init__()

                                    self.yang_name = "ext-attributes"
                                    self.yang_parent_name = "route"

                                    self.aigp = YLeaf(YType.uint64, "aigp")

                                    self.cluster_list = YLeafList(YType.str, "cluster-list")

                                    self.ext_community = YLeafList(YType.str, "ext-community")

                                    self.originator_id = YLeaf(YType.str, "originator-id")

                                    self.path_id = YLeaf(YType.uint32, "path-id")

                                    self.unknown_attribute = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("aigp",
                                                    "cluster_list",
                                                    "ext_community",
                                                    "originator_id",
                                                    "path_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                class UnknownAttribute(Entity):
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                        self.yang_name = "unknown-attribute"
                                        self.yang_parent_name = "ext-attributes"

                                        self.attr_type = YLeaf(YType.uint16, "attr-type")

                                        self.attr_len = YLeaf(YType.uint16, "attr-len")

                                        self.attr_value = YLeaf(YType.str, "attr-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("attr_type",
                                                        "attr_len",
                                                        "attr_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.attr_type.is_set or
                                            self.attr_len.is_set or
                                            self.attr_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.attr_type.yfilter != YFilter.not_set or
                                            self.attr_len.yfilter != YFilter.not_set or
                                            self.attr_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_type.get_name_leafdata())
                                        if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_len.get_name_leafdata())
                                        if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "attr-type"):
                                            self.attr_type = value
                                            self.attr_type.value_namespace = name_space
                                            self.attr_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "attr-len"):
                                            self.attr_len = value
                                            self.attr_len.value_namespace = name_space
                                            self.attr_len.value_namespace_prefix = name_space_prefix
                                        if(value_path == "attr-value"):
                                            self.attr_value = value
                                            self.attr_value.value_namespace = name_space
                                            self.attr_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.unknown_attribute:
                                        if (c.has_data()):
                                            return True
                                    for leaf in self.cluster_list.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    for leaf in self.ext_community.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.aigp.is_set or
                                        self.originator_id.is_set or
                                        self.path_id.is_set)

                                def has_operation(self):
                                    for c in self.unknown_attribute:
                                        if (c.has_operation()):
                                            return True
                                    for leaf in self.cluster_list.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    for leaf in self.ext_community.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.aigp.yfilter != YFilter.not_set or
                                        self.cluster_list.yfilter != YFilter.not_set or
                                        self.ext_community.yfilter != YFilter.not_set or
                                        self.originator_id.yfilter != YFilter.not_set or
                                        self.path_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ext-attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.aigp.get_name_leafdata())
                                    if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.originator_id.get_name_leafdata())
                                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.path_id.get_name_leafdata())

                                    leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                    leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "unknown-attribute"):
                                        for c in self.unknown_attribute:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.unknown_attribute.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "aigp"):
                                        self.aigp = value
                                        self.aigp.value_namespace = name_space
                                        self.aigp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "cluster-list"):
                                        self.cluster_list.append(value)
                                    if(value_path == "ext-community"):
                                        self.ext_community.append(value)
                                    if(value_path == "originator-id"):
                                        self.originator_id = value
                                        self.originator_id.value_namespace = name_space
                                        self.originator_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "path-id"):
                                        self.path_id = value
                                        self.path_id.value_namespace = name_space
                                        self.path_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.best_path.is_set or
                                    self.invalid_reason.is_set or
                                    self.last_modified_date.is_set or
                                    self.last_update_received.is_set or
                                    self.prefix.is_set or
                                    self.valid_route.is_set or
                                    (self.attributes is not None and self.attributes.has_data()) or
                                    (self.ext_attributes is not None and self.ext_attributes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.best_path.yfilter != YFilter.not_set or
                                    self.invalid_reason.yfilter != YFilter.not_set or
                                    self.last_modified_date.yfilter != YFilter.not_set or
                                    self.last_update_received.yfilter != YFilter.not_set or
                                    self.prefix.yfilter != YFilter.not_set or
                                    self.valid_route.yfilter != YFilter.not_set or
                                    (self.attributes is not None and self.attributes.has_operation()) or
                                    (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "route" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.best_path.get_name_leafdata())
                                if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix.get_name_leafdata())
                                if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.valid_route.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "attributes"):
                                    if (self.attributes is None):
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                    return self.attributes

                                if (child_yang_name == "ext-attributes"):
                                    if (self.ext_attributes is None):
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                    return self.ext_attributes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "best-path"):
                                    self.best_path = value
                                    self.best_path.value_namespace = name_space
                                    self.best_path.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid-reason"):
                                    self.invalid_reason = value
                                    self.invalid_reason.value_namespace = name_space
                                    self.invalid_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-modified-date"):
                                    self.last_modified_date = value
                                    self.last_modified_date.value_namespace = name_space
                                    self.last_modified_date.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-update-received"):
                                    self.last_update_received = value
                                    self.last_update_received.value_namespace = name_space
                                    self.last_update_received.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix"):
                                    self.prefix = value
                                    self.prefix.value_namespace = name_space
                                    self.prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "valid-route"):
                                    self.valid_route = value
                                    self.valid_route.value_namespace = name_space
                                    self.valid_route.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.route:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.route:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "routes" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "route"):
                                for c in self.route:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.route.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "route"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.num_routes.is_set or
                            (self.routes is not None and self.routes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.num_routes.yfilter != YFilter.not_set or
                            (self.routes is not None and self.routes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "loc-rib" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_routes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "routes"):
                            if (self.routes is None):
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                            return self.routes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "routes" or name == "num-routes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "num-routes"):
                            self.num_routes = value
                            self.num_routes.value_namespace = name_space
                            self.num_routes.value_namespace_prefix = name_space_prefix


                class Neighbors(Entity):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv4-unicast"

                        self.neighbor = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors, self).__setattr__(name, value)


                    class Neighbor(Entity):
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
                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                            self._children_yang_names.add("adj-rib-in-post")

                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._children_yang_names.add("adj-rib-in-pre")

                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                            self._children_yang_names.add("adj-rib-out-post")

                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                            self._children_yang_names.add("adj-rib-out-pre")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor, self).__setattr__(name, value)


                        class AdjRibInPre(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-in-pre" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibInPost(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-in-post" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibOutPre(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-out-pre" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibOutPost(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-out-post" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_address.is_set or
                                (self.adj_rib_in_post is not None and self.adj_rib_in_post.has_data()) or
                                (self.adj_rib_in_pre is not None and self.adj_rib_in_pre.has_data()) or
                                (self.adj_rib_out_post is not None and self.adj_rib_out_post.has_data()) or
                                (self.adj_rib_out_pre is not None and self.adj_rib_out_pre.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_address.yfilter != YFilter.not_set or
                                (self.adj_rib_in_post is not None and self.adj_rib_in_post.has_operation()) or
                                (self.adj_rib_in_pre is not None and self.adj_rib_in_pre.has_operation()) or
                                (self.adj_rib_out_post is not None and self.adj_rib_out_post.has_operation()) or
                                (self.adj_rib_out_pre is not None and self.adj_rib_out_pre.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "adj-rib-in-post"):
                                if (self.adj_rib_in_post is None):
                                    self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost()
                                    self.adj_rib_in_post.parent = self
                                    self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                                return self.adj_rib_in_post

                            if (child_yang_name == "adj-rib-in-pre"):
                                if (self.adj_rib_in_pre is None):
                                    self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre()
                                    self.adj_rib_in_pre.parent = self
                                    self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                                return self.adj_rib_in_pre

                            if (child_yang_name == "adj-rib-out-post"):
                                if (self.adj_rib_out_post is None):
                                    self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost()
                                    self.adj_rib_out_post.parent = self
                                    self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                                return self.adj_rib_out_post

                            if (child_yang_name == "adj-rib-out-pre"):
                                if (self.adj_rib_out_pre is None):
                                    self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre()
                                    self.adj_rib_out_pre.parent = self
                                    self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                                return self.adj_rib_out_pre

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "adj-rib-in-post" or name == "adj-rib-in-pre" or name == "adj-rib-out-post" or name == "adj-rib-out-pre" or name == "neighbor-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-address"):
                                self.neighbor_address = value
                                self.neighbor_address.value_namespace = name_space
                                self.neighbor_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.neighbor:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.neighbor:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbors" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "neighbor"):
                            for c in self.neighbor:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.neighbor.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.loc_rib is not None and self.loc_rib.has_data()) or
                        (self.neighbors is not None and self.neighbors.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.loc_rib is not None and self.loc_rib.has_operation()) or
                        (self.neighbors is not None and self.neighbors.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-unicast" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "loc-rib"):
                        if (self.loc_rib is None):
                            self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib()
                            self.loc_rib.parent = self
                            self._children_name_map["loc_rib"] = "loc-rib"
                        return self.loc_rib

                    if (child_yang_name == "neighbors"):
                        if (self.neighbors is None):
                            self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors()
                            self.neighbors.parent = self
                            self._children_name_map["neighbors"] = "neighbors"
                        return self.neighbors

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "loc-rib" or name == "neighbors"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv6Unicast(Entity):
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
                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast, self).__init__()

                    self.yang_name = "ipv6-unicast"
                    self.yang_parent_name = "afi-safi"

                    self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"
                    self._children_yang_names.add("loc-rib")

                    self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")


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
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: routes
                    
                    	Enclosing container for list of routes in the routing table
                    	**type**\:   :py:class:`Routes <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv6-unicast"

                        self.num_routes = YLeaf(YType.uint64, "num-routes")

                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"
                        self._children_yang_names.add("routes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("num_routes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib, self).__setattr__(name, value)


                    class Routes(Entity):
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
                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"

                            self.route = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes, self).__setattr__(name, value)


                        class Route(Entity):
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
                            	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                            
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"

                                self.best_path = YLeaf(YType.boolean, "best-path")

                                self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                self.last_update_received = YLeaf(YType.str, "last-update-received")

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.valid_route = YLeaf(YType.boolean, "valid-route")

                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes()
                                self.attributes.parent = self
                                self._children_name_map["attributes"] = "attributes"
                                self._children_yang_names.add("attributes")

                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes()
                                self.ext_attributes.parent = self
                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                self._children_yang_names.add("ext-attributes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("best_path",
                                                "invalid_reason",
                                                "last_modified_date",
                                                "last_update_received",
                                                "prefix",
                                                "valid_route") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route, self).__setattr__(name, value)


                            class Attributes(Entity):
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
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                

                                """

                                _prefix = 'oc-bgprib'
                                _revision = '2016-04-11'

                                def __init__(self):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes, self).__init__()

                                    self.yang_name = "attributes"
                                    self.yang_parent_name = "route"

                                    self.as4_path = YLeaf(YType.str, "as4-path")

                                    self.as_path = YLeaf(YType.str, "as-path")

                                    self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                    self.community = YLeafList(YType.str, "community")

                                    self.local_pref = YLeaf(YType.uint32, "local-pref")

                                    self.med = YLeaf(YType.uint32, "med")

                                    self.next_hop = YLeaf(YType.str, "next-hop")

                                    self.origin = YLeaf(YType.enumeration, "origin")

                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                    self.aggregator.parent = self
                                    self._children_name_map["aggregator"] = "aggregator"
                                    self._children_yang_names.add("aggregator")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("as4_path",
                                                    "as_path",
                                                    "atomic_aggr",
                                                    "community",
                                                    "local_pref",
                                                    "med",
                                                    "next_hop",
                                                    "origin") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes, self).__setattr__(name, value)


                                class Aggregator(Entity):
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__init__()

                                        self.yang_name = "aggregator"
                                        self.yang_parent_name = "attributes"

                                        self.address = YLeaf(YType.str, "address")

                                        self.as4 = YLeaf(YType.uint32, "as4")

                                        self.as_ = YLeaf(YType.uint32, "as")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address",
                                                        "as4",
                                                        "as_") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.as4.is_set or
                                            self.as_.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.as4.yfilter != YFilter.not_set or
                                            self.as_.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "aggregator" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as4.get_name_leafdata())
                                        if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "as4" or name == "as"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as4"):
                                            self.as4 = value
                                            self.as4.value_namespace = name_space
                                            self.as4.value_namespace_prefix = name_space_prefix
                                        if(value_path == "as"):
                                            self.as_ = value
                                            self.as_.value_namespace = name_space
                                            self.as_.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for leaf in self.community.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.as4_path.is_set or
                                        self.as_path.is_set or
                                        self.atomic_aggr.is_set or
                                        self.local_pref.is_set or
                                        self.med.is_set or
                                        self.next_hop.is_set or
                                        self.origin.is_set or
                                        (self.aggregator is not None and self.aggregator.has_data()))

                                def has_operation(self):
                                    for leaf in self.community.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.as4_path.yfilter != YFilter.not_set or
                                        self.as_path.yfilter != YFilter.not_set or
                                        self.atomic_aggr.yfilter != YFilter.not_set or
                                        self.community.yfilter != YFilter.not_set or
                                        self.local_pref.yfilter != YFilter.not_set or
                                        self.med.yfilter != YFilter.not_set or
                                        self.next_hop.yfilter != YFilter.not_set or
                                        self.origin.yfilter != YFilter.not_set or
                                        (self.aggregator is not None and self.aggregator.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.as4_path.get_name_leafdata())
                                    if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.as_path.get_name_leafdata())
                                    if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                    if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_pref.get_name_leafdata())
                                    if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.med.get_name_leafdata())
                                    if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.next_hop.get_name_leafdata())
                                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.origin.get_name_leafdata())

                                    leaf_name_data.extend(self.community.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "aggregator"):
                                        if (self.aggregator is None):
                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                        return self.aggregator

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "as4-path"):
                                        self.as4_path = value
                                        self.as4_path.value_namespace = name_space
                                        self.as4_path.value_namespace_prefix = name_space_prefix
                                    if(value_path == "as-path"):
                                        self.as_path = value
                                        self.as_path.value_namespace = name_space
                                        self.as_path.value_namespace_prefix = name_space_prefix
                                    if(value_path == "atomic-aggr"):
                                        self.atomic_aggr = value
                                        self.atomic_aggr.value_namespace = name_space
                                        self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                    if(value_path == "community"):
                                        self.community.append(value)
                                    if(value_path == "local-pref"):
                                        self.local_pref = value
                                        self.local_pref.value_namespace = name_space
                                        self.local_pref.value_namespace_prefix = name_space_prefix
                                    if(value_path == "med"):
                                        self.med = value
                                        self.med.value_namespace = name_space
                                        self.med.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop"):
                                        self.next_hop = value
                                        self.next_hop.value_namespace = name_space
                                        self.next_hop.value_namespace_prefix = name_space_prefix
                                    if(value_path == "origin"):
                                        self.origin = value
                                        self.origin.value_namespace = name_space
                                        self.origin.value_namespace_prefix = name_space_prefix


                            class ExtAttributes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes, self).__init__()

                                    self.yang_name = "ext-attributes"
                                    self.yang_parent_name = "route"

                                    self.aigp = YLeaf(YType.uint64, "aigp")

                                    self.cluster_list = YLeafList(YType.str, "cluster-list")

                                    self.ext_community = YLeafList(YType.str, "ext-community")

                                    self.originator_id = YLeaf(YType.str, "originator-id")

                                    self.path_id = YLeaf(YType.uint32, "path-id")

                                    self.unknown_attribute = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("aigp",
                                                    "cluster_list",
                                                    "ext_community",
                                                    "originator_id",
                                                    "path_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                class UnknownAttribute(Entity):
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                        self.yang_name = "unknown-attribute"
                                        self.yang_parent_name = "ext-attributes"

                                        self.attr_type = YLeaf(YType.uint16, "attr-type")

                                        self.attr_len = YLeaf(YType.uint16, "attr-len")

                                        self.attr_value = YLeaf(YType.str, "attr-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("attr_type",
                                                        "attr_len",
                                                        "attr_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.attr_type.is_set or
                                            self.attr_len.is_set or
                                            self.attr_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.attr_type.yfilter != YFilter.not_set or
                                            self.attr_len.yfilter != YFilter.not_set or
                                            self.attr_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_type.get_name_leafdata())
                                        if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_len.get_name_leafdata())
                                        if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.attr_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "attr-type"):
                                            self.attr_type = value
                                            self.attr_type.value_namespace = name_space
                                            self.attr_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "attr-len"):
                                            self.attr_len = value
                                            self.attr_len.value_namespace = name_space
                                            self.attr_len.value_namespace_prefix = name_space_prefix
                                        if(value_path == "attr-value"):
                                            self.attr_value = value
                                            self.attr_value.value_namespace = name_space
                                            self.attr_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.unknown_attribute:
                                        if (c.has_data()):
                                            return True
                                    for leaf in self.cluster_list.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    for leaf in self.ext_community.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.aigp.is_set or
                                        self.originator_id.is_set or
                                        self.path_id.is_set)

                                def has_operation(self):
                                    for c in self.unknown_attribute:
                                        if (c.has_operation()):
                                            return True
                                    for leaf in self.cluster_list.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    for leaf in self.ext_community.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.aigp.yfilter != YFilter.not_set or
                                        self.cluster_list.yfilter != YFilter.not_set or
                                        self.ext_community.yfilter != YFilter.not_set or
                                        self.originator_id.yfilter != YFilter.not_set or
                                        self.path_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ext-attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.aigp.get_name_leafdata())
                                    if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.originator_id.get_name_leafdata())
                                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.path_id.get_name_leafdata())

                                    leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                    leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "unknown-attribute"):
                                        for c in self.unknown_attribute:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.unknown_attribute.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "aigp"):
                                        self.aigp = value
                                        self.aigp.value_namespace = name_space
                                        self.aigp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "cluster-list"):
                                        self.cluster_list.append(value)
                                    if(value_path == "ext-community"):
                                        self.ext_community.append(value)
                                    if(value_path == "originator-id"):
                                        self.originator_id = value
                                        self.originator_id.value_namespace = name_space
                                        self.originator_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "path-id"):
                                        self.path_id = value
                                        self.path_id.value_namespace = name_space
                                        self.path_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.best_path.is_set or
                                    self.invalid_reason.is_set or
                                    self.last_modified_date.is_set or
                                    self.last_update_received.is_set or
                                    self.prefix.is_set or
                                    self.valid_route.is_set or
                                    (self.attributes is not None and self.attributes.has_data()) or
                                    (self.ext_attributes is not None and self.ext_attributes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.best_path.yfilter != YFilter.not_set or
                                    self.invalid_reason.yfilter != YFilter.not_set or
                                    self.last_modified_date.yfilter != YFilter.not_set or
                                    self.last_update_received.yfilter != YFilter.not_set or
                                    self.prefix.yfilter != YFilter.not_set or
                                    self.valid_route.yfilter != YFilter.not_set or
                                    (self.attributes is not None and self.attributes.has_operation()) or
                                    (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "route" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.best_path.get_name_leafdata())
                                if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix.get_name_leafdata())
                                if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.valid_route.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "attributes"):
                                    if (self.attributes is None):
                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                    return self.attributes

                                if (child_yang_name == "ext-attributes"):
                                    if (self.ext_attributes is None):
                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                    return self.ext_attributes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "best-path"):
                                    self.best_path = value
                                    self.best_path.value_namespace = name_space
                                    self.best_path.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid-reason"):
                                    self.invalid_reason = value
                                    self.invalid_reason.value_namespace = name_space
                                    self.invalid_reason.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-modified-date"):
                                    self.last_modified_date = value
                                    self.last_modified_date.value_namespace = name_space
                                    self.last_modified_date.value_namespace_prefix = name_space_prefix
                                if(value_path == "last-update-received"):
                                    self.last_update_received = value
                                    self.last_update_received.value_namespace = name_space
                                    self.last_update_received.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix"):
                                    self.prefix = value
                                    self.prefix.value_namespace = name_space
                                    self.prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "valid-route"):
                                    self.valid_route = value
                                    self.valid_route.value_namespace = name_space
                                    self.valid_route.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.route:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.route:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "routes" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "route"):
                                for c in self.route:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.route.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "route"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.num_routes.is_set or
                            (self.routes is not None and self.routes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.num_routes.yfilter != YFilter.not_set or
                            (self.routes is not None and self.routes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "loc-rib" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.num_routes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "routes"):
                            if (self.routes is None):
                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                            return self.routes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "routes" or name == "num-routes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "num-routes"):
                            self.num_routes = value
                            self.num_routes.value_namespace = name_space
                            self.num_routes.value_namespace_prefix = name_space_prefix


                class Neighbors(Entity):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	List of neighbors (peers) of the local BGP speaker
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_rib_bgp.BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-bgprib'
                    _revision = '2016-04-11'

                    def __init__(self):
                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv6-unicast"

                        self.neighbor = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors, self).__setattr__(name, value)


                    class Neighbor(Entity):
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
                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"

                            self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                            self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                            self._children_yang_names.add("adj-rib-in-post")

                            self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._children_yang_names.add("adj-rib-in-pre")

                            self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                            self._children_yang_names.add("adj-rib-out-post")

                            self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                            self._children_yang_names.add("adj-rib-out-pre")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor, self).__setattr__(name, value)


                        class AdjRibInPre(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-in-pre" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibInPost(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-in-post" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibOutPre(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-out-pre" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix


                        class AdjRibOutPost(Entity):
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
                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "neighbor"

                                self.num_routes = YLeaf(YType.uint64, "num-routes")

                                self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"
                                self._children_yang_names.add("routes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("num_routes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost, self).__setattr__(name, value)


                            class Routes(Entity):
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
                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"

                                    self.route = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes, self).__setattr__(name, value)


                                class Route(Entity):
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
                                    	**type**\:   :py:class:`Invalid_Route_Reason <ydk.models.openconfig.openconfig_rib_bgp_types.Invalid_Route_Reason>`
                                    
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
                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"

                                        self.best_path = YLeaf(YType.boolean, "best-path")

                                        self.invalid_reason = YLeaf(YType.identityref, "invalid-reason")

                                        self.last_modified_date = YLeaf(YType.str, "last-modified-date")

                                        self.last_update_received = YLeaf(YType.str, "last-update-received")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.valid_route = YLeaf(YType.boolean, "valid-route")

                                        self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                        self.attributes.parent = self
                                        self._children_name_map["attributes"] = "attributes"
                                        self._children_yang_names.add("attributes")

                                        self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                        self.ext_attributes.parent = self
                                        self._children_name_map["ext_attributes"] = "ext-attributes"
                                        self._children_yang_names.add("ext-attributes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("best_path",
                                                        "invalid_reason",
                                                        "last_modified_date",
                                                        "last_update_received",
                                                        "prefix",
                                                        "valid_route") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route, self).__setattr__(name, value)


                                    class Attributes(Entity):
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
                                        	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgprib'
                                        _revision = '2016-04-11'

                                        def __init__(self):
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__init__()

                                            self.yang_name = "attributes"
                                            self.yang_parent_name = "route"

                                            self.as4_path = YLeaf(YType.str, "as4-path")

                                            self.as_path = YLeaf(YType.str, "as-path")

                                            self.atomic_aggr = YLeaf(YType.boolean, "atomic-aggr")

                                            self.community = YLeafList(YType.str, "community")

                                            self.local_pref = YLeaf(YType.uint32, "local-pref")

                                            self.med = YLeaf(YType.uint32, "med")

                                            self.next_hop = YLeaf(YType.str, "next-hop")

                                            self.origin = YLeaf(YType.enumeration, "origin")

                                            self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                            self.aggregator.parent = self
                                            self._children_name_map["aggregator"] = "aggregator"
                                            self._children_yang_names.add("aggregator")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("as4_path",
                                                            "as_path",
                                                            "atomic_aggr",
                                                            "community",
                                                            "local_pref",
                                                            "med",
                                                            "next_hop",
                                                            "origin") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes, self).__setattr__(name, value)


                                        class Aggregator(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__init__()

                                                self.yang_name = "aggregator"
                                                self.yang_parent_name = "attributes"

                                                self.address = YLeaf(YType.str, "address")

                                                self.as4 = YLeaf(YType.uint32, "as4")

                                                self.as_ = YLeaf(YType.uint32, "as")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("address",
                                                                "as4",
                                                                "as_") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.address.is_set or
                                                    self.as4.is_set or
                                                    self.as_.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.address.yfilter != YFilter.not_set or
                                                    self.as4.yfilter != YFilter.not_set or
                                                    self.as_.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "aggregator" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.address.get_name_leafdata())
                                                if (self.as4.is_set or self.as4.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as4.get_name_leafdata())
                                                if (self.as_.is_set or self.as_.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "address" or name == "as4" or name == "as"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "address"):
                                                    self.address = value
                                                    self.address.value_namespace = name_space
                                                    self.address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as4"):
                                                    self.as4 = value
                                                    self.as4.value_namespace = name_space
                                                    self.as4.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as"):
                                                    self.as_ = value
                                                    self.as_.value_namespace = name_space
                                                    self.as_.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.as4_path.is_set or
                                                self.as_path.is_set or
                                                self.atomic_aggr.is_set or
                                                self.local_pref.is_set or
                                                self.med.is_set or
                                                self.next_hop.is_set or
                                                self.origin.is_set or
                                                (self.aggregator is not None and self.aggregator.has_data()))

                                        def has_operation(self):
                                            for leaf in self.community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.as4_path.yfilter != YFilter.not_set or
                                                self.as_path.yfilter != YFilter.not_set or
                                                self.atomic_aggr.yfilter != YFilter.not_set or
                                                self.community.yfilter != YFilter.not_set or
                                                self.local_pref.yfilter != YFilter.not_set or
                                                self.med.yfilter != YFilter.not_set or
                                                self.next_hop.yfilter != YFilter.not_set or
                                                self.origin.yfilter != YFilter.not_set or
                                                (self.aggregator is not None and self.aggregator.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.as4_path.is_set or self.as4_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as4_path.get_name_leafdata())
                                            if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.as_path.get_name_leafdata())
                                            if (self.atomic_aggr.is_set or self.atomic_aggr.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.atomic_aggr.get_name_leafdata())
                                            if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.local_pref.get_name_leafdata())
                                            if (self.med.is_set or self.med.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.med.get_name_leafdata())
                                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                                            if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.origin.get_name_leafdata())

                                            leaf_name_data.extend(self.community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "aggregator"):
                                                if (self.aggregator is None):
                                                    self.aggregator = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator()
                                                    self.aggregator.parent = self
                                                    self._children_name_map["aggregator"] = "aggregator"
                                                return self.aggregator

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "aggregator" or name == "as4-path" or name == "as-path" or name == "atomic-aggr" or name == "community" or name == "local-pref" or name == "med" or name == "next-hop" or name == "origin"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "as4-path"):
                                                self.as4_path = value
                                                self.as4_path.value_namespace = name_space
                                                self.as4_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "as-path"):
                                                self.as_path = value
                                                self.as_path.value_namespace = name_space
                                                self.as_path.value_namespace_prefix = name_space_prefix
                                            if(value_path == "atomic-aggr"):
                                                self.atomic_aggr = value
                                                self.atomic_aggr.value_namespace = name_space
                                                self.atomic_aggr.value_namespace_prefix = name_space_prefix
                                            if(value_path == "community"):
                                                self.community.append(value)
                                            if(value_path == "local-pref"):
                                                self.local_pref = value
                                                self.local_pref.value_namespace = name_space
                                                self.local_pref.value_namespace_prefix = name_space_prefix
                                            if(value_path == "med"):
                                                self.med = value
                                                self.med.value_namespace = name_space
                                                self.med.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop"):
                                                self.next_hop = value
                                                self.next_hop.value_namespace = name_space
                                                self.next_hop.value_namespace_prefix = name_space_prefix
                                            if(value_path == "origin"):
                                                self.origin = value
                                                self.origin.value_namespace = name_space
                                                self.origin.value_namespace_prefix = name_space_prefix


                                    class ExtAttributes(Entity):
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
                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__init__()

                                            self.yang_name = "ext-attributes"
                                            self.yang_parent_name = "route"

                                            self.aigp = YLeaf(YType.uint64, "aigp")

                                            self.cluster_list = YLeafList(YType.str, "cluster-list")

                                            self.ext_community = YLeafList(YType.str, "ext-community")

                                            self.originator_id = YLeaf(YType.str, "originator-id")

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.unknown_attribute = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("aigp",
                                                            "cluster_list",
                                                            "ext_community",
                                                            "originator_id",
                                                            "path_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes, self).__setattr__(name, value)


                                        class UnknownAttribute(Entity):
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
                                                super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__init__()

                                                self.yang_name = "unknown-attribute"
                                                self.yang_parent_name = "ext-attributes"

                                                self.attr_type = YLeaf(YType.uint16, "attr-type")

                                                self.attr_len = YLeaf(YType.uint16, "attr-len")

                                                self.attr_value = YLeaf(YType.str, "attr-value")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("attr_type",
                                                                "attr_len",
                                                                "attr_value") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.attr_type.is_set or
                                                    self.attr_len.is_set or
                                                    self.attr_value.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.attr_type.yfilter != YFilter.not_set or
                                                    self.attr_len.yfilter != YFilter.not_set or
                                                    self.attr_value.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "unknown-attribute" + "[attr-type='" + self.attr_type.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.attr_type.is_set or self.attr_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_type.get_name_leafdata())
                                                if (self.attr_len.is_set or self.attr_len.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_len.get_name_leafdata())
                                                if (self.attr_value.is_set or self.attr_value.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.attr_value.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "attr-type" or name == "attr-len" or name == "attr-value"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "attr-type"):
                                                    self.attr_type = value
                                                    self.attr_type.value_namespace = name_space
                                                    self.attr_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-len"):
                                                    self.attr_len = value
                                                    self.attr_len.value_namespace = name_space
                                                    self.attr_len.value_namespace_prefix = name_space_prefix
                                                if(value_path == "attr-value"):
                                                    self.attr_value = value
                                                    self.attr_value.value_namespace = name_space
                                                    self.attr_value.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_data()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.aigp.is_set or
                                                self.originator_id.is_set or
                                                self.path_id.is_set)

                                        def has_operation(self):
                                            for c in self.unknown_attribute:
                                                if (c.has_operation()):
                                                    return True
                                            for leaf in self.cluster_list.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            for leaf in self.ext_community.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.aigp.yfilter != YFilter.not_set or
                                                self.cluster_list.yfilter != YFilter.not_set or
                                                self.ext_community.yfilter != YFilter.not_set or
                                                self.originator_id.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "ext-attributes" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.aigp.is_set or self.aigp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.aigp.get_name_leafdata())
                                            if (self.originator_id.is_set or self.originator_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.originator_id.get_name_leafdata())
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())

                                            leaf_name_data.extend(self.cluster_list.get_name_leafdata())

                                            leaf_name_data.extend(self.ext_community.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "unknown-attribute"):
                                                for c in self.unknown_attribute:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.unknown_attribute.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "unknown-attribute" or name == "aigp" or name == "cluster-list" or name == "ext-community" or name == "originator-id" or name == "path-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "aigp"):
                                                self.aigp = value
                                                self.aigp.value_namespace = name_space
                                                self.aigp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "cluster-list"):
                                                self.cluster_list.append(value)
                                            if(value_path == "ext-community"):
                                                self.ext_community.append(value)
                                            if(value_path == "originator-id"):
                                                self.originator_id = value
                                                self.originator_id.value_namespace = name_space
                                                self.originator_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.best_path.is_set or
                                            self.invalid_reason.is_set or
                                            self.last_modified_date.is_set or
                                            self.last_update_received.is_set or
                                            self.prefix.is_set or
                                            self.valid_route.is_set or
                                            (self.attributes is not None and self.attributes.has_data()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.best_path.yfilter != YFilter.not_set or
                                            self.invalid_reason.yfilter != YFilter.not_set or
                                            self.last_modified_date.yfilter != YFilter.not_set or
                                            self.last_update_received.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.valid_route.yfilter != YFilter.not_set or
                                            (self.attributes is not None and self.attributes.has_operation()) or
                                            (self.ext_attributes is not None and self.ext_attributes.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "route" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.best_path.is_set or self.best_path.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.best_path.get_name_leafdata())
                                        if (self.invalid_reason.is_set or self.invalid_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.invalid_reason.get_name_leafdata())
                                        if (self.last_modified_date.is_set or self.last_modified_date.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_modified_date.get_name_leafdata())
                                        if (self.last_update_received.is_set or self.last_update_received.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.last_update_received.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.valid_route.is_set or self.valid_route.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.valid_route.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "attributes"):
                                            if (self.attributes is None):
                                                self.attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes()
                                                self.attributes.parent = self
                                                self._children_name_map["attributes"] = "attributes"
                                            return self.attributes

                                        if (child_yang_name == "ext-attributes"):
                                            if (self.ext_attributes is None):
                                                self.ext_attributes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes()
                                                self.ext_attributes.parent = self
                                                self._children_name_map["ext_attributes"] = "ext-attributes"
                                            return self.ext_attributes

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "attributes" or name == "ext-attributes" or name == "best-path" or name == "invalid-reason" or name == "last-modified-date" or name == "last-update-received" or name == "prefix" or name == "valid-route"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "best-path"):
                                            self.best_path = value
                                            self.best_path.value_namespace = name_space
                                            self.best_path.value_namespace_prefix = name_space_prefix
                                        if(value_path == "invalid-reason"):
                                            self.invalid_reason = value
                                            self.invalid_reason.value_namespace = name_space
                                            self.invalid_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-modified-date"):
                                            self.last_modified_date = value
                                            self.last_modified_date.value_namespace = name_space
                                            self.last_modified_date.value_namespace_prefix = name_space_prefix
                                        if(value_path == "last-update-received"):
                                            self.last_update_received = value
                                            self.last_update_received.value_namespace = name_space
                                            self.last_update_received.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "valid-route"):
                                            self.valid_route = value
                                            self.valid_route.value_namespace = name_space
                                            self.valid_route.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.route:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.route:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "routes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "route"):
                                        for c in self.route:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.route.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "route"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.num_routes.is_set or
                                    (self.routes is not None and self.routes.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.num_routes.yfilter != YFilter.not_set or
                                    (self.routes is not None and self.routes.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "adj-rib-out-post" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.num_routes.is_set or self.num_routes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.num_routes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "routes"):
                                    if (self.routes is None):
                                        self.routes = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes()
                                        self.routes.parent = self
                                        self._children_name_map["routes"] = "routes"
                                    return self.routes

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "routes" or name == "num-routes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "num-routes"):
                                    self.num_routes = value
                                    self.num_routes.value_namespace = name_space
                                    self.num_routes.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_address.is_set or
                                (self.adj_rib_in_post is not None and self.adj_rib_in_post.has_data()) or
                                (self.adj_rib_in_pre is not None and self.adj_rib_in_pre.has_data()) or
                                (self.adj_rib_out_post is not None and self.adj_rib_out_post.has_data()) or
                                (self.adj_rib_out_pre is not None and self.adj_rib_out_pre.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_address.yfilter != YFilter.not_set or
                                (self.adj_rib_in_post is not None and self.adj_rib_in_post.has_operation()) or
                                (self.adj_rib_in_pre is not None and self.adj_rib_in_pre.has_operation()) or
                                (self.adj_rib_out_post is not None and self.adj_rib_out_post.has_operation()) or
                                (self.adj_rib_out_pre is not None and self.adj_rib_out_pre.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "adj-rib-in-post"):
                                if (self.adj_rib_in_post is None):
                                    self.adj_rib_in_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost()
                                    self.adj_rib_in_post.parent = self
                                    self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"
                                return self.adj_rib_in_post

                            if (child_yang_name == "adj-rib-in-pre"):
                                if (self.adj_rib_in_pre is None):
                                    self.adj_rib_in_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre()
                                    self.adj_rib_in_pre.parent = self
                                    self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                                return self.adj_rib_in_pre

                            if (child_yang_name == "adj-rib-out-post"):
                                if (self.adj_rib_out_post is None):
                                    self.adj_rib_out_post = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost()
                                    self.adj_rib_out_post.parent = self
                                    self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"
                                return self.adj_rib_out_post

                            if (child_yang_name == "adj-rib-out-pre"):
                                if (self.adj_rib_out_pre is None):
                                    self.adj_rib_out_pre = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre()
                                    self.adj_rib_out_pre.parent = self
                                    self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"
                                return self.adj_rib_out_pre

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "adj-rib-in-post" or name == "adj-rib-in-pre" or name == "adj-rib-out-post" or name == "adj-rib-out-pre" or name == "neighbor-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-address"):
                                self.neighbor_address = value
                                self.neighbor_address.value_namespace = name_space
                                self.neighbor_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.neighbor:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.neighbor:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbors" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "neighbor"):
                            for c in self.neighbor:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.neighbor.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.loc_rib is not None and self.loc_rib.has_data()) or
                        (self.neighbors is not None and self.neighbors.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.loc_rib is not None and self.loc_rib.has_operation()) or
                        (self.neighbors is not None and self.neighbors.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6-unicast" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "loc-rib"):
                        if (self.loc_rib is None):
                            self.loc_rib = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib()
                            self.loc_rib.parent = self
                            self._children_name_map["loc_rib"] = "loc-rib"
                        return self.loc_rib

                    if (child_yang_name == "neighbors"):
                        if (self.neighbors is None):
                            self.neighbors = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors()
                            self.neighbors.parent = self
                            self._children_name_map["neighbors"] = "neighbors"
                        return self.neighbors

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "loc-rib" or name == "neighbors"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.afi_safi_name.is_set or
                    (self.ipv4_unicast is not None and self.ipv4_unicast.has_data()) or
                    (self.ipv6_unicast is not None and self.ipv6_unicast.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.afi_safi_name.yfilter != YFilter.not_set or
                    (self.ipv4_unicast is not None and self.ipv4_unicast.has_operation()) or
                    (self.ipv6_unicast is not None and self.ipv6_unicast.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "afi-safi" + "[afi-safi-name='" + self.afi_safi_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-rib-bgp:bgp-rib/afi-safis/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.afi_safi_name.is_set or self.afi_safi_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.afi_safi_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-unicast"):
                    if (self.ipv4_unicast is None):
                        self.ipv4_unicast = BgpRib.AfiSafis.AfiSafi.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                    return self.ipv4_unicast

                if (child_yang_name == "ipv6-unicast"):
                    if (self.ipv6_unicast is None):
                        self.ipv6_unicast = BgpRib.AfiSafis.AfiSafi.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                    return self.ipv6_unicast

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-unicast" or name == "ipv6-unicast" or name == "afi-safi-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "afi-safi-name"):
                    self.afi_safi_name = value
                    self.afi_safi_name.value_namespace = name_space
                    self.afi_safi_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.afi_safi:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.afi_safi:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "afi-safis" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-rib-bgp:bgp-rib/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "afi-safi"):
                for c in self.afi_safi:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BgpRib.AfiSafis.AfiSafi()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.afi_safi.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "afi-safi"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.afi_safis is not None and self.afi_safis.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.afi_safis is not None and self.afi_safis.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-rib-bgp:bgp-rib" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "afi-safis"):
            if (self.afi_safis is None):
                self.afi_safis = BgpRib.AfiSafis()
                self.afi_safis.parent = self
                self._children_name_map["afi_safis"] = "afi-safis"
            return self.afi_safis

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "afi-safis"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BgpRib()
        return self._top_entity

