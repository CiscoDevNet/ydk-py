""" Cisco_IOS_XR_ipv4_bgp_oc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-bgp\-oc package operational data.

This module contains definitions
for the following management objects\:
  oc\-bgp\: OC\-BGP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpOcAfiEnum(Enum):
    """
    BgpOcAfiEnum

    BGP Address family

    .. data:: ipv4 = 0

    	IPv4 unicast

    .. data:: ipv6 = 5

    	IPv6 unicast

    """

    ipv4 = 0

    ipv6 = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcAfiEnum']


class BgpOcInvalidRouteReasonEnum(Enum):
    """
    BgpOcInvalidRouteReasonEnum

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

    valid_route = 1

    invalid_clsuter_loop = 2

    invalid_as_path_loop = 3

    invalid_origin_at_or_id = 4

    invalid_as_confed_loop = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcInvalidRouteReasonEnum']


class BgpOcOriginAttrEnum(Enum):
    """
    BgpOcOriginAttrEnum

    Origin Type

    .. data:: igp = 0

    	IGP

    .. data:: egp = 1

    	EGP

    .. data:: incomplete = 2

    	Incomplete

    """

    igp = 0

    egp = 1

    incomplete = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['BgpOcOriginAttrEnum']



class OcBgp(object):
    """
    OC\-BGP operational data
    
    .. attribute:: bgp_rib
    
    	BGP\-RIB operational data
    	**type**\:   :py:class:`BgpRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib>`
    
    

    """

    _prefix = 'ipv4-bgp-oc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.bgp_rib = OcBgp.BgpRib()
        self.bgp_rib.parent = self


    class BgpRib(object):
        """
        BGP\-RIB operational data
        
        .. attribute:: afi_safi_table
        
        	AFI\-SAFIs information
        	**type**\:   :py:class:`AfiSafiTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable>`
        
        

        """

        _prefix = 'ipv4-bgp-oc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.afi_safi_table = OcBgp.BgpRib.AfiSafiTable()
            self.afi_safi_table.parent = self


        class AfiSafiTable(object):
            """
            AFI\-SAFIs information
            
            .. attribute:: ipv4_unicast
            
            	IPv4 Unicast
            	**type**\:   :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast>`
            
            .. attribute:: ipv6_unicast
            
            	IPv6 Unicast
            	**type**\:   :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast>`
            
            

            """

            _prefix = 'ipv4-bgp-oc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv4_unicast = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast()
                self.ipv4_unicast.parent = self
                self.ipv6_unicast = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast()
                self.ipv6_unicast.parent = self


            class Ipv4Unicast(object):
                """
                IPv4 Unicast
                
                .. attribute:: loc_rib
                
                	Local rib route table
                	**type**\:   :py:class:`LocRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib>`
                
                .. attribute:: open_config_neighbors
                
                	Neighbor list
                	**type**\:   :py:class:`OpenConfigNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors>`
                
                

                """

                _prefix = 'ipv4-bgp-oc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.loc_rib = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib()
                    self.loc_rib.parent = self
                    self.open_config_neighbors = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors()
                    self.open_config_neighbors.parent = self


                class LocRib(object):
                    """
                    Local rib route table
                    
                    .. attribute:: num_routes
                    
                    	Number of routes in adjacency rib out\-bound post\-policy table
                    	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes>`
                    
                    .. attribute:: routes
                    
                    	routes table
                    	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes()
                        self.num_routes.parent = self
                        self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes()
                        self.routes.parent = self


                    class Routes(object):
                        """
                        routes table
                        
                        .. attribute:: route
                        
                        	route entry
                        	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
                            """
                            route entry
                            
                            .. attribute:: best_path
                            
                            	BestPath
                            	**type**\:  bool
                            
                            .. attribute:: ext_attributes_list
                            
                            	ExtAttributesList
                            	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList>`
                            
                            .. attribute:: invalid_reason
                            
                            	IndentityRef
                            	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                            
                            .. attribute:: last_modified_date
                            
                            	LastModifiedDate
                            	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate>`
                            
                            .. attribute:: last_update_recieved
                            
                            	LastUpdateRecieved
                            	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: path_id
                            
                            	Path ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: prefix_name
                            
                            	Prefix
                            	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName>`
                            
                            .. attribute:: route
                            
                            	Network in prefix/length format
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            
                            ----
                            .. attribute:: route_attr_list
                            
                            	RouteAttributesList
                            	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList>`
                            
                            .. attribute:: valid_route
                            
                            	ValidRoute
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.best_path = None
                                self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList()
                                self.ext_attributes_list.parent = self
                                self.invalid_reason = None
                                self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate()
                                self.last_modified_date.parent = self
                                self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved()
                                self.last_update_recieved.parent = self
                                self.neighbor_address = None
                                self.path_id = None
                                self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName()
                                self.prefix_name.parent = self
                                self.route = None
                                self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList()
                                self.route_attr_list.parent = self
                                self.valid_route = None


                            class PrefixName(object):
                                """
                                Prefix
                                
                                .. attribute:: prefix
                                
                                	Prefix
                                	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix>`
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix()
                                    self.prefix.parent = self
                                    self.prefix_length = None


                                class Prefix(object):
                                    """
                                    Prefix
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.afi is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.prefix is not None and self.prefix._has_data():
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName']['meta_info']


                            class RouteAttrList(object):
                                """
                                RouteAttributesList
                                
                                .. attribute:: aggregrator_attributes
                                
                                	AggregatorList
                                	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                
                                .. attribute:: as4_path
                                
                                	AS4 Path
                                	**type**\:  str
                                
                                .. attribute:: as_path
                                
                                	AS Path
                                	**type**\:  str
                                
                                .. attribute:: atomic_aggr
                                
                                	AtomicAggr
                                	**type**\:  bool
                                
                                .. attribute:: community
                                
                                	CommunityArray
                                	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community>`
                                
                                .. attribute:: local_pref
                                
                                	LocalPref
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med
                                
                                	Med
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop
                                
                                	NextHopAddress
                                	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop>`
                                
                                .. attribute:: origin_type
                                
                                	Origin Attribute Type
                                	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes()
                                    self.aggregrator_attributes.parent = self
                                    self.as4_path = None
                                    self.as_path = None
                                    self.atomic_aggr = None
                                    self.community = YList()
                                    self.community.parent = self
                                    self.community.name = 'community'
                                    self.local_pref = None
                                    self.med = None
                                    self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop()
                                    self.next_hop.parent = self
                                    self.origin_type = None


                                class NextHop(object):
                                    """
                                    NextHopAddress
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.afi is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                class AggregratorAttributes(object):
                                    """
                                    AggregatorList
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: as4
                                    
                                    	AS4 number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.as4 = None
                                        self.as_ = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                class Community(object):
                                    """
                                    CommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.objects = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.objects is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                        return True

                                    if self.as4_path is not None:
                                        return True

                                    if self.as_path is not None:
                                        return True

                                    if self.atomic_aggr is not None:
                                        return True

                                    if self.community is not None:
                                        for child_ref in self.community:
                                            if child_ref._has_data():
                                                return True

                                    if self.local_pref is not None:
                                        return True

                                    if self.med is not None:
                                        return True

                                    if self.next_hop is not None and self.next_hop._has_data():
                                        return True

                                    if self.origin_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']


                            class ExtAttributesList(object):
                                """
                                ExtAttributesList
                                
                                .. attribute:: aigp
                                
                                	AIGP
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: cluster
                                
                                	ClusterList
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	ExtendedCommunityArray
                                	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity>`
                                
                                .. attribute:: originator_id
                                
                                	OriginatorID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: path_id
                                
                                	PathId
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attributes
                                
                                	UnknownAttributes
                                	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aigp = None
                                    self.cluster = YLeafList()
                                    self.cluster.parent = self
                                    self.cluster.name = 'cluster'
                                    self.ext_community = YList()
                                    self.ext_community.parent = self
                                    self.ext_community.name = 'ext_community'
                                    self.originator_id = None
                                    self.path_id = None
                                    self.unknown_attributes = YList()
                                    self.unknown_attributes.parent = self
                                    self.unknown_attributes.name = 'unknown_attributes'


                                class ExtCommunity(object):
                                    """
                                    ExtendedCommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.objects = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.objects is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                class UnknownAttributes(object):
                                    """
                                    UnknownAttributes
                                    
                                    .. attribute:: attribute_length
                                    
                                    	AttributeLength
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attribute_type
                                    
                                    	AttributeType
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attribute_value
                                    
                                    	Atributevalue
                                    	**type**\:  str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.attribute_length = None
                                        self.attribute_type = None
                                        self.attribute_value = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attribute_length is not None:
                                            return True

                                        if self.attribute_type is not None:
                                            return True

                                        if self.attribute_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aigp is not None:
                                        return True

                                    if self.cluster is not None:
                                        for child in self.cluster:
                                            if child is not None:
                                                return True

                                    if self.ext_community is not None:
                                        for child_ref in self.ext_community:
                                            if child_ref._has_data():
                                                return True

                                    if self.originator_id is not None:
                                        return True

                                    if self.path_id is not None:
                                        return True

                                    if self.unknown_attributes is not None:
                                        for child_ref in self.unknown_attributes:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']


                            class LastModifiedDate(object):
                                """
                                LastModifiedDate
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.time_value = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info']


                            class LastUpdateRecieved(object):
                                """
                                LastUpdateRecieved
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.time_value = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.best_path is not None:
                                    return True

                                if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                    return True

                                if self.invalid_reason is not None:
                                    return True

                                if self.last_modified_date is not None and self.last_modified_date._has_data():
                                    return True

                                if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.path_id is not None:
                                    return True

                                if self.prefix_name is not None and self.prefix_name._has_data():
                                    return True

                                if self.route is not None:
                                    return True

                                if self.route_attr_list is not None and self.route_attr_list._has_data():
                                    return True

                                if self.valid_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes']['meta_info']


                    class NumRoutes(object):
                        """
                        Number of routes in adjacency rib out\-bound
                        post\-policy table
                        
                        .. attribute:: num_routes
                        
                        	NumRoutes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.num_routes = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.num_routes is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.num_routes is not None and self.num_routes._has_data():
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib']['meta_info']


                class OpenConfigNeighbors(object):
                    """
                    Neighbor list
                    
                    .. attribute:: open_config_neighbor
                    
                    	Neighbor name
                    	**type**\: list of    :py:class:`OpenConfigNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.open_config_neighbor = YList()
                        self.open_config_neighbor.parent = self
                        self.open_config_neighbor.name = 'open_config_neighbor'


                    class OpenConfigNeighbor(object):
                        """
                        Neighbor name
                        
                        .. attribute:: neighbor_address  <key>
                        
                        	Neighbor Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: adj_rib_in_post
                        
                        	Adjacency rib in\-bound post\-policy table
                        	**type**\:   :py:class:`AdjRibInPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Adjacency rib in\-bound pre\-policy table
                        	**type**\:   :py:class:`AdjRibInPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Adjacency rib out\-bound post\-policy table
                        	**type**\:   :py:class:`AdjRibOutPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Adjacency rib out\-bound pre\-policy table
                        	**type**\:   :py:class:`AdjRibOutPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None
                            self.adj_rib_in_post = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self.adj_rib_in_pre = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self.adj_rib_out_post = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self.adj_rib_out_pre = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self


                        class AdjRibInPost(object):
                            """
                            Adjacency rib in\-bound post\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-in-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPost(object):
                            """
                            Adjacency rib out\-bound post\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-out-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']


                        class AdjRibOutPre(object):
                            """
                            Adjacency rib out\-bound pre\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-out-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']


                        class AdjRibInPre(object):
                            """
                            Adjacency rib in\-bound pre\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-in-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']

                        @property
                        def _common_path(self):
                            if self.neighbor_address is None:
                                raise YPYModelError('Key property neighbor_address is None')

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbors/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbor[Cisco-IOS-XR-ipv4-bgp-oc-oper:neighbor-address = ' + str(self.neighbor_address) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.open_config_neighbor is not None:
                            for child_ref in self.open_config_neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv4-unicast'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.loc_rib is not None and self.loc_rib._has_data():
                        return True

                    if self.open_config_neighbors is not None and self.open_config_neighbors._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast']['meta_info']


            class Ipv6Unicast(object):
                """
                IPv6 Unicast
                
                .. attribute:: loc_rib
                
                	Local rib route table
                	**type**\:   :py:class:`LocRib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib>`
                
                .. attribute:: open_config_neighbors
                
                	Neighbor list
                	**type**\:   :py:class:`OpenConfigNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors>`
                
                

                """

                _prefix = 'ipv4-bgp-oc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.loc_rib = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib()
                    self.loc_rib.parent = self
                    self.open_config_neighbors = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors()
                    self.open_config_neighbors.parent = self


                class LocRib(object):
                    """
                    Local rib route table
                    
                    .. attribute:: num_routes
                    
                    	Number of routes in adjacency rib out\-bound post\-policy table
                    	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes>`
                    
                    .. attribute:: routes
                    
                    	routes table
                    	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes()
                        self.num_routes.parent = self
                        self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes()
                        self.routes.parent = self


                    class Routes(object):
                        """
                        routes table
                        
                        .. attribute:: route
                        
                        	route entry
                        	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
                            """
                            route entry
                            
                            .. attribute:: best_path
                            
                            	BestPath
                            	**type**\:  bool
                            
                            .. attribute:: ext_attributes_list
                            
                            	ExtAttributesList
                            	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList>`
                            
                            .. attribute:: invalid_reason
                            
                            	IndentityRef
                            	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                            
                            .. attribute:: last_modified_date
                            
                            	LastModifiedDate
                            	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate>`
                            
                            .. attribute:: last_update_recieved
                            
                            	LastUpdateRecieved
                            	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved>`
                            
                            .. attribute:: neighbor_address
                            
                            	Neighbor address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: path_id
                            
                            	Path ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: prefix_name
                            
                            	Prefix
                            	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName>`
                            
                            .. attribute:: route
                            
                            	Network in prefix/length format
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            
                            ----
                            .. attribute:: route_attr_list
                            
                            	RouteAttributesList
                            	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList>`
                            
                            .. attribute:: valid_route
                            
                            	ValidRoute
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.best_path = None
                                self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList()
                                self.ext_attributes_list.parent = self
                                self.invalid_reason = None
                                self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate()
                                self.last_modified_date.parent = self
                                self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved()
                                self.last_update_recieved.parent = self
                                self.neighbor_address = None
                                self.path_id = None
                                self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName()
                                self.prefix_name.parent = self
                                self.route = None
                                self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList()
                                self.route_attr_list.parent = self
                                self.valid_route = None


                            class PrefixName(object):
                                """
                                Prefix
                                
                                .. attribute:: prefix
                                
                                	Prefix
                                	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix>`
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix()
                                    self.prefix.parent = self
                                    self.prefix_length = None


                                class Prefix(object):
                                    """
                                    Prefix
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.afi is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.prefix is not None and self.prefix._has_data():
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName']['meta_info']


                            class RouteAttrList(object):
                                """
                                RouteAttributesList
                                
                                .. attribute:: aggregrator_attributes
                                
                                	AggregatorList
                                	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                
                                .. attribute:: as4_path
                                
                                	AS4 Path
                                	**type**\:  str
                                
                                .. attribute:: as_path
                                
                                	AS Path
                                	**type**\:  str
                                
                                .. attribute:: atomic_aggr
                                
                                	AtomicAggr
                                	**type**\:  bool
                                
                                .. attribute:: community
                                
                                	CommunityArray
                                	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community>`
                                
                                .. attribute:: local_pref
                                
                                	LocalPref
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med
                                
                                	Med
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop
                                
                                	NextHopAddress
                                	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop>`
                                
                                .. attribute:: origin_type
                                
                                	Origin Attribute Type
                                	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes()
                                    self.aggregrator_attributes.parent = self
                                    self.as4_path = None
                                    self.as_path = None
                                    self.atomic_aggr = None
                                    self.community = YList()
                                    self.community.parent = self
                                    self.community.name = 'community'
                                    self.local_pref = None
                                    self.med = None
                                    self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop()
                                    self.next_hop.parent = self
                                    self.origin_type = None


                                class NextHop(object):
                                    """
                                    NextHopAddress
                                    
                                    .. attribute:: afi
                                    
                                    	AFI
                                    	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 Addr
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.afi = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.afi is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                class AggregratorAttributes(object):
                                    """
                                    AggregatorList
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: as4
                                    
                                    	AS4 number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.as4 = None
                                        self.as_ = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                class Community(object):
                                    """
                                    CommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.objects = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.objects is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                        return True

                                    if self.as4_path is not None:
                                        return True

                                    if self.as_path is not None:
                                        return True

                                    if self.atomic_aggr is not None:
                                        return True

                                    if self.community is not None:
                                        for child_ref in self.community:
                                            if child_ref._has_data():
                                                return True

                                    if self.local_pref is not None:
                                        return True

                                    if self.med is not None:
                                        return True

                                    if self.next_hop is not None and self.next_hop._has_data():
                                        return True

                                    if self.origin_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']


                            class ExtAttributesList(object):
                                """
                                ExtAttributesList
                                
                                .. attribute:: aigp
                                
                                	AIGP
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: cluster
                                
                                	ClusterList
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ext_community
                                
                                	ExtendedCommunityArray
                                	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity>`
                                
                                .. attribute:: originator_id
                                
                                	OriginatorID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: path_id
                                
                                	PathId
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: unknown_attributes
                                
                                	UnknownAttributes
                                	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aigp = None
                                    self.cluster = YLeafList()
                                    self.cluster.parent = self
                                    self.cluster.name = 'cluster'
                                    self.ext_community = YList()
                                    self.ext_community.parent = self
                                    self.ext_community.name = 'ext_community'
                                    self.originator_id = None
                                    self.path_id = None
                                    self.unknown_attributes = YList()
                                    self.unknown_attributes.parent = self
                                    self.unknown_attributes.name = 'unknown_attributes'


                                class ExtCommunity(object):
                                    """
                                    ExtendedCommunityArray
                                    
                                    .. attribute:: objects
                                    
                                    	BGP OC objects
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.objects = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.objects is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                class UnknownAttributes(object):
                                    """
                                    UnknownAttributes
                                    
                                    .. attribute:: attribute_length
                                    
                                    	AttributeLength
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attribute_type
                                    
                                    	AttributeType
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: attribute_value
                                    
                                    	Atributevalue
                                    	**type**\:  str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.attribute_length = None
                                        self.attribute_type = None
                                        self.attribute_value = None

                                    @property
                                    def _common_path(self):

                                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.attribute_length is not None:
                                            return True

                                        if self.attribute_type is not None:
                                            return True

                                        if self.attribute_value is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.aigp is not None:
                                        return True

                                    if self.cluster is not None:
                                        for child in self.cluster:
                                            if child is not None:
                                                return True

                                    if self.ext_community is not None:
                                        for child_ref in self.ext_community:
                                            if child_ref._has_data():
                                                return True

                                    if self.originator_id is not None:
                                        return True

                                    if self.path_id is not None:
                                        return True

                                    if self.unknown_attributes is not None:
                                        for child_ref in self.unknown_attributes:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']


                            class LastModifiedDate(object):
                                """
                                LastModifiedDate
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.time_value = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info']


                            class LastUpdateRecieved(object):
                                """
                                LastUpdateRecieved
                                
                                .. attribute:: time_value
                                
                                	TimeValue
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.time_value = None

                                @property
                                def _common_path(self):

                                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info']

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.best_path is not None:
                                    return True

                                if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                    return True

                                if self.invalid_reason is not None:
                                    return True

                                if self.last_modified_date is not None and self.last_modified_date._has_data():
                                    return True

                                if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                    return True

                                if self.neighbor_address is not None:
                                    return True

                                if self.path_id is not None:
                                    return True

                                if self.prefix_name is not None and self.prefix_name._has_data():
                                    return True

                                if self.route is not None:
                                    return True

                                if self.route_attr_list is not None and self.route_attr_list._has_data():
                                    return True

                                if self.valid_route is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes']['meta_info']


                    class NumRoutes(object):
                        """
                        Number of routes in adjacency rib out\-bound
                        post\-policy table
                        
                        .. attribute:: num_routes
                        
                        	NumRoutes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.num_routes = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.num_routes is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:loc-rib'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.num_routes is not None and self.num_routes._has_data():
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib']['meta_info']


                class OpenConfigNeighbors(object):
                    """
                    Neighbor list
                    
                    .. attribute:: open_config_neighbor
                    
                    	Neighbor name
                    	**type**\: list of    :py:class:`OpenConfigNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor>`
                    
                    

                    """

                    _prefix = 'ipv4-bgp-oc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.open_config_neighbor = YList()
                        self.open_config_neighbor.parent = self
                        self.open_config_neighbor.name = 'open_config_neighbor'


                    class OpenConfigNeighbor(object):
                        """
                        Neighbor name
                        
                        .. attribute:: neighbor_address  <key>
                        
                        	Neighbor Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: adj_rib_in_post
                        
                        	Adjacency rib in\-bound post\-policy table
                        	**type**\:   :py:class:`AdjRibInPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost>`
                        
                        .. attribute:: adj_rib_in_pre
                        
                        	Adjacency rib in\-bound pre\-policy table
                        	**type**\:   :py:class:`AdjRibInPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre>`
                        
                        .. attribute:: adj_rib_out_post
                        
                        	Adjacency rib out\-bound post\-policy table
                        	**type**\:   :py:class:`AdjRibOutPost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost>`
                        
                        .. attribute:: adj_rib_out_pre
                        
                        	Adjacency rib out\-bound pre\-policy table
                        	**type**\:   :py:class:`AdjRibOutPre <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-oc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.neighbor_address = None
                            self.adj_rib_in_post = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost()
                            self.adj_rib_in_post.parent = self
                            self.adj_rib_in_pre = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre()
                            self.adj_rib_in_pre.parent = self
                            self.adj_rib_out_post = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost()
                            self.adj_rib_out_post.parent = self
                            self.adj_rib_out_pre = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre()
                            self.adj_rib_out_pre.parent = self


                        class AdjRibInPost(object):
                            """
                            Adjacency rib in\-bound post\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-in-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']


                        class AdjRibOutPost(object):
                            """
                            Adjacency rib out\-bound post\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-out-post'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']


                        class AdjRibOutPre(object):
                            """
                            Adjacency rib out\-bound pre\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-out-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']


                        class AdjRibInPre(object):
                            """
                            Adjacency rib in\-bound pre\-policy table
                            
                            .. attribute:: num_routes
                            
                            	Number of routes in adjacency rib out\-bound post\-policy table
                            	**type**\:   :py:class:`NumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes>`
                            
                            .. attribute:: routes
                            
                            	routes table
                            	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-oc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.num_routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes()
                                self.num_routes.parent = self
                                self.routes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes()
                                self.routes.parent = self


                            class Routes(object):
                                """
                                routes table
                                
                                .. attribute:: route
                                
                                	route entry
                                	**type**\: list of    :py:class:`Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.route = YList()
                                    self.route.parent = self
                                    self.route.name = 'route'


                                class Route(object):
                                    """
                                    route entry
                                    
                                    .. attribute:: best_path
                                    
                                    	BestPath
                                    	**type**\:  bool
                                    
                                    .. attribute:: ext_attributes_list
                                    
                                    	ExtAttributesList
                                    	**type**\:   :py:class:`ExtAttributesList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList>`
                                    
                                    .. attribute:: invalid_reason
                                    
                                    	IndentityRef
                                    	**type**\:   :py:class:`BgpOcInvalidRouteReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcInvalidRouteReasonEnum>`
                                    
                                    .. attribute:: last_modified_date
                                    
                                    	LastModifiedDate
                                    	**type**\:   :py:class:`LastModifiedDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate>`
                                    
                                    .. attribute:: last_update_recieved
                                    
                                    	LastUpdateRecieved
                                    	**type**\:   :py:class:`LastUpdateRecieved <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved>`
                                    
                                    .. attribute:: neighbor_address
                                    
                                    	Neighbor address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: path_id
                                    
                                    	Path ID
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: prefix_name
                                    
                                    	Prefix
                                    	**type**\:   :py:class:`PrefixName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName>`
                                    
                                    .. attribute:: route
                                    
                                    	Network in prefix/length format
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    .. attribute:: route_attr_list
                                    
                                    	RouteAttributesList
                                    	**type**\:   :py:class:`RouteAttrList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList>`
                                    
                                    .. attribute:: valid_route
                                    
                                    	ValidRoute
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-oc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.best_path = None
                                        self.ext_attributes_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList()
                                        self.ext_attributes_list.parent = self
                                        self.invalid_reason = None
                                        self.last_modified_date = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate()
                                        self.last_modified_date.parent = self
                                        self.last_update_recieved = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved()
                                        self.last_update_recieved.parent = self
                                        self.neighbor_address = None
                                        self.path_id = None
                                        self.prefix_name = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName()
                                        self.prefix_name.parent = self
                                        self.route = None
                                        self.route_attr_list = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList()
                                        self.route_attr_list.parent = self
                                        self.valid_route = None


                                    class PrefixName(object):
                                        """
                                        Prefix
                                        
                                        .. attribute:: prefix
                                        
                                        	Prefix
                                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix>`
                                        
                                        .. attribute:: prefix_length
                                        
                                        	Prefix length
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.prefix = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix()
                                            self.prefix.parent = self
                                            self.prefix_length = None


                                        class Prefix(object):
                                            """
                                            Prefix
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:prefix-name'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.prefix is not None and self.prefix._has_data():
                                                return True

                                            if self.prefix_length is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']


                                    class RouteAttrList(object):
                                        """
                                        RouteAttributesList
                                        
                                        .. attribute:: aggregrator_attributes
                                        
                                        	AggregatorList
                                        	**type**\:   :py:class:`AggregratorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes>`
                                        
                                        .. attribute:: as4_path
                                        
                                        	AS4 Path
                                        	**type**\:  str
                                        
                                        .. attribute:: as_path
                                        
                                        	AS Path
                                        	**type**\:  str
                                        
                                        .. attribute:: atomic_aggr
                                        
                                        	AtomicAggr
                                        	**type**\:  bool
                                        
                                        .. attribute:: community
                                        
                                        	CommunityArray
                                        	**type**\: list of    :py:class:`Community <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community>`
                                        
                                        .. attribute:: local_pref
                                        
                                        	LocalPref
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: med
                                        
                                        	Med
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: next_hop
                                        
                                        	NextHopAddress
                                        	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop>`
                                        
                                        .. attribute:: origin_type
                                        
                                        	Origin Attribute Type
                                        	**type**\:   :py:class:`BgpOcOriginAttrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcOriginAttrEnum>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aggregrator_attributes = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes()
                                            self.aggregrator_attributes.parent = self
                                            self.as4_path = None
                                            self.as_path = None
                                            self.atomic_aggr = None
                                            self.community = YList()
                                            self.community.parent = self
                                            self.community.name = 'community'
                                            self.local_pref = None
                                            self.med = None
                                            self.next_hop = OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop()
                                            self.next_hop.parent = self
                                            self.origin_type = None


                                        class NextHop(object):
                                            """
                                            NextHopAddress
                                            
                                            .. attribute:: afi
                                            
                                            	AFI
                                            	**type**\:   :py:class:`BgpOcAfiEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.BgpOcAfiEnum>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 Addr
                                            	**type**\:  str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.afi = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:next-hop'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.afi is not None:
                                                    return True

                                                if self.ipv4_address is not None:
                                                    return True

                                                if self.ipv6_address is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info']


                                        class AggregratorAttributes(object):
                                            """
                                            AggregatorList
                                            
                                            .. attribute:: address
                                            
                                            	IPv4 address
                                            	**type**\:  str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: as4
                                            
                                            	AS4 number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_
                                            
                                            	AS number
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.address = None
                                                self.as4 = None
                                                self.as_ = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:aggregrator-attributes'

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
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info']


                                        class Community(object):
                                            """
                                            CommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route-attr-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aggregrator_attributes is not None and self.aggregrator_attributes._has_data():
                                                return True

                                            if self.as4_path is not None:
                                                return True

                                            if self.as_path is not None:
                                                return True

                                            if self.atomic_aggr is not None:
                                                return True

                                            if self.community is not None:
                                                for child_ref in self.community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.local_pref is not None:
                                                return True

                                            if self.med is not None:
                                                return True

                                            if self.next_hop is not None and self.next_hop._has_data():
                                                return True

                                            if self.origin_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']


                                    class ExtAttributesList(object):
                                        """
                                        ExtAttributesList
                                        
                                        .. attribute:: aigp
                                        
                                        	AIGP
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: cluster
                                        
                                        	ClusterList
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: ext_community
                                        
                                        	ExtendedCommunityArray
                                        	**type**\: list of    :py:class:`ExtCommunity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity>`
                                        
                                        .. attribute:: originator_id
                                        
                                        	OriginatorID
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: path_id
                                        
                                        	PathId
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: unknown_attributes
                                        
                                        	UnknownAttributes
                                        	**type**\: list of    :py:class:`UnknownAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper.OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.aigp = None
                                            self.cluster = YLeafList()
                                            self.cluster.parent = self
                                            self.cluster.name = 'cluster'
                                            self.ext_community = YList()
                                            self.ext_community.parent = self
                                            self.ext_community.name = 'ext_community'
                                            self.originator_id = None
                                            self.path_id = None
                                            self.unknown_attributes = YList()
                                            self.unknown_attributes.parent = self
                                            self.unknown_attributes.name = 'unknown_attributes'


                                        class ExtCommunity(object):
                                            """
                                            ExtendedCommunityArray
                                            
                                            .. attribute:: objects
                                            
                                            	BGP OC objects
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.objects = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-community'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.objects is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info']


                                        class UnknownAttributes(object):
                                            """
                                            UnknownAttributes
                                            
                                            .. attribute:: attribute_length
                                            
                                            	AttributeLength
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_type
                                            
                                            	AttributeType
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: attribute_value
                                            
                                            	Atributevalue
                                            	**type**\:  str
                                            
                                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                            
                                            

                                            """

                                            _prefix = 'ipv4-bgp-oc-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.attribute_length = None
                                                self.attribute_type = None
                                                self.attribute_value = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:unknown-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attribute_length is not None:
                                                    return True

                                                if self.attribute_type is not None:
                                                    return True

                                                if self.attribute_value is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:ext-attributes-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.aigp is not None:
                                                return True

                                            if self.cluster is not None:
                                                for child in self.cluster:
                                                    if child is not None:
                                                        return True

                                            if self.ext_community is not None:
                                                for child_ref in self.ext_community:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.originator_id is not None:
                                                return True

                                            if self.path_id is not None:
                                                return True

                                            if self.unknown_attributes is not None:
                                                for child_ref in self.unknown_attributes:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']


                                    class LastModifiedDate(object):
                                        """
                                        LastModifiedDate
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-modified-date'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info']


                                    class LastUpdateRecieved(object):
                                        """
                                        LastUpdateRecieved
                                        
                                        .. attribute:: time_value
                                        
                                        	TimeValue
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-bgp-oc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_value = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:last-update-recieved'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_value is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:route'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.best_path is not None:
                                            return True

                                        if self.ext_attributes_list is not None and self.ext_attributes_list._has_data():
                                            return True

                                        if self.invalid_reason is not None:
                                            return True

                                        if self.last_modified_date is not None and self.last_modified_date._has_data():
                                            return True

                                        if self.last_update_recieved is not None and self.last_update_recieved._has_data():
                                            return True

                                        if self.neighbor_address is not None:
                                            return True

                                        if self.path_id is not None:
                                            return True

                                        if self.prefix_name is not None and self.prefix_name._has_data():
                                            return True

                                        if self.route is not None:
                                            return True

                                        if self.route_attr_list is not None and self.route_attr_list._has_data():
                                            return True

                                        if self.valid_route is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:routes'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']


                            class NumRoutes(object):
                                """
                                Number of routes in adjacency rib out\-bound
                                post\-policy table
                                
                                .. attribute:: num_routes
                                
                                	NumRoutes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'ipv4-bgp-oc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.num_routes = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:num-routes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.num_routes is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-oc-oper:adj-rib-in-pre'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.num_routes is not None and self.num_routes._has_data():
                                    return True

                                if self.routes is not None and self.routes._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']

                        @property
                        def _common_path(self):
                            if self.neighbor_address is None:
                                raise YPYModelError('Key property neighbor_address is None')

                            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbors/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbor[Cisco-IOS-XR-ipv4-bgp-oc-oper:neighbor-address = ' + str(self.neighbor_address) + ']'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                            return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast/Cisco-IOS-XR-ipv4-bgp-oc-oper:open-config-neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.open_config_neighbor is not None:
                            for child_ref in self.open_config_neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                        return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table/Cisco-IOS-XR-ipv4-bgp-oc-oper:ipv6-unicast'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.loc_rib is not None and self.loc_rib._has_data():
                        return True

                    if self.open_config_neighbors is not None and self.open_config_neighbors._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                    return meta._meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib/Cisco-IOS-XR-ipv4-bgp-oc-oper:afi-safi-table'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipv4_unicast is not None and self.ipv4_unicast._has_data():
                    return True

                if self.ipv6_unicast is not None and self.ipv6_unicast._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
                return meta._meta_table['OcBgp.BgpRib.AfiSafiTable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp/Cisco-IOS-XR-ipv4-bgp-oc-oper:bgp-rib'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.afi_safi_table is not None and self.afi_safi_table._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
            return meta._meta_table['OcBgp.BgpRib']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-bgp-oc-oper:oc-bgp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.bgp_rib is not None and self.bgp_rib._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_oc_oper as meta
        return meta._meta_table['OcBgp']['meta_info']


