""" Cisco_IOS_XR_ipv4_bgp_oc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-bgp\-oc package operational data.

This module contains definitions
for the following management objects\:
  oc\-bgp\: OC\-BGP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpOcAfi(Enum):
    """
    BgpOcAfi (Enum Class)

    BGP Address family

    .. data:: ipv4 = 0

    	IPv4 unicast

    .. data:: ipv6 = 5

    	IPv6 unicast

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(5, "ipv6")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcAfi']


class BgpOcInvalidRouteReason(Enum):
    """
    BgpOcInvalidRouteReason (Enum Class)

    Invalid route reason

    .. data:: valid_route = 1

    	Valid route

    .. data:: invalid_clsuter_loop = 2

    	ClusterLoop

    .. data:: invalid_as_path_loop = 3

    	AsPathLoop

    .. data:: invalid_origin_at_or_id = 4

    	OriginatorID

    .. data:: invalid_as_confed_loop = 5

    	ASConfedLoop

    """

    valid_route = Enum.YLeaf(1, "valid-route")

    invalid_clsuter_loop = Enum.YLeaf(2, "invalid-clsuter-loop")

    invalid_as_path_loop = Enum.YLeaf(3, "invalid-as-path-loop")

    invalid_origin_at_or_id = Enum.YLeaf(4, "invalid-origin-at-or-id")

    invalid_as_confed_loop = Enum.YLeaf(5, "invalid-as-confed-loop")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcInvalidRouteReason']


class BgpOcOriginAttr(Enum):
    """
    BgpOcOriginAttr (Enum Class)

    Origin Type

    .. data:: igp = 0

    	IGP

    .. data:: egp = 1

    	EGP

    .. data:: incomplete = 2

    	Incomplete

    """

    igp = Enum.YLeaf(0, "igp")

    egp = Enum.YLeaf(1, "egp")

    incomplete = Enum.YLeaf(2, "incomplete")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcOriginAttr']



