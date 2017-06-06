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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Local_Defined_Next_HopIdentity(object):
    """
    A base identity type of local defined next\-hops
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_local_routing as meta
        return meta._meta_table['Local_Defined_Next_HopIdentity']['meta_info']


class LocalRoutes(object):
    """
    Top\-level container for local routes
    
    .. attribute:: config
    
    	Configuration data for locally defined routes
    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.Config>`
    
    .. attribute:: local_aggregates
    
    	Enclosing container for locally\-defined aggregate routes
    	**type**\:   :py:class:`LocalAggregates <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates>`
    
    .. attribute:: state
    
    	Operational state data for locally defined routes
    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.State>`
    
    .. attribute:: static_routes
    
    	Enclosing container for the list of static routes
    	**type**\:   :py:class:`StaticRoutes <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes>`
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        self.config = LocalRoutes.Config()
        self.config.parent = self
        self.local_aggregates = LocalRoutes.LocalAggregates()
        self.local_aggregates.parent = self
        self.state = LocalRoutes.State()
        self.state.parent = self
        self.static_routes = LocalRoutes.StaticRoutes()
        self.static_routes.parent = self


    class Config(object):
        """
        Configuration data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-local-routing:local-routes/openconfig-local-routing:config'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
            return meta._meta_table['LocalRoutes.Config']['meta_info']


    class State(object):
        """
        Operational state data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/openconfig-local-routing:local-routes/openconfig-local-routing:state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
            return meta._meta_table['LocalRoutes.State']['meta_info']


    class StaticRoutes(object):
        """
        Enclosing container for the list of static routes
        
        .. attribute:: static
        
        	List of locally configured static routes
        	**type**\: list of    :py:class:`Static <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static>`
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            self.parent = None
            self.static = YList()
            self.static.parent = self
            self.static.name = 'static'


        class Static(object):
            """
            List of locally configured static routes
            
            .. attribute:: prefix  <key>
            
            	Reference to the destination prefix list key
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: config
            
            	Configuration data for static routes
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.Config>`
            
            .. attribute:: next_hops
            
            	Configuration and state parameters relating to the next\-hops that are to be utilised for the static route being specified
            	**type**\:   :py:class:`NextHops <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops>`
            
            .. attribute:: state
            
            	Operational state data for static routes
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.State>`
            
            

            """

            _prefix = 'oc-loc-rt'
            _revision = '2016-05-11'

            def __init__(self):
                self.parent = None
                self.prefix = None
                self.config = LocalRoutes.StaticRoutes.Static.Config()
                self.config.parent = self
                self.next_hops = LocalRoutes.StaticRoutes.Static.NextHops()
                self.next_hops.parent = self
                self.state = LocalRoutes.StaticRoutes.Static.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for static routes
                
                .. attribute:: prefix
                
                	Destination prefix for the static route, either IPv4 or IPv6
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                
                ----
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2016-05-11'

                def __init__(self):
                    self.parent = None
                    self.prefix = None
                    self.set_tag = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-local-routing:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.prefix is not None:
                        return True

                    if self.set_tag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                    return meta._meta_table['LocalRoutes.StaticRoutes.Static.Config']['meta_info']


            class State(object):
                """
                Operational state data for static routes
                
                .. attribute:: prefix
                
                	Destination prefix for the static route, either IPv4 or IPv6
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                
                ----
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2016-05-11'

                def __init__(self):
                    self.parent = None
                    self.prefix = None
                    self.set_tag = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-local-routing:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefix is not None:
                        return True

                    if self.set_tag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                    return meta._meta_table['LocalRoutes.StaticRoutes.Static.State']['meta_info']


            class NextHops(object):
                """
                Configuration and state parameters relating to the
                next\-hops that are to be utilised for the static
                route being specified
                
                .. attribute:: next_hop
                
                	A list of next\-hops to be utilised for the static route being specified
                	**type**\: list of    :py:class:`NextHop <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop>`
                
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2016-05-11'

                def __init__(self):
                    self.parent = None
                    self.next_hop = YList()
                    self.next_hop.parent = self
                    self.next_hop.name = 'next_hop'


                class NextHop(object):
                    """
                    A list of next\-hops to be utilised for the static
                    route being specified.
                    
                    .. attribute:: index  <key>
                    
                    	A reference to the index of the current next\-hop. The index is intended to be a user\-specified value which can be used to reference the next\-hop in question, without any other semantics being assigned to it
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to the next\-hop entry
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config>`
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef>`
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the next\-hop entry
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State>`
                    
                    

                    """

                    _prefix = 'oc-loc-rt'
                    _revision = '2016-05-11'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config()
                        self.config.parent = self
                        self.interface_ref = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef()
                        self.interface_ref.parent = self
                        self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters relating to the next\-hop
                        entry
                        
                        .. attribute:: index
                        
                        	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                        	**type**\:  str
                        
                        .. attribute:: metric
                        
                        	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        
                        ----
                        	**type**\:   :py:class:`Local_Defined_Next_HopIdentity <ydk.models.openconfig.openconfig_local_routing.Local_Defined_Next_HopIdentity>`
                        
                        
                        ----
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2016-05-11'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.metric = None
                            self.next_hop = None
                            self.recurse = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-local-routing:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            if self.recurse is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                            return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config']['meta_info']


                    class State(object):
                        """
                        Operational state parameters relating to the
                        next\-hop entry
                        
                        .. attribute:: index
                        
                        	An user\-specified identifier utilised to uniquely reference the next\-hop entry in the next\-hop list. The value of this index has no semantic meaning other than for referencing the entry
                        	**type**\:  str
                        
                        .. attribute:: metric
                        
                        	A metric which is utilised to specify the preference of the next\-hop entry when it is injected into the RIB. The lower the metric, the more preferable the prefix is. When this value is not specified the metric is inherited from the default metric utilised for static routes within the network instance that the static routes are being instantiated. When multiple next\-hops are specified for a static route, the metric is utilised to determine which of the next\-hops is to be installed in the RIB. When multiple next\-hops have the same metric (be it specified, or simply the default) then these next\-hops should all be installed in the RIB
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	The next\-hop that is to be used for the static route \- this may be specified as an IP address, an interface or a pre\-defined next\-hop type \- for instance, DROP or LOCAL\_LINK. When this leaf is not set, and the interface\-ref value is specified for the next\-hop, then the system should treat the prefix as though it is directly connected to the interface
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        
                        ----
                        	**type**\:   :py:class:`Local_Defined_Next_HopIdentity <ydk.models.openconfig.openconfig_local_routing.Local_Defined_Next_HopIdentity>`
                        
                        
                        ----
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2016-05-11'

                        def __init__(self):
                            self.parent = None
                            self.index = None
                            self.metric = None
                            self.next_hop = None
                            self.recurse = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-local-routing:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.index is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            if self.recurse is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                            return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State']['meta_info']


                    class InterfaceRef(object):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State>`
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2016-05-11'

                        def __init__(self):
                            self.parent = None
                            self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config()
                            self.config.parent = self
                            self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-loc-rt'
                            _revision = '2016-05-11'

                            def __init__(self):
                                self.parent = None
                                self.interface = None
                                self.subinterface = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-local-routing:config'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.interface is not None:
                                    return True

                                if self.subinterface is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                                return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config']['meta_info']


                        class State(object):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-loc-rt'
                            _revision = '2016-05-11'

                            def __init__(self):
                                self.parent = None
                                self.interface = None
                                self.subinterface = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-local-routing:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.interface is not None:
                                    return True

                                if self.subinterface is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                                return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-local-routing:interface-ref'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                            return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/openconfig-local-routing:next-hop[openconfig-local-routing:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.interface_ref is not None and self.interface_ref._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                        return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-local-routing:next-hops'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.next_hop is not None:
                        for child_ref in self.next_hop:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                    return meta._meta_table['LocalRoutes.StaticRoutes.Static.NextHops']['meta_info']

            @property
            def _common_path(self):
                if self.prefix is None:
                    raise YPYModelError('Key property prefix is None')

                return '/openconfig-local-routing:local-routes/openconfig-local-routing:static-routes/openconfig-local-routing:static[openconfig-local-routing:prefix = ' + str(self.prefix) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prefix is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.next_hops is not None and self.next_hops._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                return meta._meta_table['LocalRoutes.StaticRoutes.Static']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-local-routing:local-routes/openconfig-local-routing:static-routes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.static is not None:
                for child_ref in self.static:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
            return meta._meta_table['LocalRoutes.StaticRoutes']['meta_info']


    class LocalAggregates(object):
        """
        Enclosing container for locally\-defined aggregate
        routes
        
        .. attribute:: aggregate
        
        	List of aggregates
        	**type**\: list of    :py:class:`Aggregate <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate>`
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            self.parent = None
            self.aggregate = YList()
            self.aggregate.parent = self
            self.aggregate.name = 'aggregate'


        class Aggregate(object):
            """
            List of aggregates
            
            .. attribute:: prefix  <key>
            
            	Reference to the configured prefix for this aggregate
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            
            ----
            .. attribute:: config
            
            	Configuration data for aggregate advertisements
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate.Config>`
            
            .. attribute:: state
            
            	Operational state data for aggregate advertisements
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.LocalAggregates.Aggregate.State>`
            
            

            """

            _prefix = 'oc-loc-rt'
            _revision = '2016-05-11'

            def __init__(self):
                self.parent = None
                self.prefix = None
                self.config = LocalRoutes.LocalAggregates.Aggregate.Config()
                self.config.parent = self
                self.state = LocalRoutes.LocalAggregates.Aggregate.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for aggregate advertisements
                
                .. attribute:: discard
                
                	When true, install the aggregate route with a discard next\-hop \-\- traffic destined to the aggregate will be discarded with no ICMP message generated.  When false, traffic destined to an aggregate address when no constituent routes are present will generate an ICMP unreachable message
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: prefix
                
                	Aggregate prefix to be advertised
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                
                ----
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2016-05-11'

                def __init__(self):
                    self.parent = None
                    self.discard = None
                    self.prefix = None
                    self.set_tag = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-local-routing:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.discard is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.set_tag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                    return meta._meta_table['LocalRoutes.LocalAggregates.Aggregate.Config']['meta_info']


            class State(object):
                """
                Operational state data for aggregate
                advertisements
                
                .. attribute:: discard
                
                	When true, install the aggregate route with a discard next\-hop \-\- traffic destined to the aggregate will be discarded with no ICMP message generated.  When false, traffic destined to an aggregate address when no constituent routes are present will generate an ICMP unreachable message
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: prefix
                
                	Aggregate prefix to be advertised
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: set_tag
                
                	Set a generic tag value on the route. This tag can be used for filtering routes that are distributed to other routing protocols
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                
                ----
                

                """

                _prefix = 'oc-loc-rt'
                _revision = '2016-05-11'

                def __init__(self):
                    self.parent = None
                    self.discard = None
                    self.prefix = None
                    self.set_tag = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-local-routing:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.discard is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.set_tag is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                    return meta._meta_table['LocalRoutes.LocalAggregates.Aggregate.State']['meta_info']

            @property
            def _common_path(self):
                if self.prefix is None:
                    raise YPYModelError('Key property prefix is None')

                return '/openconfig-local-routing:local-routes/openconfig-local-routing:local-aggregates/openconfig-local-routing:aggregate[openconfig-local-routing:prefix = ' + str(self.prefix) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prefix is not None:
                    return True

                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_local_routing as meta
                return meta._meta_table['LocalRoutes.LocalAggregates.Aggregate']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-local-routing:local-routes/openconfig-local-routing:local-aggregates'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.aggregate is not None:
                for child_ref in self.aggregate:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_local_routing as meta
            return meta._meta_table['LocalRoutes.LocalAggregates']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-local-routing:local-routes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.config is not None and self.config._has_data():
            return True

        if self.local_aggregates is not None and self.local_aggregates._has_data():
            return True

        if self.state is not None and self.state._has_data():
            return True

        if self.static_routes is not None and self.static_routes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_local_routing as meta
        return meta._meta_table['LocalRoutes']['meta_info']


class DropIdentity(Local_Defined_Next_HopIdentity):
    """
    Discard traffic for the corresponding destination
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        Local_Defined_Next_HopIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_local_routing as meta
        return meta._meta_table['DropIdentity']['meta_info']


class Local_LinkIdentity(Local_Defined_Next_HopIdentity):
    """
    Treat traffic towards addresses within the specified
    next\-hop prefix as though they are connected to a local
    link. When the LOCAL\_LINK next\-hop type is specified,
    an interface must also be specified such that
    the local system can determine which link to trigger
    link\-layer address discovery against
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        Local_Defined_Next_HopIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_local_routing as meta
        return meta._meta_table['Local_LinkIdentity']['meta_info']


