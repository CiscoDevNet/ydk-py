""" openconfig_local_routing 

This module describes configuration and operational state data
for routes that are locally generated, i.e., not created by
dynamic routing protocols.  These include static routes, locally
created aggregate routes for reducing the number of constituent
routes that must be advertised, summary routes for IGPs, etc.

This model expresses locally generated routes as generically as
possible, avoiding configuration of protocol\-specific attributes
at the time of route creation.  This is primarily to avoid
assumptions about how underlying router implementations handle
route attributes in various routing table data structures they
maintain.  Hence, the definition of locally generated routes
essentially creates 'bare' routes that do not have any protocol\-
specific attributes.

When protocol\-specific attributes must be attached to a route
(e.g., communities on a locally defined route meant to be
advertised via BGP), the attributes should be attached via a
protocol\-specific policy after importing the route into the
protocol for distribution (again via routing policy).

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class LOCALDEFINEDNEXTHOP(Identity):
    """
    A base identity type of local defined next\-hops
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2017-05-15'

    def __init__(self, ns="http://openconfig.net/yang/local-routing", pref="openconfig-local-routing", tag="openconfig-local-routing:LOCAL_DEFINED_NEXT_HOP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCALDEFINEDNEXTHOP, self).__init__(ns, pref, tag)



class LocalRoutes(_Entity_):
    """
    Top\-level container for local routes
    
    .. attribute:: config
    
    	Configuration data for locally defined routes
    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.Config>`
    
    .. attribute:: state
    
    	Operational state data for locally defined routes
    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.State>`
    
    	**config**\: False
    
    .. attribute:: static_routes
    
    	Enclosing container for the list of static routes
    	**type**\:  :py:class:`StaticRoutes <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes>`
    
    .. attribute:: local_aggregates
    
    	Enclosing container for locally\-defined aggregate routes
    	**type**\:  :py:class:`LocalAggregates <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates>`
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2017-05-15'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(LocalRoutes, self).__init__()
        self._top_entity = None

        self.yang_name = "local-routes"
        self.yang_parent_name = "openconfig-local-routing"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", LocalRoutes.Config)), ("state", ("state", LocalRoutes.State)), ("static-routes", ("static_routes", LocalRoutes.StaticRoutes)), ("local-aggregates", ("local_aggregates", LocalRoutes.LocalAggregates))])
        self._leafs = OrderedDict()

        self.config = LocalRoutes.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.state = LocalRoutes.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"

        self.static_routes = LocalRoutes.StaticRoutes()
        self.static_routes.parent = self
        self._children_name_map["static_routes"] = "static-routes"

        self.local_aggregates = LocalRoutes.LocalAggregates()
        self.local_aggregates.parent = self
        self._children_name_map["local_aggregates"] = "local-aggregates"
        self._segment_path = lambda: "openconfig-local-routing:local-routes"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(LocalRoutes, [], name, value)


    class Config(_Entity_):
        """
        Configuration data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2017-05-15'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LocalRoutes.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "local-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "openconfig-local-routing:local-routes/%s" % self._segment_path()
            self._is_frozen = True



    class State(_Entity_):
        """
        Operational state data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2017-05-15'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LocalRoutes.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "local-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict()
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "openconfig-local-routing:local-routes/%s" % self._segment_path()
            self._is_frozen = True



    class StaticRoutes(_Entity_):
        """
        Enclosing container for the list of static routes
        
        .. attribute:: static
        
        	List of locally configured static routes
        	**type**\: list of  		 :py:class:`Static <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static>`
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2017-05-15'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LocalRoutes.StaticRoutes, self).__init__()

            self.yang_name = "static-routes"
            self.yang_parent_name = "local-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("static", ("static", LocalRoutes.StaticRoutes.Static))])
            self._leafs = OrderedDict()

            self.static = YList(self)
            self._segment_path = lambda: "static-routes"
            self._absolute_path = lambda: "openconfig-local-routing:local-routes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LocalRoutes.StaticRoutes, [], name, value)


        class Static(_Entity_):
            """
            List of locally configured static routes
            
            .. attribute:: prefix  (key)
            
            	Reference to the destination prefix list key
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
            
            	**refers to**\:  :py:class:`prefix <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.Config>`
            
            .. attribute:: config
            
            	Configuration data for static routes
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.Config>`
            
            .. attribute:: state
            
            	Operational state data for static routes
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.State>`
            
            	**config**\: False
            
            .. attribute:: next_hops
            
            	Configuration and state parameters relating to the next\-hops that are to be utilised for the static route being specified
            	**type**\:  :py:class:`NextHops <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops>`
            
            

            """

            _prefix = 'oc-loc-rt'
            _revision = '2017-05-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(LocalRoutes.StaticRoutes.Static, self).__init__()

                self.yang_name = "static"
                self.yang_parent_name = "static-routes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['prefix']
                self._child_classes = OrderedDict([("config", ("config", LocalRoutes.StaticRoutes.Static.Config)), ("state", ("state", LocalRoutes.StaticRoutes.Static.State)), ("next-hops", ("next_hops", LocalRoutes.StaticRoutes.Static.NextHops))])
                self._leafs = OrderedDict([
                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                ])
                self.prefix = None

                self.config = LocalRoutes.StaticRoutes.Static.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = LocalRoutes.StaticRoutes.Static.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.next_hops = LocalRoutes.StaticRoutes.Static.NextHops()
                self.next_hops.parent = self
                self._children_name_map["next_hops"] = "next-hops"
                self._segment_path = lambda: "static" + "[prefix='" + str(self.prefix) + "']"
                self._absolute_path = lambda: "openconfig-local-routing:local-routes/static-routes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LocalRoutes.StaticRoutes.Static, ['prefix'], name, value)


            class Config(_Entity_):
                """
                Configuration data for static routes
                
                .. attribute:: prefix
                
                	Destination prefix for the static route, either IPv4 or IPv6
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 0..4294967295
                
                		**type**\: str
                
                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2017-05-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LocalRoutes.StaticRoutes.Static.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "static"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                        ('set_tag', (YLeaf(YType.str, 'set-tag'), ['int','str'])),
                    ])
                    self.prefix = None
                    self.set_tag = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LocalRoutes.StaticRoutes.Static.Config, ['prefix', 'set_tag'], name, value)



            class State(_Entity_):
                """
                Operational state data for static routes
                
                .. attribute:: prefix
                
                	Destination prefix for the static route, either IPv4 or IPv6
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                
                	**config**\: False
                
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 0..4294967295
                
                		**type**\: str
                
                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2017-05-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LocalRoutes.StaticRoutes.Static.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "static"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                        ('set_tag', (YLeaf(YType.str, 'set-tag'), ['int','str'])),
                    ])
                    self.prefix = None
                    self.set_tag = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LocalRoutes.StaticRoutes.Static.State, ['prefix', 'set_tag'], name, value)



            class NextHops(_Entity_):
                """
                Configuration and state parameters relating to the
                next\-hops that are to be utilised for the static
                route being specified
                
                .. attribute:: next_hop
                
                	A list of next\-hops to be utilised for the static route being specified
                	**type**\: list of  		 :py:class:`NextHop <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop>`
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2017-05-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LocalRoutes.StaticRoutes.Static.NextHops, self).__init__()

                    self.yang_name = "next-hops"
                    self.yang_parent_name = "static"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("next-hop", ("next_hop", LocalRoutes.StaticRoutes.Static.NextHops.NextHop))])
                    self._leafs = OrderedDict()

                    self.next_hop = YList(self)
                    self._segment_path = lambda: "next-hops"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops, [], name, value)


                class NextHop(_Entity_):
                    """
                    A list of next\-hops to be utilised for the static
                    route being specified.
                    
                    .. attribute:: index  (key)
                    
                    	A reference to the index of the current next\-hop. The index is intended to be a user\-specified value which can be used to reference the next\-hop in question, without any other semantics being assigned to it
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to the next\-hop entry
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the next\-hop entry
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef>`
                    
                    

                    """

                    _prefix = 'oc-loc-rt'
                    _revision = '2017-05-15'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop, self).__init__()

                        self.yang_name = "next-hop"
                        self.yang_parent_name = "next-hops"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([("config", ("config", LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config)), ("state", ("state", LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State)), ("interface-ref", ("interface_ref", LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.str, 'index'), ['str'])),
                        ])
                        self.index = None

                        self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.interface_ref = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                        self._segment_path = lambda: "next-hop" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop, ['index'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters relating to the next\-hop
                        entry
                        
                        .. attribute:: index
                        
                        	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                        	**type**\: str
                        
                        .. attribute:: next_hop
                        
                        	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        		**type**\:  :py:class:`LOCALDEFINEDNEXTHOP <ydk.models.openconfig.openconfig_local_routing.LOCALDEFINEDNEXTHOP>`
                        
                        .. attribute:: metric
                        
                        	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2017-05-15'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "next-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str',('ydk.models.openconfig.openconfig_local_routing', 'LOCALDEFINEDNEXTHOP')])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('recurse', (YLeaf(YType.boolean, 'recurse'), ['bool'])),
                            ])
                            self.index = None
                            self.next_hop = None
                            self.metric = None
                            self.recurse = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config, ['index', 'next_hop', 'metric', 'recurse'], name, value)



                    class State(_Entity_):
                        """
                        Operational state parameters relating to the
                        next\-hop entry
                        
                        .. attribute:: index
                        
                        	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop
                        
                        	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        		**type**\:  :py:class:`LOCALDEFINEDNEXTHOP <ydk.models.openconfig.openconfig_local_routing.LOCALDEFINEDNEXTHOP>`
                        
                        	**config**\: False
                        
                        .. attribute:: metric
                        
                        	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2017-05-15'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "next-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.str, 'index'), ['str'])),
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str',('ydk.models.openconfig.openconfig_local_routing', 'LOCALDEFINEDNEXTHOP')])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('recurse', (YLeaf(YType.boolean, 'recurse'), ['bool'])),
                            ])
                            self.index = None
                            self.next_hop = None
                            self.metric = None
                            self.recurse = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State, ['index', 'next_hop', 'metric', 'recurse'], name, value)



                    class InterfaceRef(_Entity_):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2017-05-15'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "next-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config)), ("state", ("state", LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State))])
                            self._leafs = OrderedDict()

                            self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "interface-ref"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef, [], name, value)


                        class Config(_Entity_):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-loc-rt'
                            _revision = '2017-05-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                        class State(_Entity_):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            	**config**\: False
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-loc-rt'
                            _revision = '2017-05-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State, ['interface', 'subinterface'], name, value)








    class LocalAggregates(_Entity_):
        """
        Enclosing container for locally\-defined aggregate
        routes
        
        .. attribute:: aggregate
        
        	List of aggregates
        	**type**\: list of  		 :py:class:`Aggregate <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate>`
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2017-05-15'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(LocalRoutes.LocalAggregates, self).__init__()

            self.yang_name = "local-aggregates"
            self.yang_parent_name = "local-routes"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("aggregate", ("aggregate", LocalRoutes.LocalAggregates.Aggregate))])
            self._leafs = OrderedDict()

            self.aggregate = YList(self)
            self._segment_path = lambda: "local-aggregates"
            self._absolute_path = lambda: "openconfig-local-routing:local-routes/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(LocalRoutes.LocalAggregates, [], name, value)


        class Aggregate(_Entity_):
            """
            List of aggregates
            
            .. attribute:: prefix  (key)
            
            	Reference to the configured prefix for this aggregate
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
            
            		**type**\: str
            
            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
            
            	**refers to**\:  :py:class:`prefix <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate.Config>`
            
            .. attribute:: config
            
            	Configuration data for aggregate advertisements
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate.Config>`
            
            .. attribute:: state
            
            	Operational state data for aggregate advertisements
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-loc-rt'
            _revision = '2017-05-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(LocalRoutes.LocalAggregates.Aggregate, self).__init__()

                self.yang_name = "aggregate"
                self.yang_parent_name = "local-aggregates"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['prefix']
                self._child_classes = OrderedDict([("config", ("config", LocalRoutes.LocalAggregates.Aggregate.Config)), ("state", ("state", LocalRoutes.LocalAggregates.Aggregate.State))])
                self._leafs = OrderedDict([
                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                ])
                self.prefix = None

                self.config = LocalRoutes.LocalAggregates.Aggregate.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = LocalRoutes.LocalAggregates.Aggregate.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "aggregate" + "[prefix='" + str(self.prefix) + "']"
                self._absolute_path = lambda: "openconfig-local-routing:local-routes/local-aggregates/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(LocalRoutes.LocalAggregates.Aggregate, ['prefix'], name, value)


            class Config(_Entity_):
                """
                Configuration data for aggregate advertisements
                
                .. attribute:: prefix
                
                	Aggregate prefix to be advertised
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                
                .. attribute:: discard
                
                	When true, install the aggregate route with a discard next\-hop \-\- traffic destined to the aggregate will be discarded with no ICMP message generated.  When false, traffic destined to an aggregate address when no constituent routes are present will generate an ICMP unreachable message
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 0..4294967295
                
                		**type**\: str
                
                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2017-05-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LocalRoutes.LocalAggregates.Aggregate.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "aggregate"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                        ('discard', (YLeaf(YType.boolean, 'discard'), ['bool'])),
                        ('set_tag', (YLeaf(YType.str, 'set-tag'), ['int','str'])),
                    ])
                    self.prefix = None
                    self.discard = None
                    self.set_tag = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LocalRoutes.LocalAggregates.Aggregate.Config, ['prefix', 'discard', 'set_tag'], name, value)



            class State(_Entity_):
                """
                Operational state data for aggregate
                advertisements
                
                .. attribute:: prefix
                
                	Aggregate prefix to be advertised
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))$
                
                		**type**\: str
                
                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))/(12[0\-8]\|1[0\-1][0\-9]\|[1\-9][0\-9]\|[0\-9])$
                
                	**config**\: False
                
                .. attribute:: discard
                
                	When true, install the aggregate route with a discard next\-hop \-\- traffic destined to the aggregate will be discarded with no ICMP message generated.  When false, traffic destined to an aggregate address when no constituent routes are present will generate an ICMP unreachable message
                	**type**\: bool
                
                	**config**\: False
                
                	**default value**\: false
                
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: union of the below types:
                
                		**type**\: int
                
                			**range:** 0..4294967295
                
                		**type**\: str
                
                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2017-05-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(LocalRoutes.LocalAggregates.Aggregate.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "aggregate"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                        ('discard', (YLeaf(YType.boolean, 'discard'), ['bool'])),
                        ('set_tag', (YLeaf(YType.str, 'set-tag'), ['int','str'])),
                    ])
                    self.prefix = None
                    self.discard = None
                    self.set_tag = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(LocalRoutes.LocalAggregates.Aggregate.State, ['prefix', 'discard', 'set_tag'], name, value)




    def clone_ptr(self):
        self._top_entity = LocalRoutes()
        return self._top_entity



class DROP(LOCALDEFINEDNEXTHOP):
    """
    Discard traffic for the corresponding destination
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2017-05-15'

    def __init__(self, ns="http://openconfig.net/yang/local-routing", pref="openconfig-local-routing", tag="openconfig-local-routing:DROP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(DROP, self).__init__(ns, pref, tag)



class LOCALLINK(LOCALDEFINEDNEXTHOP):
    """
    Treat traffic towards addresses within the specified
    next\-hop prefix as though they are connected to a local
    link. When the LOCAL\_LINK next\-hop type is specified,
    an interface must also be specified such that
    the local system can determine which link to trigger
    link\-layer address discovery against
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2017-05-15'

    def __init__(self, ns="http://openconfig.net/yang/local-routing", pref="openconfig-local-routing", tag="openconfig-local-routing:LOCAL_LINK"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(LOCALLINK, self).__init__(ns, pref, tag)