class OcBgp(_Entity_):
    """
    OC\-BGP operational data
    
    .. attribute:: bgp_rib
    
    	BGP\-RIB operational data
    	**type**\:  :py:class:`BgpRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv4-bgp-oc-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(OcBgp, self).__init__()
        self._top_entity = None

        self.yang_name = "oc-bgp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-bgp-oc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("bgp-rib", ("bgp_rib", OcBgp.BgpRib))])
        self._leafs = OrderedDict()

        self.bgp_rib = OcBgp.BgpRib()
        self.bgp_rib.parent = self
        self._children_name_map["bgp_rib"] = "bgp-rib"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OcBgp, [], name, value)


    class BgpRib(_Entity_):
        """
        BGP\-RIB operational data
        
        .. attribute:: afi_safi_table
        
        	AFI\-SAFIs information
        	**type**\:  :py:class:`AfiSafiTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-bgp-oc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(OcBgp.BgpRib, self).__init__()

            self.yang_name = "bgp-rib"
            self.yang_parent_name = "oc-bgp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("afi-safi-table", ("afi_safi_table", OcBgp.BgpRib.AfiSafiTable))])
            self._leafs = OrderedDict()

            self.afi_safi_table = OcBgp.BgpRib.AfiSafiTable()
            self.afi_safi_table.parent = self
            self._children_name_map["afi_safi_table"] = "afi-safi-table"
            self._segment_path = lambda: "bgp-rib"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OcBgp.BgpRib, [], name, value)


        class AfiSafiTable(_Entity_):
            """
            AFI\-SAFIs information
            
            .. attribute:: ipv4_unicast
            
            	IPv4 Unicast
            	**type**\:  :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast>`
            
            	**config**\: False
            
            .. attribute:: ipv6_unicast
            
            	IPv6 Unicast
            	**type**\:  :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-bgp-oc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(OcBgp.BgpRib.AfiSafiTable, self).__init__()

                self.yang_name = "afi-safi-table"
                self.yang_parent_name = "bgp-rib"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4-unicast", ("ipv4_unicast", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast)), ("ipv6-unicast", ("ipv6_unicast", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast))])
                self._leafs = OrderedDict()

                self.ipv4_unicast = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast()
                self.ipv4_unicast.parent = self
                self._children_name_map["ipv4_unicast"] = "ipv4-unicast"

                self.ipv6_unicast = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast()
                self.ipv6_unicast.parent = self
                self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                self._segment_path = lambda: "afi-safi-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable, [], name, value)


            class Ipv4Unicast(_Entity_):
                """
                IPv4 Unicast
                
                .. attribute:: loc_rib
                
                	Local rib route table
                	**type**\:  :py:class:`LocRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib>`
                
                	**config**\: False
                
                .. attribute:: open_config_neighbors
                
                	Neighbor list
                	**type**\:  :py:class:`OpenConfigNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-bgp-oc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast, self).__init__()

                    self.yang_name = "ipv4-unicast"
                    self.yang_parent_name = "afi-safi-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("loc-rib", ("loc_rib", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib)), ("open-config-neighbors", ("open_config_neighbors", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors))])
                    self._leafs = OrderedDict()

                    self.loc_rib = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"

                    self.open_config_neighbors = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors()
                    self.open_config_neighbors.parent = self
                    self._children_name_map["open_config_neighbors"] = "open-config-neighbors"
                    self._segment_path = lambda: "ipv4-unicast"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast, [], name, value)


                class LocRib(_Entity_):
                    """
                    Local rib route table
                    
                    .. attribute:: routes
                    
                    	routes table
                    	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes>`
                    
                    	**config**\: False
                    
                    .. attribute:: num_routes
                    
                    	Number of routes in adjacency rib out\-bound post\-policy table
                    	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv4-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes))])
                        self._leafs = OrderedDict()

                        self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"

                        self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes()
                        self.num_routes.parent = self
                        self._children_name_map["num_routes"] = "num-routes"
                        self._segment_path = lambda: "loc-rib"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib, [], name, value)


                    class Routes(_Entity_):
                        """
                        routes table
                        
                        .. attribute:: route
                        
                        	route entry
                        	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "routes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes, [], name, value)


                        class Route(_Entity_):
                            """
                            route entry
                            
                            .. attribute:: route
                            
                            	Network in prefix/length format
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**config**\: False
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: path_id
                            
                            	Path ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prefix_name
                            
                            	Prefix
                            	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName>`
                            
                            	**config**\: False
                            
                            .. attribute:: route_attr_list
                            
                            	RouteAttributesList
                            	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList>`
                            
                            	**config**\: False
                            
                            .. attribute:: ext_attributes_list
                            
                            	ExtAttributesList
                            	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList>`
                            
                            	**config**\: False
                            
                            .. attribute:: last_modified_date
                            
                            	LastModifiedDate
                            	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate>`
                            
                            	**config**\: False
                            
                            .. attribute:: last_update_recieved
                            
                            	LastUpdateRecieved
                            	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid_route
                            
                            	ValidRoute
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: invalid_reason
                            
                            	IndentityRef
                            	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                            
                            	**config**\: False
                            
                            .. attribute:: best_path
                            
                            	BestPath
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved))])
                                self._leafs = OrderedDict([
                                    ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                    ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                    ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                    ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                    ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                ])
                                self.route = None
                                self.neighbor_address = None
                                self.path_id = None
                                self.valid_route = None
                                self.invalid_reason = None
                                self.best_path = None

                                self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName()
                                self.prefix_name.parent = self
                                self._children_name_map["prefix_name"] = "prefix-name"

                                self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList()
                                self.route_attr_list.parent = self
                                self._children_name_map["route_attr_list"] = "route-attr-list"

                                self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList()
                                self.ext_attributes_list.parent = self
                                self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate()
                                self.last_modified_date.parent = self
                                self._children_name_map["last_modified_date"] = "last-modified-date"

                                self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved()
                                self.last_update_recieved.parent = self
                                self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                self._segment_path = lambda: "route"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                            class PrefixName(_Entity_):
                                """
                                Prefix
                                
                                .. attribute:: prefix
                                
                                	Prefix
                                	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix>`
                                
                                	**config**\: False
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName, self).__init__()

                                    self.yang_name = "prefix-name"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix))])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                    ])
                                    self.prefix_length = None

                                    self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"
                                    self._segment_path = lambda: "prefix-name"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                class Prefix(_Entity_):
                                    """
                                    Prefix
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix, self).__init__()

                                        self.yang_name = "prefix"
                                        self.yang_parent_name = "prefix-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "prefix"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/prefix-name/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName']['meta_info']


                            class RouteAttrList(_Entity_):
                                """
                                RouteAttributesList
                                
                                .. attribute:: next_hop
                                
                                	NextHopAddress
                                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: aggregrator_attributes
                                
                                	AggregatorList
                                	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                
                                	**config**\: False
                                
                                .. attribute:: origin_type
                                
                                	Origin Attribute Type
                                	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                
                                	**config**\: False
                                
                                .. attribute:: as_path
                                
                                	AS Path
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: as4_path
                                
                                	AS4 Path
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: med
                                
                                	Med
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_pref
                                
                                	LocalPref
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: atomic_aggr
                                
                                	AtomicAggr
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: community
                                
                                	CommunityArray
                                	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList, self).__init__()

                                    self.yang_name = "route-attr-list"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community))])
                                    self._leafs = OrderedDict([
                                        ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                        ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                        ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                        ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                        ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                        ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                    ])
                                    self.origin_type = None
                                    self.as_path = None
                                    self.as4_path = None
                                    self.med = None
                                    self.local_pref = None
                                    self.atomic_aggr = None

                                    self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"

                                    self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes()
                                    self.aggregrator_attributes.parent = self
                                    self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                    self.community = YList(self)
                                    self._segment_path = lambda: "route-attr-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                class NextHop(_Entity_):
                                    """
                                    NextHopAddress
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                class AggregratorAttributes(_Entity_):
                                    """
                                    AggregatorList
                                    
                                    .. attribute:: as_
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: as4
                                    
                                    	AS4 number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                        self.yang_name = "aggregrator-attributes"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                            ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.as_ = None
                                        self.as4 = None
                                        self.address = None
                                        self._segment_path = lambda: "aggregrator-attributes"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                class Community(_Entity_):
                                    """
                                    CommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community, self).__init__()

                                        self.yang_name = "community"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                        ])
                                        self.objects = None
                                        self._segment_path = lambda: "community"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']


                            class ExtAttributesList(_Entity_):
                                """
                                ExtAttributesList
                                
                                .. attribute:: originator_id
                                
                                	OriginatorID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: aigp
                                
                                	AIGP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: path_id
                                
                                	PathId
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: cluster
                                
                                	ClusterList
                                	**type**\: list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: ext_community
                                
                                	ExtendedCommunityArray
                                	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity>`
                                
                                	**config**\: False
                                
                                .. attribute:: unknown_attributes
                                
                                	UnknownAttributes
                                	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList, self).__init__()

                                    self.yang_name = "ext-attributes-list"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                    self._leafs = OrderedDict([
                                        ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                        ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                        ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                        ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                    ])
                                    self.originator_id = None
                                    self.aigp = None
                                    self.path_id = None
                                    self.cluster = []

                                    self.ext_community = YList(self)
                                    self.unknown_attributes = YList(self)
                                    self._segment_path = lambda: "ext-attributes-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                class ExtCommunity(_Entity_):
                                    """
                                    ExtendedCommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                        self.yang_name = "ext-community"
                                        self.yang_parent_name = "ext-attributes-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                        ])
                                        self.objects = None
                                        self._segment_path = lambda: "ext-community"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/ext-attributes-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                class UnknownAttributes(_Entity_):
                                    """
                                    UnknownAttributes
                                    
                                    .. attribute:: attribute_type
                                    
                                    	AttributeType
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: attribute_length
                                    
                                    	AttributeLength
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: attribute_value
                                    
                                    	Atributevalue
                                    	**type**\: str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                        self.yang_name = "unknown-attributes"
                                        self.yang_parent_name = "ext-attributes-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                            ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                            ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                        ])
                                        self.attribute_type = None
                                        self.attribute_length = None
                                        self.attribute_value = None
                                        self._segment_path = lambda: "unknown-attributes"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/ext-attributes-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']


                            class LastModifiedDate(_Entity_):
                                """
                                LastModifiedDate
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate, self).__init__()

                                    self.yang_name = "last-modified-date"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                    ])
                                    self.time_value = None
                                    self._segment_path = lambda: "last-modified-date"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info']


                            class LastUpdateRecieved(_Entity_):
                                """
                                LastUpdateRecieved
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved, self).__init__()

                                    self.yang_name = "last-update-recieved"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                    ])
                                    self.time_value = None
                                    self._segment_path = lambda: "last-update-recieved"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes']['meta_info']


                    class NumRoutes(_Entity_):
                        """
                        Number of routes in adjacency rib out\-bound
                        post\-policy table
                        
                        .. attribute:: num_routes
                        
                        	NumRoutes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes, self).__init__()

                            self.yang_name = "num-routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                            ])
                            self.num_routes = None
                            self._segment_path = lambda: "num-routes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/loc-rib/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes, ['num_routes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib']['meta_info']


                class OpenConfigNeighbors(_Entity_):
                    """
                    Neighbor list
                    
                    .. attribute:: open_config_neighbor
                    
                    	Neighbor name
                    	**type**\: list of  		 :py:class:`OpenConfigNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors, self).__init__()

                        self.yang_name = "open-config-neighbors"
                        self.yang_parent_name = "ipv4-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("open-config-neighbor", ("open_config_neighbor", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor))])
                        self._leafs = OrderedDict()

                        self.open_config_neighbor = YList(self)
                        self._segment_path = lambda: "open-config-neighbors"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors, [], name, value)


                    class OpenConfigNeighbor(_Entity_):
                        """
                        Neighbor name
                        
                        .. attribute:: neighbor_address  (key)
                        
                        	Neighbor Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_in_post
                        
                        	Adjacency rib in\-bound post\-policy table
                        	**type**\:  :py:class:`AdjRibInPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Adjacency rib out\-bound post\-policy table
                        	**type**\:  :py:class:`AdjRibOutPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Adjacency rib out\-bound pre\-policy table
                        	**type**\:  :py:class:`AdjRibOutPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Adjacency rib in\-bound pre\-policy table
                        	**type**\:  :py:class:`AdjRibInPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor, self).__init__()

                            self.yang_name = "open-config-neighbor"
                            self.yang_parent_name = "open-config-neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['neighbor_address']
                            self._child_classes = OrderedDict([("adj-rib-in-post", ("adj_rib_in_post", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost)), ("adj-rib-out-post", ("adj_rib_out_post", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost)), ("adj-rib-out-pre", ("adj_rib_out_pre", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre)), ("adj-rib-in-pre", ("adj_rib_in_pre", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre))])
                            self._leafs = OrderedDict([
                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                            ])
                            self.neighbor_address = None

                            self.adj_rib_in_post = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"

                            self.adj_rib_out_post = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"

                            self.adj_rib_out_pre = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"

                            self.adj_rib_in_pre = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._segment_path = lambda: "open-config-neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv4-unicast/open-config-neighbors/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor, ['neighbor_address'], name, value)


                        class AdjRibInPost(_Entity_):
                            """
                            Adjacency rib in\-bound post\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-in-post"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPost(_Entity_):
                            """
                            Adjacency rib out\-bound post\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-out-post"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']


                        class AdjRibOutPre(_Entity_):
                            """
                            Adjacency rib out\-bound pre\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-out-pre"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']


                        class AdjRibInPre(_Entity_):
                            """
                            Adjacency rib in\-bound pre\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-in-pre"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast']['meta_info']


            class Ipv6Unicast(_Entity_):
                """
                IPv6 Unicast
                
                .. attribute:: loc_rib
                
                	Local rib route table
                	**type**\:  :py:class:`LocRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib>`
                
                	**config**\: False
                
                .. attribute:: open_config_neighbors
                
                	Neighbor list
                	**type**\:  :py:class:`OpenConfigNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-bgp-oc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast, self).__init__()

                    self.yang_name = "ipv6-unicast"
                    self.yang_parent_name = "afi-safi-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("loc-rib", ("loc_rib", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib)), ("open-config-neighbors", ("open_config_neighbors", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors))])
                    self._leafs = OrderedDict()

                    self.loc_rib = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib()
                    self.loc_rib.parent = self
                    self._children_name_map["loc_rib"] = "loc-rib"

                    self.open_config_neighbors = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors()
                    self.open_config_neighbors.parent = self
                    self._children_name_map["open_config_neighbors"] = "open-config-neighbors"
                    self._segment_path = lambda: "ipv6-unicast"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast, [], name, value)


                class LocRib(_Entity_):
                    """
                    Local rib route table
                    
                    .. attribute:: routes
                    
                    	routes table
                    	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes>`
                    
                    	**config**\: False
                    
                    .. attribute:: num_routes
                    
                    	Number of routes in adjacency rib out\-bound post\-policy table
                    	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib, self).__init__()

                        self.yang_name = "loc-rib"
                        self.yang_parent_name = "ipv6-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes))])
                        self._leafs = OrderedDict()

                        self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes()
                        self.routes.parent = self
                        self._children_name_map["routes"] = "routes"

                        self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes()
                        self.num_routes.parent = self
                        self._children_name_map["num_routes"] = "num-routes"
                        self._segment_path = lambda: "loc-rib"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib, [], name, value)


                    class Routes(_Entity_):
                        """
                        routes table
                        
                        .. attribute:: route
                        
                        	route entry
                        	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "routes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes, [], name, value)


                        class Route(_Entity_):
                            """
                            route entry
                            
                            .. attribute:: route
                            
                            	Network in prefix/length format
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**config**\: False
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: path_id
                            
                            	Path ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prefix_name
                            
                            	Prefix
                            	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName>`
                            
                            	**config**\: False
                            
                            .. attribute:: route_attr_list
                            
                            	RouteAttributesList
                            	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList>`
                            
                            	**config**\: False
                            
                            .. attribute:: ext_attributes_list
                            
                            	ExtAttributesList
                            	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList>`
                            
                            	**config**\: False
                            
                            .. attribute:: last_modified_date
                            
                            	LastModifiedDate
                            	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate>`
                            
                            	**config**\: False
                            
                            .. attribute:: last_update_recieved
                            
                            	LastUpdateRecieved
                            	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid_route
                            
                            	ValidRoute
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: invalid_reason
                            
                            	IndentityRef
                            	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                            
                            	**config**\: False
                            
                            .. attribute:: best_path
                            
                            	BestPath
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "routes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved))])
                                self._leafs = OrderedDict([
                                    ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                    ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                    ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                    ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                    ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                ])
                                self.route = None
                                self.neighbor_address = None
                                self.path_id = None
                                self.valid_route = None
                                self.invalid_reason = None
                                self.best_path = None

                                self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName()
                                self.prefix_name.parent = self
                                self._children_name_map["prefix_name"] = "prefix-name"

                                self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList()
                                self.route_attr_list.parent = self
                                self._children_name_map["route_attr_list"] = "route-attr-list"

                                self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList()
                                self.ext_attributes_list.parent = self
                                self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate()
                                self.last_modified_date.parent = self
                                self._children_name_map["last_modified_date"] = "last-modified-date"

                                self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved()
                                self.last_update_recieved.parent = self
                                self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                self._segment_path = lambda: "route"
                                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                            class PrefixName(_Entity_):
                                """
                                Prefix
                                
                                .. attribute:: prefix
                                
                                	Prefix
                                	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix>`
                                
                                	**config**\: False
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName, self).__init__()

                                    self.yang_name = "prefix-name"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix))])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                    ])
                                    self.prefix_length = None

                                    self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"
                                    self._segment_path = lambda: "prefix-name"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                class Prefix(_Entity_):
                                    """
                                    Prefix
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix, self).__init__()

                                        self.yang_name = "prefix"
                                        self.yang_parent_name = "prefix-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "prefix"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/prefix-name/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName']['meta_info']


                            class RouteAttrList(_Entity_):
                                """
                                RouteAttributesList
                                
                                .. attribute:: next_hop
                                
                                	NextHopAddress
                                	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop>`
                                
                                	**config**\: False
                                
                                .. attribute:: aggregrator_attributes
                                
                                	AggregatorList
                                	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                
                                	**config**\: False
                                
                                .. attribute:: origin_type
                                
                                	Origin Attribute Type
                                	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                
                                	**config**\: False
                                
                                .. attribute:: as_path
                                
                                	AS Path
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: as4_path
                                
                                	AS4 Path
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: med
                                
                                	Med
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: local_pref
                                
                                	LocalPref
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: atomic_aggr
                                
                                	AtomicAggr
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                .. attribute:: community
                                
                                	CommunityArray
                                	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList, self).__init__()

                                    self.yang_name = "route-attr-list"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community))])
                                    self._leafs = OrderedDict([
                                        ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                        ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                        ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                        ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                        ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                        ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                    ])
                                    self.origin_type = None
                                    self.as_path = None
                                    self.as4_path = None
                                    self.med = None
                                    self.local_pref = None
                                    self.atomic_aggr = None

                                    self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop()
                                    self.next_hop.parent = self
                                    self._children_name_map["next_hop"] = "next-hop"

                                    self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes()
                                    self.aggregrator_attributes.parent = self
                                    self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                    self.community = YList(self)
                                    self._segment_path = lambda: "route-attr-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                class NextHop(_Entity_):
                                    """
                                    NextHopAddress
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                        self.yang_name = "next-hop"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "next-hop"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                class AggregratorAttributes(_Entity_):
                                    """
                                    AggregatorList
                                    
                                    .. attribute:: as_
                                    
                                    	AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: as4
                                    
                                    	AS4 number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                        self.yang_name = "aggregrator-attributes"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                            ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ])
                                        self.as_ = None
                                        self.as4 = None
                                        self.address = None
                                        self._segment_path = lambda: "aggregrator-attributes"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                class Community(_Entity_):
                                    """
                                    CommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community, self).__init__()

                                        self.yang_name = "community"
                                        self.yang_parent_name = "route-attr-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                        ])
                                        self.objects = None
                                        self._segment_path = lambda: "community"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/route-attr-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']


                            class ExtAttributesList(_Entity_):
                                """
                                ExtAttributesList
                                
                                .. attribute:: originator_id
                                
                                	OriginatorID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: aigp
                                
                                	AIGP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: path_id
                                
                                	PathId
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: cluster
                                
                                	ClusterList
                                	**type**\: list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: ext_community
                                
                                	ExtendedCommunityArray
                                	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity>`
                                
                                	**config**\: False
                                
                                .. attribute:: unknown_attributes
                                
                                	UnknownAttributes
                                	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList, self).__init__()

                                    self.yang_name = "ext-attributes-list"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                    self._leafs = OrderedDict([
                                        ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                        ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                        ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                        ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                    ])
                                    self.originator_id = None
                                    self.aigp = None
                                    self.path_id = None
                                    self.cluster = []

                                    self.ext_community = YList(self)
                                    self.unknown_attributes = YList(self)
                                    self._segment_path = lambda: "ext-attributes-list"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                class ExtCommunity(_Entity_):
                                    """
                                    ExtendedCommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                        self.yang_name = "ext-community"
                                        self.yang_parent_name = "ext-attributes-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                        ])
                                        self.objects = None
                                        self._segment_path = lambda: "ext-community"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/ext-attributes-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                class UnknownAttributes(_Entity_):
                                    """
                                    UnknownAttributes
                                    
                                    .. attribute:: attribute_type
                                    
                                    	AttributeType
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: attribute_length
                                    
                                    	AttributeLength
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: attribute_value
                                    
                                    	Atributevalue
                                    	**type**\: str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                        self.yang_name = "unknown-attributes"
                                        self.yang_parent_name = "ext-attributes-list"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = False
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                            ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                            ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                        ])
                                        self.attribute_type = None
                                        self.attribute_length = None
                                        self.attribute_value = None
                                        self._segment_path = lambda: "unknown-attributes"
                                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/ext-attributes-list/%s" % self._segment_path()
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']


                            class LastModifiedDate(_Entity_):
                                """
                                LastModifiedDate
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate, self).__init__()

                                    self.yang_name = "last-modified-date"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                    ])
                                    self.time_value = None
                                    self._segment_path = lambda: "last-modified-date"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info']


                            class LastUpdateRecieved(_Entity_):
                                """
                                LastUpdateRecieved
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\: str
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved, self).__init__()

                                    self.yang_name = "last-update-recieved"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                    ])
                                    self.time_value = None
                                    self._segment_path = lambda: "last-update-recieved"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/routes/route/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes']['meta_info']


                    class NumRoutes(_Entity_):
                        """
                        Number of routes in adjacency rib out\-bound
                        post\-policy table
                        
                        .. attribute:: num_routes
                        
                        	NumRoutes
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes, self).__init__()

                            self.yang_name = "num-routes"
                            self.yang_parent_name = "loc-rib"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                            ])
                            self.num_routes = None
                            self._segment_path = lambda: "num-routes"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/loc-rib/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes, ['num_routes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib']['meta_info']


                class OpenConfigNeighbors(_Entity_):
                    """
                    Neighbor list
                    
                    .. attribute:: open_config_neighbor
                    
                    	Neighbor name
                    	**type**\: list of  		 :py:class:`OpenConfigNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors, self).__init__()

                        self.yang_name = "open-config-neighbors"
                        self.yang_parent_name = "ipv6-unicast"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("open-config-neighbor", ("open_config_neighbor", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor))])
                        self._leafs = OrderedDict()

                        self.open_config_neighbor = YList(self)
                        self._segment_path = lambda: "open-config-neighbors"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors, [], name, value)


                    class OpenConfigNeighbor(_Entity_):
                        """
                        Neighbor name
                        
                        .. attribute:: neighbor_address  (key)
                        
                        	Neighbor Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_in_post
                        
                        	Adjacency rib in\-bound post\-policy table
                        	**type**\:  :py:class:`AdjRibInPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Adjacency rib out\-bound post\-policy table
                        	**type**\:  :py:class:`AdjRibOutPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Adjacency rib out\-bound pre\-policy table
                        	**type**\:  :py:class:`AdjRibOutPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre>`
                        
                        	**config**\: False
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Adjacency rib in\-bound pre\-policy table
                        	**type**\:  :py:class:`AdjRibInPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor, self).__init__()

                            self.yang_name = "open-config-neighbor"
                            self.yang_parent_name = "open-config-neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['neighbor_address']
                            self._child_classes = OrderedDict([("adj-rib-in-post", ("adj_rib_in_post", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost)), ("adj-rib-out-post", ("adj_rib_out_post", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost)), ("adj-rib-out-pre", ("adj_rib_out_pre", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre)), ("adj-rib-in-pre", ("adj_rib_in_pre", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre))])
                            self._leafs = OrderedDict([
                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                            ])
                            self.neighbor_address = None

                            self.adj_rib_in_post = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self._children_name_map["adj_rib_in_post"] = "adj-rib-in-post"

                            self.adj_rib_out_post = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self._children_name_map["adj_rib_out_post"] = "adj-rib-out-post"

                            self.adj_rib_out_pre = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self
                            self._children_name_map["adj_rib_out_pre"] = "adj-rib-out-pre"

                            self.adj_rib_in_pre = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self._children_name_map["adj_rib_in_pre"] = "adj-rib-in-pre"
                            self._segment_path = lambda: "open-config-neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/bgp-rib/afi-safi-table/ipv6-unicast/open-config-neighbors/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor, ['neighbor_address'], name, value)


                        class AdjRibInPost(_Entity_):
                            """
                            Adjacency rib in\-bound post\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost, self).__init__()

                                self.yang_name = "adj-rib-in-post"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-in-post"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-in-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPost(_Entity_):
                            """
                            Adjacency rib out\-bound post\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost, self).__init__()

                                self.yang_name = "adj-rib-out-post"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-out-post"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-out-post"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']


                        class AdjRibOutPre(_Entity_):
                            """
                            Adjacency rib out\-bound pre\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre, self).__init__()

                                self.yang_name = "adj-rib-out-pre"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-out-pre"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-out-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']


                        class AdjRibInPre(_Entity_):
                            """
                            Adjacency rib in\-bound pre\-policy table
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes>`
                            
                            	**config**\: False
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:  :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre, self).__init__()

                                self.yang_name = "adj-rib-in-pre"
                                self.yang_parent_name = "open-config-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("routes", ("routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes)), ("num-routes", ("num_routes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes))])
                                self._leafs = OrderedDict()

                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes()
                                self.routes.parent = self
                                self._children_name_map["routes"] = "routes"

                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes()
                                self.num_routes.parent = self
                                self._children_name_map["num_routes"] = "num-routes"
                                self._segment_path = lambda: "adj-rib-in-pre"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre, [], name, value)


                            class Routes(_Entity_):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of  		 :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes, self).__init__()

                                    self.yang_name = "routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("route", ("route", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route))])
                                    self._leafs = OrderedDict()

                                    self.route = YList(self)
                                    self._segment_path = lambda: "routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes, [], name, value)


                                class Route(_Entity_):
                                    """
                                    route entry
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:  :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:  :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:  :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:  :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:  :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:  :py:class:`BgpOcInvalidRouteReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReason>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route, self).__init__()

                                        self.yang_name = "route"
                                        self.yang_parent_name = "routes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("prefix-name", ("prefix_name", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName)), ("route-attr-list", ("route_attr_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList)), ("ext-attributes-list", ("ext_attributes_list", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList)), ("last-modified-date", ("last_modified_date", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate)), ("last-update-recieved", ("last_update_recieved", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved))])
                                        self._leafs = OrderedDict([
                                            ('route', (YLeaf(YType.str, 'route'), ['str','str'])),
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('valid_route', (YLeaf(YType.boolean, 'valid-route'), ['bool'])),
                                            ('invalid_reason', (YLeaf(YType.enumeration, 'invalid-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReason', '')])),
                                            ('best_path', (YLeaf(YType.boolean, 'best-path'), ['bool'])),
                                        ])
                                        self.route = None
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.valid_route = None
                                        self.invalid_reason = None
                                        self.best_path = None

                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self._children_name_map["prefix_name"] = "prefix-name"

                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self._children_name_map["route_attr_list"] = "route-attr-list"

                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self._children_name_map["ext_attributes_list"] = "ext-attributes-list"

                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self._children_name_map["last_modified_date"] = "last-modified-date"

                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self._children_name_map["last_update_recieved"] = "last-update-recieved"
                                        self._segment_path = lambda: "route"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route, ['route', 'neighbor_address', 'path_id', 'valid_route', 'invalid_reason', 'best_path'], name, value)


                                    class PrefixName(_Entity_):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName, self).__init__()

                                            self.yang_name = "prefix-name"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("prefix", ("prefix", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix))])
                                            self._leafs = OrderedDict([
                                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                            ])
                                            self.prefix_length = None

                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self._children_name_map["prefix"] = "prefix"
                                            self._segment_path = lambda: "prefix-name"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName, ['prefix_length'], name, value)


                                        class Prefix(_Entity_):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix, self).__init__()

                                                self.yang_name = "prefix"
                                                self.yang_parent_name = "prefix-name"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(_Entity_):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:  :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:  :py:class:`BgpOcOriginAttr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttr>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of  		 :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList, self).__init__()

                                            self.yang_name = "route-attr-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("next-hop", ("next_hop", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop)), ("aggregrator-attributes", ("aggregrator_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes)), ("community", ("community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community))])
                                            self._leafs = OrderedDict([
                                                ('origin_type', (YLeaf(YType.enumeration, 'origin-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttr', '')])),
                                                ('as_path', (YLeaf(YType.str, 'as-path'), ['str'])),
                                                ('as4_path', (YLeaf(YType.str, 'as4-path'), ['str'])),
                                                ('med', (YLeaf(YType.uint32, 'med'), ['int'])),
                                                ('local_pref', (YLeaf(YType.uint32, 'local-pref'), ['int'])),
                                                ('atomic_aggr', (YLeaf(YType.boolean, 'atomic-aggr'), ['bool'])),
                                            ])
                                            self.origin_type = None
                                            self.as_path = None
                                            self.as4_path = None
                                            self.med = None
                                            self.local_pref = None
                                            self.atomic_aggr = None

                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self._children_name_map["next_hop"] = "next-hop"

                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self._children_name_map["aggregrator_attributes"] = "aggregrator-attributes"

                                            self.community = YList(self)
                                            self._segment_path = lambda: "route-attr-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList, ['origin_type', 'as_path', 'as4_path', 'med', 'local_pref', 'atomic_aggr'], name, value)


                                        class NextHop(_Entity_):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:  :py:class:`BgpOcAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfi>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop, self).__init__()

                                                self.yang_name = "next-hop"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfi', '')])),
                                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                ])
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "next-hop"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop, ['afi', 'ipv4_address', 'ipv6_address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(_Entity_):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes, self).__init__()

                                                self.yang_name = "aggregrator-attributes"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('as_', (YLeaf(YType.uint32, 'as'), ['int'])),
                                                    ('as4', (YLeaf(YType.uint32, 'as4'), ['int'])),
                                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ])
                                                self.as_ = None
                                                self.as4 = None
                                                self.address = None
                                                self._segment_path = lambda: "aggregrator-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes, ['as_', 'as4', 'address'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(_Entity_):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community, self).__init__()

                                                self.yang_name = "community"
                                                self.yang_parent_name = "route-attr-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(_Entity_):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of  		 :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of  		 :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList, self).__init__()

                                            self.yang_name = "ext-attributes-list"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("ext-community", ("ext_community", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity)), ("unknown-attributes", ("unknown_attributes", OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes))])
                                            self._leafs = OrderedDict([
                                                ('originator_id', (YLeaf(YType.str, 'originator-id'), ['str'])),
                                                ('aigp', (YLeaf(YType.uint64, 'aigp'), ['int'])),
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('cluster', (YLeafList(YType.str, 'cluster'), ['str'])),
                                            ])
                                            self.originator_id = None
                                            self.aigp = None
                                            self.path_id = None
                                            self.cluster = []

                                            self.ext_community = YList(self)
                                            self.unknown_attributes = YList(self)
                                            self._segment_path = lambda: "ext-attributes-list"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList, ['originator_id', 'aigp', 'path_id', 'cluster'], name, value)


                                        class ExtCommunity(_Entity_):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\: str
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity, self).__init__()

                                                self.yang_name = "ext-community"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('objects', (YLeaf(YType.str, 'objects'), ['str'])),
                                                ])
                                                self.objects = None
                                                self._segment_path = lambda: "ext-community"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity, ['objects'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(_Entity_):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\: str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2017-09-07'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes, self).__init__()

                                                self.yang_name = "unknown-attributes"
                                                self.yang_parent_name = "ext-attributes-list"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('attribute_type', (YLeaf(YType.uint16, 'attribute-type'), ['int'])),
                                                    ('attribute_length', (YLeaf(YType.uint16, 'attribute-length'), ['int'])),
                                                    ('attribute_value', (YLeaf(YType.str, 'attribute-value'), ['str'])),
                                                ])
                                                self.attribute_type = None
                                                self.attribute_length = None
                                                self.attribute_value = None
                                                self._segment_path = lambda: "unknown-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes, ['attribute_type', 'attribute_length', 'attribute_value'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(_Entity_):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate, self).__init__()

                                            self.yang_name = "last-modified-date"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-modified-date"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(_Entity_):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\: str
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved, self).__init__()

                                            self.yang_name = "last-update-recieved"
                                            self.yang_parent_name = "route"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_value', (YLeaf(YType.str, 'time-value'), ['str'])),
                                            ])
                                            self.time_value = None
                                            self._segment_path = lambda: "last-update-recieved"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved, ['time_value'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']


                            class NumRoutes(_Entity_):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes, self).__init__()

                                    self.yang_name = "num-routes"
                                    self.yang_parent_name = "adj-rib-in-pre"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_routes', (YLeaf(YType.uint64, 'num-routes'), ['int'])),
                                    ])
                                    self.num_routes = None
                                    self._segment_path = lambda: "num-routes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes, ['num_routes'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
            return meta._meta_table['OcBgp.BgpRib']['meta_info']

    def clone_ptr(self):
        self._top_entity = OcBgp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['OcBgp']['meta_info']


