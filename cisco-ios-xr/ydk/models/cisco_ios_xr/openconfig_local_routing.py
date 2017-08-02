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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Local_Defined_Next_Hop(Identity):
    """
    A base identity type of local defined next\-hops
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        super(Local_Defined_Next_Hop, self).__init__("http://openconfig.net/yang/local-routing", "openconfig-local-routing", "openconfig-local-routing:LOCAL_DEFINED_NEXT_HOP")


class LocalRoutes(Entity):
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
        super(LocalRoutes, self).__init__()
        self._top_entity = None

        self.yang_name = "local-routes"
        self.yang_parent_name = "openconfig-local-routing"

        self.config = LocalRoutes.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._children_yang_names.add("config")

        self.local_aggregates = LocalRoutes.LocalAggregates()
        self.local_aggregates.parent = self
        self._children_name_map["local_aggregates"] = "local-aggregates"
        self._children_yang_names.add("local-aggregates")

        self.state = LocalRoutes.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._children_yang_names.add("state")

        self.static_routes = LocalRoutes.StaticRoutes()
        self.static_routes.parent = self
        self._children_name_map["static_routes"] = "static-routes"
        self._children_yang_names.add("static-routes")


    class Config(Entity):
        """
        Configuration data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            super(LocalRoutes.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "local-routes"

        def has_data(self):
            return False

        def has_operation(self):
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "config" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-local-routing:local-routes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class State(Entity):
        """
        Operational state data for locally defined routes
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            super(LocalRoutes.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "local-routes"

        def has_data(self):
            return False

        def has_operation(self):
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "state" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-local-routing:local-routes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class StaticRoutes(Entity):
        """
        Enclosing container for the list of static routes
        
        .. attribute:: static
        
        	List of locally configured static routes
        	**type**\: list of    :py:class:`Static <ydk.models.openconfig.openconfig_local_routing.LocalRoutes.StaticRoutes.Static>`
        
        

        """

        _prefix = 'oc-loc-rt'
        _revision = '2016-05-11'

        def __init__(self):
            super(LocalRoutes.StaticRoutes, self).__init__()

            self.yang_name = "static-routes"
            self.yang_parent_name = "local-routes"

            self.static = YList(self)

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
                        super(LocalRoutes.StaticRoutes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LocalRoutes.StaticRoutes, self).__setattr__(name, value)


        class Static(Entity):
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
                super(LocalRoutes.StaticRoutes.Static, self).__init__()

                self.yang_name = "static"
                self.yang_parent_name = "static-routes"

                self.prefix = YLeaf(YType.str, "prefix")

                self.config = LocalRoutes.StaticRoutes.Static.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.next_hops = LocalRoutes.StaticRoutes.Static.NextHops()
                self.next_hops.parent = self
                self._children_name_map["next_hops"] = "next-hops"
                self._children_yang_names.add("next-hops")

                self.state = LocalRoutes.StaticRoutes.Static.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prefix") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LocalRoutes.StaticRoutes.Static, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LocalRoutes.StaticRoutes.Static, self).__setattr__(name, value)


            class Config(Entity):
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
                    super(LocalRoutes.StaticRoutes.Static.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "static"

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.set_tag = YLeaf(YType.str, "set-tag")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prefix",
                                    "set_tag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LocalRoutes.StaticRoutes.Static.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LocalRoutes.StaticRoutes.Static.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prefix.is_set or
                        self.set_tag.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.set_tag.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.set_tag.is_set or self.set_tag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_tag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix" or name == "set-tag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "set-tag"):
                        self.set_tag = value
                        self.set_tag.value_namespace = name_space
                        self.set_tag.value_namespace_prefix = name_space_prefix


            class State(Entity):
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
                    super(LocalRoutes.StaticRoutes.Static.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "static"

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.set_tag = YLeaf(YType.str, "set-tag")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prefix",
                                    "set_tag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LocalRoutes.StaticRoutes.Static.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LocalRoutes.StaticRoutes.Static.State, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prefix.is_set or
                        self.set_tag.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.set_tag.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.set_tag.is_set or self.set_tag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_tag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix" or name == "set-tag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "set-tag"):
                        self.set_tag = value
                        self.set_tag.value_namespace = name_space
                        self.set_tag.value_namespace_prefix = name_space_prefix


            class NextHops(Entity):
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
                    super(LocalRoutes.StaticRoutes.Static.NextHops, self).__init__()

                    self.yang_name = "next-hops"
                    self.yang_parent_name = "static"

                    self.next_hop = YList(self)

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
                                super(LocalRoutes.StaticRoutes.Static.NextHops, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LocalRoutes.StaticRoutes.Static.NextHops, self).__setattr__(name, value)


                class NextHop(Entity):
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
                        super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop, self).__init__()

                        self.yang_name = "next-hop"
                        self.yang_parent_name = "next-hops"

                        self.index = YLeaf(YType.str, "index")

                        self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.interface_ref = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                        self._children_yang_names.add("interface-ref")

                        self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop, self).__setattr__(name, value)


                    class Config(Entity):
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
                        	**type**\:   :py:class:`Local_Defined_Next_Hop <ydk.models.openconfig.openconfig_local_routing.Local_Defined_Next_Hop>`
                        
                        
                        ----
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2016-05-11'

                        def __init__(self):
                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "next-hop"

                            self.index = YLeaf(YType.str, "index")

                            self.metric = YLeaf(YType.uint32, "metric")

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.recurse = YLeaf(YType.boolean, "recurse")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "metric",
                                            "next_hop",
                                            "recurse") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.metric.is_set or
                                self.next_hop.is_set or
                                self.recurse.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop.yfilter != YFilter.not_set or
                                self.recurse.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "config" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                            if (self.recurse.is_set or self.recurse.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.recurse.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index" or name == "metric" or name == "next-hop" or name == "recurse"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop"):
                                self.next_hop = value
                                self.next_hop.value_namespace = name_space
                                self.next_hop.value_namespace_prefix = name_space_prefix
                            if(value_path == "recurse"):
                                self.recurse = value
                                self.recurse.value_namespace = name_space
                                self.recurse.value_namespace_prefix = name_space_prefix


                    class State(Entity):
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
                        	**type**\:   :py:class:`Local_Defined_Next_Hop <ydk.models.openconfig.openconfig_local_routing.Local_Defined_Next_Hop>`
                        
                        
                        ----
                        .. attribute:: recurse
                        
                        	Determines whether the next\-hop should be allowed to be looked up recursively \- i.e., via a RIB entry which has been installed by a routing protocol, or another static route \- rather than needing to be connected directly to an interface of the local system within the current network instance. When the interface reference specified within the next\-hop entry is set (i.e., is not null) then forwarding is restricted to being via the interface specified \- and recursion is hence disabled
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-loc-rt'
                        _revision = '2016-05-11'

                        def __init__(self):
                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "next-hop"

                            self.index = YLeaf(YType.str, "index")

                            self.metric = YLeaf(YType.uint32, "metric")

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.recurse = YLeaf(YType.boolean, "recurse")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index",
                                            "metric",
                                            "next_hop",
                                            "recurse") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.index.is_set or
                                self.metric.is_set or
                                self.next_hop.is_set or
                                self.recurse.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop.yfilter != YFilter.not_set or
                                self.recurse.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                            if (self.recurse.is_set or self.recurse.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.recurse.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index" or name == "metric" or name == "next-hop" or name == "recurse"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop"):
                                self.next_hop = value
                                self.next_hop.value_namespace = name_space
                                self.next_hop.value_namespace_prefix = name_space_prefix
                            if(value_path == "recurse"):
                                self.recurse = value
                                self.recurse.value_namespace = name_space
                                self.recurse.value_namespace_prefix = name_space_prefix


                    class InterfaceRef(Entity):
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
                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "next-hop"

                            self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")


                        class Config(Entity):
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
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface",
                                                "subinterface") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface.is_set or
                                    self.subinterface.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.subinterface.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.subinterface.is_set or self.subinterface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.subinterface.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface" or name == "subinterface"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "subinterface"):
                                    self.subinterface = value
                                    self.subinterface.value_namespace = name_space
                                    self.subinterface.value_namespace_prefix = name_space_prefix


                        class State(Entity):
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
                                super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface",
                                                "subinterface") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.interface.is_set or
                                    self.subinterface.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.subinterface.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.subinterface.is_set or self.subinterface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.subinterface.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface" or name == "subinterface"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "subinterface"):
                                    self.subinterface = value
                                    self.subinterface.value_namespace = name_space
                                    self.subinterface.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.config is not None and self.config.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-ref" + path_buffer

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

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "config" or name == "state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.index.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.interface_ref is not None and self.interface_ref.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.interface_ref is not None and self.interface_ref.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "next-hop" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "interface-ref"):
                            if (self.interface_ref is None):
                                self.interface_ref = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef()
                                self.interface_ref.parent = self
                                self._children_name_map["interface_ref"] = "interface-ref"
                            return self.interface_ref

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "interface-ref" or name == "state" or name == "index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.next_hop:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.next_hop:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "next-hops" + path_buffer

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

                    if (child_yang_name == "next-hop"):
                        for c in self.next_hop:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = LocalRoutes.StaticRoutes.Static.NextHops.NextHop()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.next_hop.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "next-hop"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.prefix.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.next_hops is not None and self.next_hops.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prefix.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.next_hops is not None and self.next_hops.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "static" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-local-routing:local-routes/static-routes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prefix.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = LocalRoutes.StaticRoutes.Static.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "next-hops"):
                    if (self.next_hops is None):
                        self.next_hops = LocalRoutes.StaticRoutes.Static.NextHops()
                        self.next_hops.parent = self
                        self._children_name_map["next_hops"] = "next-hops"
                    return self.next_hops

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = LocalRoutes.StaticRoutes.Static.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "next-hops" or name == "state" or name == "prefix"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prefix"):
                    self.prefix = value
                    self.prefix.value_namespace = name_space
                    self.prefix.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.static:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.static:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "static-routes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-local-routing:local-routes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "static"):
                for c in self.static:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LocalRoutes.StaticRoutes.Static()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.static.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "static"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LocalAggregates(Entity):
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
            super(LocalRoutes.LocalAggregates, self).__init__()

            self.yang_name = "local-aggregates"
            self.yang_parent_name = "local-routes"

            self.aggregate = YList(self)

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
                        super(LocalRoutes.LocalAggregates, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(LocalRoutes.LocalAggregates, self).__setattr__(name, value)


        class Aggregate(Entity):
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
                super(LocalRoutes.LocalAggregates.Aggregate, self).__init__()

                self.yang_name = "aggregate"
                self.yang_parent_name = "local-aggregates"

                self.prefix = YLeaf(YType.str, "prefix")

                self.config = LocalRoutes.LocalAggregates.Aggregate.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = LocalRoutes.LocalAggregates.Aggregate.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prefix") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(LocalRoutes.LocalAggregates.Aggregate, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(LocalRoutes.LocalAggregates.Aggregate, self).__setattr__(name, value)


            class Config(Entity):
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
                    super(LocalRoutes.LocalAggregates.Aggregate.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "aggregate"

                    self.discard = YLeaf(YType.boolean, "discard")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.set_tag = YLeaf(YType.str, "set-tag")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discard",
                                    "prefix",
                                    "set_tag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LocalRoutes.LocalAggregates.Aggregate.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LocalRoutes.LocalAggregates.Aggregate.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.discard.is_set or
                        self.prefix.is_set or
                        self.set_tag.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discard.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.set_tag.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discard.is_set or self.discard.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discard.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.set_tag.is_set or self.set_tag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_tag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discard" or name == "prefix" or name == "set-tag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discard"):
                        self.discard = value
                        self.discard.value_namespace = name_space
                        self.discard.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "set-tag"):
                        self.set_tag = value
                        self.set_tag.value_namespace = name_space
                        self.set_tag.value_namespace_prefix = name_space_prefix


            class State(Entity):
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
                    super(LocalRoutes.LocalAggregates.Aggregate.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "aggregate"

                    self.discard = YLeaf(YType.boolean, "discard")

                    self.prefix = YLeaf(YType.str, "prefix")

                    self.set_tag = YLeaf(YType.str, "set-tag")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discard",
                                    "prefix",
                                    "set_tag") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(LocalRoutes.LocalAggregates.Aggregate.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(LocalRoutes.LocalAggregates.Aggregate.State, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.discard.is_set or
                        self.prefix.is_set or
                        self.set_tag.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discard.yfilter != YFilter.not_set or
                        self.prefix.yfilter != YFilter.not_set or
                        self.set_tag.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discard.is_set or self.discard.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discard.get_name_leafdata())
                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix.get_name_leafdata())
                    if (self.set_tag.is_set or self.set_tag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.set_tag.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discard" or name == "prefix" or name == "set-tag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discard"):
                        self.discard = value
                        self.discard.value_namespace = name_space
                        self.discard.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix"):
                        self.prefix = value
                        self.prefix.value_namespace = name_space
                        self.prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "set-tag"):
                        self.set_tag = value
                        self.set_tag.value_namespace = name_space
                        self.set_tag.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.prefix.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prefix.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "aggregate" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-local-routing:local-routes/local-aggregates/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prefix.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = LocalRoutes.LocalAggregates.Aggregate.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = LocalRoutes.LocalAggregates.Aggregate.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "state" or name == "prefix"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prefix"):
                    self.prefix = value
                    self.prefix.value_namespace = name_space
                    self.prefix.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.aggregate:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.aggregate:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "local-aggregates" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-local-routing:local-routes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "aggregate"):
                for c in self.aggregate:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = LocalRoutes.LocalAggregates.Aggregate()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.aggregate.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "aggregate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.config is not None and self.config.has_data()) or
            (self.local_aggregates is not None and self.local_aggregates.has_data()) or
            (self.state is not None and self.state.has_data()) or
            (self.static_routes is not None and self.static_routes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.config is not None and self.config.has_operation()) or
            (self.local_aggregates is not None and self.local_aggregates.has_operation()) or
            (self.state is not None and self.state.has_operation()) or
            (self.static_routes is not None and self.static_routes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-local-routing:local-routes" + path_buffer

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

        if (child_yang_name == "config"):
            if (self.config is None):
                self.config = LocalRoutes.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
            return self.config

        if (child_yang_name == "local-aggregates"):
            if (self.local_aggregates is None):
                self.local_aggregates = LocalRoutes.LocalAggregates()
                self.local_aggregates.parent = self
                self._children_name_map["local_aggregates"] = "local-aggregates"
            return self.local_aggregates

        if (child_yang_name == "state"):
            if (self.state is None):
                self.state = LocalRoutes.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
            return self.state

        if (child_yang_name == "static-routes"):
            if (self.static_routes is None):
                self.static_routes = LocalRoutes.StaticRoutes()
                self.static_routes.parent = self
                self._children_name_map["static_routes"] = "static-routes"
            return self.static_routes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "config" or name == "local-aggregates" or name == "state" or name == "static-routes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = LocalRoutes()
        return self._top_entity

class Drop(Identity):
    """
    Discard traffic for the corresponding destination
    
    

    """

    _prefix = 'oc-loc-rt'
    _revision = '2016-05-11'

    def __init__(self):
        super(Drop, self).__init__("http://openconfig.net/yang/local-routing", "openconfig-local-routing", "openconfig-local-routing:DROP")


class Local_Link(Identity):
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
        super(Local_Link, self).__init__("http://openconfig.net/yang/local-routing", "openconfig-local-routing", "openconfig-local-routing:LOCAL_LINK")


