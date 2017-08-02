""" openconfig_routing_policy 

This module describes a YANG model for routing policy
configuration. It is a limited subset of all of the policy
configuration parameters available in the variety of vendor
implementations, but supports widely used constructs for managing
how routes are imported, exported, and modified across different
routing protocols.  This module is intended to be used in
conjunction with routing protocol configuration models (e.g.,
BGP) defined in other modules.

Route policy expression\:

Policies are expressed as a set of top\-level policy definitions,
each of which consists of a sequence of policy statements. Policy
statements consist of simple condition\-action tuples. Conditions
may include mutiple match or comparison operations, and similarly
actions may be multitude of changes to route attributes or a
final disposition of accepting or rejecting the route.

Route policy evaluation\:

Policy definitions are referenced in routing protocol
configurations using import and export configuration statements.
The arguments are members of an ordered list of named policy
definitions which comprise a policy chain, and optionally, an
explicit default policy action (i.e., reject or accept).

Evaluation of each policy definition proceeds by evaluating its
corresponding individual policy statements in order.  When a
condition statement in a policy statement is satisfied, the
corresponding action statement is executed.  If the action
statement has either accept\-route or reject\-route actions, policy
evaluation of the current policy definition stops, and no further
policy definitions in the chain are evaluated.

If the condition is not satisfied, then evaluation proceeds to
the next policy statement.  If none of the policy statement
conditions are satisfied, then evaluation of the current policy
definition stops, and the next policy definition in the chain is
evaluated.  When the end of the policy chain is reached, the
default route disposition action is performed (i.e., reject\-route
unless an an alternate default action is specified for the
chain).

Policy 'subroutines' (or nested policies) are supported by
allowing policy statement conditions to reference another policy
definition which applies conditions and actions from the
referenced policy before returning to the calling policy
statement and resuming evaluation.  If the called policy
results in an accept\-route (either explicit or by default), then
the subroutine returns an effective true value to the calling
policy.  Similarly, a reject\-route action returns false.  If the
subroutine returns true, the calling policy continues to evaluate
the remaining conditions (using a modified route if the
subroutine performed any changes to the route).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DefaultPolicyType(Enum):
    """
    DefaultPolicyType

    type used to specify default route disposition in

    a policy chain

    .. data:: ACCEPT_ROUTE = 0

    	default policy to accept the route

    .. data:: REJECT_ROUTE = 1

    	default policy to reject the route

    """

    ACCEPT_ROUTE = Enum.YLeaf(0, "ACCEPT_ROUTE")

    REJECT_ROUTE = Enum.YLeaf(1, "REJECT_ROUTE")



class RoutingPolicy(Entity):
    """
    Top\-level container for all routing policy configuration
    
    .. attribute:: defined_sets
    
    	Predefined sets of attributes used in policy match statements
    	**type**\:   :py:class:`DefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets>`
    
    .. attribute:: policy_definitions
    
    	Enclosing container for the list of top\-level policy  definitions
    	**type**\:   :py:class:`PolicyDefinitions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions>`
    
    

    """

    _prefix = 'oc-rpol'
    _revision = '2016-05-12'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "openconfig-routing-policy"

        self.defined_sets = RoutingPolicy.DefinedSets()
        self.defined_sets.parent = self
        self._children_name_map["defined_sets"] = "defined-sets"
        self._children_yang_names.add("defined-sets")

        self.policy_definitions = RoutingPolicy.PolicyDefinitions()
        self.policy_definitions.parent = self
        self._children_name_map["policy_definitions"] = "policy-definitions"
        self._children_yang_names.add("policy-definitions")


    class DefinedSets(Entity):
        """
        Predefined sets of attributes used in policy match
        statements
        
        .. attribute:: bgp_defined_sets
        
        	BGP\-related set definitions for policy match conditions
        	**type**\:   :py:class:`BgpDefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets>`
        
        .. attribute:: neighbor_sets
        
        	Enclosing container for the list of neighbor set definitions
        	**type**\:   :py:class:`NeighborSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets>`
        
        .. attribute:: prefix_sets
        
        	Enclosing container 
        	**type**\:   :py:class:`PrefixSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets>`
        
        .. attribute:: tag_sets
        
        	Enclosing container for the list of tag sets
        	**type**\:   :py:class:`TagSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets>`
        
        

        """

        _prefix = 'oc-rpol'
        _revision = '2016-05-12'

        def __init__(self):
            super(RoutingPolicy.DefinedSets, self).__init__()

            self.yang_name = "defined-sets"
            self.yang_parent_name = "routing-policy"

            self.bgp_defined_sets = RoutingPolicy.DefinedSets.BgpDefinedSets()
            self.bgp_defined_sets.parent = self
            self._children_name_map["bgp_defined_sets"] = "bgp-defined-sets"
            self._children_yang_names.add("bgp-defined-sets")

            self.neighbor_sets = RoutingPolicy.DefinedSets.NeighborSets()
            self.neighbor_sets.parent = self
            self._children_name_map["neighbor_sets"] = "neighbor-sets"
            self._children_yang_names.add("neighbor-sets")

            self.prefix_sets = RoutingPolicy.DefinedSets.PrefixSets()
            self.prefix_sets.parent = self
            self._children_name_map["prefix_sets"] = "prefix-sets"
            self._children_yang_names.add("prefix-sets")

            self.tag_sets = RoutingPolicy.DefinedSets.TagSets()
            self.tag_sets.parent = self
            self._children_name_map["tag_sets"] = "tag-sets"
            self._children_yang_names.add("tag-sets")


        class TagSets(Entity):
            """
            Enclosing container for the list of tag sets.
            
            .. attribute:: tag_set
            
            	List of tag set definitions
            	**type**\: list of    :py:class:`TagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.TagSets, self).__init__()

                self.yang_name = "tag-sets"
                self.yang_parent_name = "defined-sets"

                self.tag_set = YList(self)

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
                            super(RoutingPolicy.DefinedSets.TagSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.DefinedSets.TagSets, self).__setattr__(name, value)


            class TagSet(Entity):
                """
                List of tag set definitions.
                
                .. attribute:: tag_set_name  <key>
                
                	Reference to the tag set name list key
                	**type**\:  str
                
                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for tag sets
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Config>`
                
                .. attribute:: state
                
                	Operational state data for tag sets
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.State>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.TagSets.TagSet, self).__init__()

                    self.yang_name = "tag-set"
                    self.yang_parent_name = "tag-sets"

                    self.tag_set_name = YLeaf(YType.str, "tag-set-name")

                    self.config = RoutingPolicy.DefinedSets.TagSets.TagSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = RoutingPolicy.DefinedSets.TagSets.TagSet.State()
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
                        if name in ("tag_set_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.DefinedSets.TagSets.TagSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.TagSets.TagSet, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Configuration data for tag sets
                    
                    .. attribute:: tag_set_name
                    
                    	name / label of the tag set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    .. attribute:: tag_value
                    
                    	Value of the tag set member
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.TagSets.TagSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "tag-set"

                        self.tag_set_name = YLeaf(YType.str, "tag-set-name")

                        self.tag_value = YLeafList(YType.str, "tag-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tag_set_name",
                                        "tag_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.TagSets.TagSet.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.TagSets.TagSet.Config, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.tag_value.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.tag_set_name.is_set

                    def has_operation(self):
                        for leaf in self.tag_value.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tag_set_name.yfilter != YFilter.not_set or
                            self.tag_value.yfilter != YFilter.not_set)

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
                        if (self.tag_set_name.is_set or self.tag_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag_set_name.get_name_leafdata())

                        leaf_name_data.extend(self.tag_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tag-set-name" or name == "tag-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tag-set-name"):
                            self.tag_set_name = value
                            self.tag_set_name.value_namespace = name_space
                            self.tag_set_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag-value"):
                            self.tag_value.append(value)


                class State(Entity):
                    """
                    Operational state data for tag sets
                    
                    .. attribute:: tag_set_name
                    
                    	name / label of the tag set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    .. attribute:: tag_value
                    
                    	Value of the tag set member
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.TagSets.TagSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "tag-set"

                        self.tag_set_name = YLeaf(YType.str, "tag-set-name")

                        self.tag_value = YLeafList(YType.str, "tag-value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tag_set_name",
                                        "tag_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.TagSets.TagSet.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.TagSets.TagSet.State, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.tag_value.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.tag_set_name.is_set

                    def has_operation(self):
                        for leaf in self.tag_value.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tag_set_name.yfilter != YFilter.not_set or
                            self.tag_value.yfilter != YFilter.not_set)

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
                        if (self.tag_set_name.is_set or self.tag_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tag_set_name.get_name_leafdata())

                        leaf_name_data.extend(self.tag_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tag-set-name" or name == "tag-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tag-set-name"):
                            self.tag_set_name = value
                            self.tag_set_name.value_namespace = name_space
                            self.tag_set_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "tag-value"):
                            self.tag_value.append(value)

                def has_data(self):
                    return (
                        self.tag_set_name.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.tag_set_name.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tag-set" + "[tag-set-name='" + self.tag_set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/tag-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.tag_set_name.is_set or self.tag_set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tag_set_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = RoutingPolicy.DefinedSets.TagSets.TagSet.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = RoutingPolicy.DefinedSets.TagSets.TagSet.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state" or name == "tag-set-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "tag-set-name"):
                        self.tag_set_name = value
                        self.tag_set_name.value_namespace = name_space
                        self.tag_set_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.tag_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.tag_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tag-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "tag-set"):
                    for c in self.tag_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.DefinedSets.TagSets.TagSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.tag_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tag-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class BgpDefinedSets(Entity):
            """
            BGP\-related set definitions for policy match conditions
            
            .. attribute:: as_path_sets
            
            	Enclosing container for list of define AS path sets
            	**type**\:   :py:class:`AsPathSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets>`
            
            .. attribute:: community_sets
            
            	Enclosing container for list of defined BGP community sets
            	**type**\:   :py:class:`CommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets>`
            
            .. attribute:: ext_community_sets
            
            	Enclosing container for list of extended BGP community sets
            	**type**\:   :py:class:`ExtCommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets>`
            
            

            """

            _prefix = 'oc-bgp-pol'
            _revision = '2016-06-21'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.BgpDefinedSets, self).__init__()

                self.yang_name = "bgp-defined-sets"
                self.yang_parent_name = "defined-sets"

                self.as_path_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets()
                self.as_path_sets.parent = self
                self._children_name_map["as_path_sets"] = "as-path-sets"
                self._children_yang_names.add("as-path-sets")

                self.community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets()
                self.community_sets.parent = self
                self._children_name_map["community_sets"] = "community-sets"
                self._children_yang_names.add("community-sets")

                self.ext_community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets()
                self.ext_community_sets.parent = self
                self._children_name_map["ext_community_sets"] = "ext-community-sets"
                self._children_yang_names.add("ext-community-sets")


            class AsPathSets(Entity):
                """
                Enclosing container for list of define AS path sets
                
                .. attribute:: as_path_set
                
                	List of defined AS path sets
                	**type**\: list of    :py:class:`AsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets, self).__init__()

                    self.yang_name = "as-path-sets"
                    self.yang_parent_name = "bgp-defined-sets"

                    self.as_path_set = YList(self)

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
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets, self).__setattr__(name, value)


                class AsPathSet(Entity):
                    """
                    List of defined AS path sets
                    
                    .. attribute:: as_path_set_name  <key>
                    
                    	Reference to list key
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for AS path sets
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for AS path sets
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet, self).__init__()

                        self.yang_name = "as-path-set"
                        self.yang_parent_name = "as-path-sets"

                        self.as_path_set_name = YLeaf(YType.str, "as-path-set-name")

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State()
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
                            if name in ("as_path_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for AS path sets
                        
                        .. attribute:: as_path_set_member
                        
                        	AS path expression \-\- list of ASes in the set
                        	**type**\:  list of str
                        
                        .. attribute:: as_path_set_name
                        
                        	name of the AS path set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "as-path-set"

                            self.as_path_set_member = YLeafList(YType.str, "as-path-set-member")

                            self.as_path_set_name = YLeaf(YType.str, "as-path-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("as_path_set_member",
                                            "as_path_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.as_path_set_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.as_path_set_name.is_set

                        def has_operation(self):
                            for leaf in self.as_path_set_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.as_path_set_member.yfilter != YFilter.not_set or
                                self.as_path_set_name.yfilter != YFilter.not_set)

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
                            if (self.as_path_set_name.is_set or self.as_path_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_path_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.as_path_set_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "as-path-set-member" or name == "as-path-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "as-path-set-member"):
                                self.as_path_set_member.append(value)
                            if(value_path == "as-path-set-name"):
                                self.as_path_set_name = value
                                self.as_path_set_name.value_namespace = name_space
                                self.as_path_set_name.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for AS path sets
                        
                        .. attribute:: as_path_set_member
                        
                        	AS path expression \-\- list of ASes in the set
                        	**type**\:  list of str
                        
                        .. attribute:: as_path_set_name
                        
                        	name of the AS path set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "as-path-set"

                            self.as_path_set_member = YLeafList(YType.str, "as-path-set-member")

                            self.as_path_set_name = YLeaf(YType.str, "as-path-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("as_path_set_member",
                                            "as_path_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.as_path_set_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.as_path_set_name.is_set

                        def has_operation(self):
                            for leaf in self.as_path_set_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.as_path_set_member.yfilter != YFilter.not_set or
                                self.as_path_set_name.yfilter != YFilter.not_set)

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
                            if (self.as_path_set_name.is_set or self.as_path_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.as_path_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.as_path_set_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "as-path-set-member" or name == "as-path-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "as-path-set-member"):
                                self.as_path_set_member.append(value)
                            if(value_path == "as-path-set-name"):
                                self.as_path_set_name = value
                                self.as_path_set_name.value_namespace = name_space
                                self.as_path_set_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.as_path_set_name.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.as_path_set_name.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "as-path-set" + "[as-path-set-name='" + self.as_path_set_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/as-path-sets/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.as_path_set_name.is_set or self.as_path_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.as_path_set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "as-path-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "as-path-set-name"):
                            self.as_path_set_name = value
                            self.as_path_set_name.value_namespace = name_space
                            self.as_path_set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.as_path_set:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.as_path_set:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "as-path-sets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "as-path-set"):
                        for c in self.as_path_set:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.as_path_set.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "as-path-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class CommunitySets(Entity):
                """
                Enclosing container for list of defined BGP community sets
                
                .. attribute:: community_set
                
                	List of defined BGP community sets
                	**type**\: list of    :py:class:`CommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets, self).__init__()

                    self.yang_name = "community-sets"
                    self.yang_parent_name = "bgp-defined-sets"

                    self.community_set = YList(self)

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
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets, self).__setattr__(name, value)


                class CommunitySet(Entity):
                    """
                    List of defined BGP community sets
                    
                    .. attribute:: community_set_name  <key>
                    
                    	Reference to list key
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for BGP community sets
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for BGP community sets
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet, self).__init__()

                        self.yang_name = "community-set"
                        self.yang_parent_name = "community-sets"

                        self.community_set_name = YLeaf(YType.str, "community-set-name")

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State()
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
                            if name in ("community_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for BGP community sets
                        
                        .. attribute:: community_member
                        
                        	members of the community set
                        	**type**\: one of the below types:
                        
                        	**type**\:  list of int
                        
                        	**range:** 65536..4294901759
                        
                        
                        ----
                        	**type**\:  list of str
                        
                        	**pattern:** ([0\-9]+\:[0\-9]+)
                        
                        
                        ----
                        
                        ----
                        	**type**\:  list of str
                        
                        
                        ----
                        	**type**\:  
                        		list of  
                        
                        
                        ----
                        .. attribute:: community_set_name
                        
                        	name / label of the community set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "community-set"

                            self.community_member = YLeafList(YType.str, "community-member")

                            self.community_set_name = YLeaf(YType.str, "community-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("community_member",
                                            "community_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.community_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.community_set_name.is_set

                        def has_operation(self):
                            for leaf in self.community_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.community_member.yfilter != YFilter.not_set or
                                self.community_set_name.yfilter != YFilter.not_set)

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
                            if (self.community_set_name.is_set or self.community_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.community_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.community_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "community-member" or name == "community-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "community-member"):
                                self.community_member.append(value)
                            if(value_path == "community-set-name"):
                                self.community_set_name = value
                                self.community_set_name.value_namespace = name_space
                                self.community_set_name.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for BGP community sets
                        
                        .. attribute:: community_member
                        
                        	members of the community set
                        	**type**\: one of the below types:
                        
                        	**type**\:  list of int
                        
                        	**range:** 65536..4294901759
                        
                        
                        ----
                        	**type**\:  list of str
                        
                        	**pattern:** ([0\-9]+\:[0\-9]+)
                        
                        
                        ----
                        
                        ----
                        	**type**\:  list of str
                        
                        
                        ----
                        	**type**\:  
                        		list of  
                        
                        
                        ----
                        .. attribute:: community_set_name
                        
                        	name / label of the community set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "community-set"

                            self.community_member = YLeafList(YType.str, "community-member")

                            self.community_set_name = YLeaf(YType.str, "community-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("community_member",
                                            "community_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.community_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.community_set_name.is_set

                        def has_operation(self):
                            for leaf in self.community_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.community_member.yfilter != YFilter.not_set or
                                self.community_set_name.yfilter != YFilter.not_set)

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
                            if (self.community_set_name.is_set or self.community_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.community_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.community_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "community-member" or name == "community-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "community-member"):
                                self.community_member.append(value)
                            if(value_path == "community-set-name"):
                                self.community_set_name = value
                                self.community_set_name.value_namespace = name_space
                                self.community_set_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.community_set_name.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.community_set_name.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "community-set" + "[community-set-name='" + self.community_set_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.community_set_name.is_set or self.community_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.community_set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "community-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "community-set-name"):
                            self.community_set_name = value
                            self.community_set_name.value_namespace = name_space
                            self.community_set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.community_set:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.community_set:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "community-sets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "community-set"):
                        for c in self.community_set:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.community_set.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "community-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ExtCommunitySets(Entity):
                """
                Enclosing container for list of extended BGP community
                sets
                
                .. attribute:: ext_community_set
                
                	List of defined extended BGP community sets
                	**type**\: list of    :py:class:`ExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets, self).__init__()

                    self.yang_name = "ext-community-sets"
                    self.yang_parent_name = "bgp-defined-sets"

                    self.ext_community_set = YList(self)

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
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets, self).__setattr__(name, value)


                class ExtCommunitySet(Entity):
                    """
                    List of defined extended BGP community sets
                    
                    .. attribute:: ext_community_set_name  <key>
                    
                    	Reference to list key
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for extended BGP community sets
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for extended BGP community sets
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet, self).__init__()

                        self.yang_name = "ext-community-set"
                        self.yang_parent_name = "ext-community-sets"

                        self.ext_community_set_name = YLeaf(YType.str, "ext-community-set-name")

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State()
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
                            if name in ("ext_community_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for extended BGP community sets
                        
                        .. attribute:: ext_community_member
                        
                        	members of the extended community set
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
                        
                        ----
                        	**type**\:  list of str
                        
                        
                        ----
                        .. attribute:: ext_community_set_name
                        
                        	name / label of the extended community set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ext-community-set"

                            self.ext_community_member = YLeafList(YType.str, "ext-community-member")

                            self.ext_community_set_name = YLeaf(YType.str, "ext-community-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ext_community_member",
                                            "ext_community_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.ext_community_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.ext_community_set_name.is_set

                        def has_operation(self):
                            for leaf in self.ext_community_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ext_community_member.yfilter != YFilter.not_set or
                                self.ext_community_set_name.yfilter != YFilter.not_set)

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
                            if (self.ext_community_set_name.is_set or self.ext_community_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ext_community_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.ext_community_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ext-community-member" or name == "ext-community-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ext-community-member"):
                                self.ext_community_member.append(value)
                            if(value_path == "ext-community-set-name"):
                                self.ext_community_set_name = value
                                self.ext_community_set_name.value_namespace = name_space
                                self.ext_community_set_name.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for extended BGP community sets
                        
                        .. attribute:: ext_community_member
                        
                        	members of the extended community set
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
                        
                        ----
                        	**type**\:  list of str
                        
                        
                        ----
                        .. attribute:: ext_community_set_name
                        
                        	name / label of the extended community set \-\- this is used to reference the set in match conditions
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ext-community-set"

                            self.ext_community_member = YLeafList(YType.str, "ext-community-member")

                            self.ext_community_set_name = YLeaf(YType.str, "ext-community-set-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ext_community_member",
                                            "ext_community_set_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State, self).__setattr__(name, value)

                        def has_data(self):
                            for leaf in self.ext_community_member.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return self.ext_community_set_name.is_set

                        def has_operation(self):
                            for leaf in self.ext_community_member.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ext_community_member.yfilter != YFilter.not_set or
                                self.ext_community_set_name.yfilter != YFilter.not_set)

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
                            if (self.ext_community_set_name.is_set or self.ext_community_set_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ext_community_set_name.get_name_leafdata())

                            leaf_name_data.extend(self.ext_community_member.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ext-community-member" or name == "ext-community-set-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ext-community-member"):
                                self.ext_community_member.append(value)
                            if(value_path == "ext-community-set-name"):
                                self.ext_community_set_name = value
                                self.ext_community_set_name.value_namespace = name_space
                                self.ext_community_set_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.ext_community_set_name.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ext_community_set_name.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ext-community-set" + "[ext-community-set-name='" + self.ext_community_set_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ext_community_set_name.is_set or self.ext_community_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ext_community_set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "ext-community-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ext-community-set-name"):
                            self.ext_community_set_name = value
                            self.ext_community_set_name.value_namespace = name_space
                            self.ext_community_set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ext_community_set:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ext_community_set:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ext-community-sets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ext-community-set"):
                        for c in self.ext_community_set:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ext_community_set.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ext-community-set"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.as_path_sets is not None and self.as_path_sets.has_data()) or
                    (self.community_sets is not None and self.community_sets.has_data()) or
                    (self.ext_community_sets is not None and self.ext_community_sets.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.as_path_sets is not None and self.as_path_sets.has_operation()) or
                    (self.community_sets is not None and self.community_sets.has_operation()) or
                    (self.ext_community_sets is not None and self.ext_community_sets.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "openconfig-bgp-policy:bgp-defined-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "as-path-sets"):
                    if (self.as_path_sets is None):
                        self.as_path_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets()
                        self.as_path_sets.parent = self
                        self._children_name_map["as_path_sets"] = "as-path-sets"
                    return self.as_path_sets

                if (child_yang_name == "community-sets"):
                    if (self.community_sets is None):
                        self.community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets()
                        self.community_sets.parent = self
                        self._children_name_map["community_sets"] = "community-sets"
                    return self.community_sets

                if (child_yang_name == "ext-community-sets"):
                    if (self.ext_community_sets is None):
                        self.ext_community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets()
                        self.ext_community_sets.parent = self
                        self._children_name_map["ext_community_sets"] = "ext-community-sets"
                    return self.ext_community_sets

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "as-path-sets" or name == "community-sets" or name == "ext-community-sets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NeighborSets(Entity):
            """
            Enclosing container for the list of neighbor set
            definitions
            
            .. attribute:: neighbor_set
            
            	List of defined neighbor sets for use in policies
            	**type**\: list of    :py:class:`NeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.NeighborSets, self).__init__()

                self.yang_name = "neighbor-sets"
                self.yang_parent_name = "defined-sets"

                self.neighbor_set = YList(self)

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
                            super(RoutingPolicy.DefinedSets.NeighborSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.DefinedSets.NeighborSets, self).__setattr__(name, value)


            class NeighborSet(Entity):
                """
                List of defined neighbor sets for use in policies.
                
                .. attribute:: neighbor_set_name  <key>
                
                	Reference to the neighbor set name list key
                	**type**\:  str
                
                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for neighbor sets
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config>`
                
                .. attribute:: state
                
                	Operational state data for neighbor sets
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet, self).__init__()

                    self.yang_name = "neighbor-set"
                    self.yang_parent_name = "neighbor-sets"

                    self.neighbor_set_name = YLeaf(YType.str, "neighbor-set-name")

                    self.config = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State()
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
                        if name in ("neighbor_set_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Configuration data for neighbor sets.
                    
                    .. attribute:: address
                    
                    	List of IP addresses in the neighbor set
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: neighbor_set_name
                    
                    	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "neighbor-set"

                        self.address = YLeafList(YType.str, "address")

                        self.neighbor_set_name = YLeaf(YType.str, "neighbor-set-name")

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
                                        "neighbor_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.neighbor_set_name.is_set

                    def has_operation(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.neighbor_set_name.yfilter != YFilter.not_set)

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
                        if (self.neighbor_set_name.is_set or self.neighbor_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_set_name.get_name_leafdata())

                        leaf_name_data.extend(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "neighbor-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address.append(value)
                        if(value_path == "neighbor-set-name"):
                            self.neighbor_set_name = value
                            self.neighbor_set_name.value_namespace = name_space
                            self.neighbor_set_name.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    Operational state data for neighbor sets.
                    
                    .. attribute:: address
                    
                    	List of IP addresses in the neighbor set
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: neighbor_set_name
                    
                    	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "neighbor-set"

                        self.address = YLeafList(YType.str, "address")

                        self.neighbor_set_name = YLeaf(YType.str, "neighbor-set-name")

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
                                        "neighbor_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return self.neighbor_set_name.is_set

                    def has_operation(self):
                        for leaf in self.address.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.neighbor_set_name.yfilter != YFilter.not_set)

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
                        if (self.neighbor_set_name.is_set or self.neighbor_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.neighbor_set_name.get_name_leafdata())

                        leaf_name_data.extend(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "neighbor-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address.append(value)
                        if(value_path == "neighbor-set-name"):
                            self.neighbor_set_name = value
                            self.neighbor_set_name.value_namespace = name_space
                            self.neighbor_set_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.neighbor_set_name.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.neighbor_set_name.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor-set" + "[neighbor-set-name='" + self.neighbor_set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.neighbor_set_name.is_set or self.neighbor_set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.neighbor_set_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state" or name == "neighbor-set-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "neighbor-set-name"):
                        self.neighbor_set_name = value
                        self.neighbor_set_name.value_namespace = name_space
                        self.neighbor_set_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.neighbor_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.neighbor_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbor-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "neighbor-set"):
                    for c in self.neighbor_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "neighbor-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PrefixSets(Entity):
            """
            Enclosing container 
            
            .. attribute:: prefix_set
            
            	List of the defined prefix sets
            	**type**\: list of    :py:class:`PrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.PrefixSets, self).__init__()

                self.yang_name = "prefix-sets"
                self.yang_parent_name = "defined-sets"

                self.prefix_set = YList(self)

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
                            super(RoutingPolicy.DefinedSets.PrefixSets, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.DefinedSets.PrefixSets, self).__setattr__(name, value)


            class PrefixSet(Entity):
                """
                List of the defined prefix sets
                
                .. attribute:: prefix_set_name  <key>
                
                	Reference to prefix name list key
                	**type**\:  str
                
                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for prefix sets
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config>`
                
                .. attribute:: prefixes
                
                	Enclosing container for the list of prefixes in a policy prefix list
                	**type**\:   :py:class:`Prefixes <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes>`
                
                .. attribute:: state
                
                	Operational state data 
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet, self).__init__()

                    self.yang_name = "prefix-set"
                    self.yang_parent_name = "prefix-sets"

                    self.prefix_set_name = YLeaf(YType.str, "prefix-set-name")

                    self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.prefixes = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                    self._children_yang_names.add("prefixes")

                    self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State()
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
                        if name in ("prefix_set_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Configuration data for prefix sets
                    
                    .. attribute:: prefix_set_name
                    
                    	name / label of the prefix set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "prefix-set"

                        self.prefix_set_name = YLeaf(YType.str, "prefix-set-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return self.prefix_set_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix_set_name.yfilter != YFilter.not_set)

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
                        if (self.prefix_set_name.is_set or self.prefix_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix-set-name"):
                            self.prefix_set_name = value
                            self.prefix_set_name.value_namespace = name_space
                            self.prefix_set_name.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    Operational state data 
                    
                    .. attribute:: prefix_set_name
                    
                    	name / label of the prefix set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "prefix-set"

                        self.prefix_set_name = YLeaf(YType.str, "prefix-set-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("prefix_set_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State, self).__setattr__(name, value)

                    def has_data(self):
                        return self.prefix_set_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix_set_name.yfilter != YFilter.not_set)

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
                        if (self.prefix_set_name.is_set or self.prefix_set_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_set_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix-set-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix-set-name"):
                            self.prefix_set_name = value
                            self.prefix_set_name.value_namespace = name_space
                            self.prefix_set_name.value_namespace_prefix = name_space_prefix


                class Prefixes(Entity):
                    """
                    Enclosing container for the list of prefixes in a policy
                    prefix list
                    
                    .. attribute:: prefix
                    
                    	List of prefixes in the prefix set
                    	**type**\: list of    :py:class:`Prefix <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes, self).__init__()

                        self.yang_name = "prefixes"
                        self.yang_parent_name = "prefix-set"

                        self.prefix = YList(self)

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
                                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes, self).__setattr__(name, value)


                    class Prefix(Entity):
                        """
                        List of prefixes in the prefix set
                        
                        .. attribute:: ip_prefix  <key>
                        
                        	Reference to the ip\-prefix list key
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        
                        ----
                        .. attribute:: masklength_range  <key>
                        
                        	Reference to the masklength\-range list key
                        	**type**\:  str
                        
                        	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                        
                        	**refers to**\:  :py:class:`masklength_range <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for prefix definition
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for prefix definition
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefixes"

                            self.ip_prefix = YLeaf(YType.str, "ip-prefix")

                            self.masklength_range = YLeaf(YType.str, "masklength-range")

                            self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State()
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
                                if name in ("ip_prefix",
                                            "masklength_range") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration data for prefix definition
                            
                            .. attribute:: ip_prefix
                            
                            	The prefix member in CIDR notation \-\- while the prefix may be either IPv4 or IPv6, most implementations require all members of the prefix set to be the same address family.  Mixing address types in the same prefix set is likely to cause an error
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            .. attribute:: masklength_range
                            
                            	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                            	**type**\:  str
                            
                            	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix"

                                self.ip_prefix = YLeaf(YType.str, "ip-prefix")

                                self.masklength_range = YLeaf(YType.str, "masklength-range")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_prefix",
                                                "masklength_range") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ip_prefix.is_set or
                                    self.masklength_range.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_prefix.yfilter != YFilter.not_set or
                                    self.masklength_range.yfilter != YFilter.not_set)

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
                                if (self.ip_prefix.is_set or self.ip_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_prefix.get_name_leafdata())
                                if (self.masklength_range.is_set or self.masklength_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.masklength_range.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-prefix" or name == "masklength-range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-prefix"):
                                    self.ip_prefix = value
                                    self.ip_prefix.value_namespace = name_space
                                    self.ip_prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "masklength-range"):
                                    self.masklength_range = value
                                    self.masklength_range.value_namespace = name_space
                                    self.masklength_range.value_namespace_prefix = name_space_prefix


                        class State(Entity):
                            """
                            Operational state data for prefix definition
                            
                            .. attribute:: ip_prefix
                            
                            	The prefix member in CIDR notation \-\- while the prefix may be either IPv4 or IPv6, most implementations require all members of the prefix set to be the same address family.  Mixing address types in the same prefix set is likely to cause an error
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            .. attribute:: masklength_range
                            
                            	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                            	**type**\:  str
                            
                            	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix"

                                self.ip_prefix = YLeaf(YType.str, "ip-prefix")

                                self.masklength_range = YLeaf(YType.str, "masklength-range")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_prefix",
                                                "masklength_range") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ip_prefix.is_set or
                                    self.masklength_range.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_prefix.yfilter != YFilter.not_set or
                                    self.masklength_range.yfilter != YFilter.not_set)

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
                                if (self.ip_prefix.is_set or self.ip_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_prefix.get_name_leafdata())
                                if (self.masklength_range.is_set or self.masklength_range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.masklength_range.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-prefix" or name == "masklength-range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-prefix"):
                                    self.ip_prefix = value
                                    self.ip_prefix.value_namespace = name_space
                                    self.ip_prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "masklength-range"):
                                    self.masklength_range = value
                                    self.masklength_range.value_namespace = name_space
                                    self.masklength_range.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.ip_prefix.is_set or
                                self.masklength_range.is_set or
                                (self.config is not None and self.config.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_prefix.yfilter != YFilter.not_set or
                                self.masklength_range.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prefix" + "[ip-prefix='" + self.ip_prefix.get() + "']" + "[masklength-range='" + self.masklength_range.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_prefix.is_set or self.ip_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_prefix.get_name_leafdata())
                            if (self.masklength_range.is_set or self.masklength_range.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.masklength_range.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "config" or name == "state" or name == "ip-prefix" or name == "masklength-range"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-prefix"):
                                self.ip_prefix = value
                                self.ip_prefix.value_namespace = name_space
                                self.ip_prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "masklength-range"):
                                self.masklength_range = value
                                self.masklength_range.value_namespace = name_space
                                self.masklength_range.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prefix:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prefix:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefixes" + path_buffer

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

                        if (child_yang_name == "prefix"):
                            for c in self.prefix:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prefix.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.prefix_set_name.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.prefixes is not None and self.prefixes.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix_set_name.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.prefixes is not None and self.prefixes.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix-set" + "[prefix-set-name='" + self.prefix_set_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix_set_name.is_set or self.prefix_set_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_set_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "prefixes"):
                        if (self.prefixes is None):
                            self.prefixes = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"
                        return self.prefixes

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "prefixes" or name == "state" or name == "prefix-set-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix-set-name"):
                        self.prefix_set_name = value
                        self.prefix_set_name.value_namespace = name_space
                        self.prefix_set_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.prefix_set:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.prefix_set:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prefix-sets" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-routing-policy:routing-policy/defined-sets/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prefix-set"):
                    for c in self.prefix_set:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.prefix_set.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prefix-set"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.bgp_defined_sets is not None and self.bgp_defined_sets.has_data()) or
                (self.neighbor_sets is not None and self.neighbor_sets.has_data()) or
                (self.prefix_sets is not None and self.prefix_sets.has_data()) or
                (self.tag_sets is not None and self.tag_sets.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.bgp_defined_sets is not None and self.bgp_defined_sets.has_operation()) or
                (self.neighbor_sets is not None and self.neighbor_sets.has_operation()) or
                (self.prefix_sets is not None and self.prefix_sets.has_operation()) or
                (self.tag_sets is not None and self.tag_sets.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "defined-sets" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-routing-policy:routing-policy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgp-defined-sets"):
                if (self.bgp_defined_sets is None):
                    self.bgp_defined_sets = RoutingPolicy.DefinedSets.BgpDefinedSets()
                    self.bgp_defined_sets.parent = self
                    self._children_name_map["bgp_defined_sets"] = "bgp-defined-sets"
                return self.bgp_defined_sets

            if (child_yang_name == "neighbor-sets"):
                if (self.neighbor_sets is None):
                    self.neighbor_sets = RoutingPolicy.DefinedSets.NeighborSets()
                    self.neighbor_sets.parent = self
                    self._children_name_map["neighbor_sets"] = "neighbor-sets"
                return self.neighbor_sets

            if (child_yang_name == "prefix-sets"):
                if (self.prefix_sets is None):
                    self.prefix_sets = RoutingPolicy.DefinedSets.PrefixSets()
                    self.prefix_sets.parent = self
                    self._children_name_map["prefix_sets"] = "prefix-sets"
                return self.prefix_sets

            if (child_yang_name == "tag-sets"):
                if (self.tag_sets is None):
                    self.tag_sets = RoutingPolicy.DefinedSets.TagSets()
                    self.tag_sets.parent = self
                    self._children_name_map["tag_sets"] = "tag-sets"
                return self.tag_sets

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgp-defined-sets" or name == "neighbor-sets" or name == "prefix-sets" or name == "tag-sets"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class PolicyDefinitions(Entity):
        """
        Enclosing container for the list of top\-level policy
         definitions
        
        .. attribute:: policy_definition
        
        	List of top\-level policy definitions, keyed by unique name.  These policy definitions are expected to be referenced (by name) in policy chains specified in import or export configuration statements
        	**type**\: list of    :py:class:`PolicyDefinition <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
        
        

        """

        _prefix = 'oc-rpol'
        _revision = '2016-05-12'

        def __init__(self):
            super(RoutingPolicy.PolicyDefinitions, self).__init__()

            self.yang_name = "policy-definitions"
            self.yang_parent_name = "routing-policy"

            self.policy_definition = YList(self)

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
                        super(RoutingPolicy.PolicyDefinitions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RoutingPolicy.PolicyDefinitions, self).__setattr__(name, value)


        class PolicyDefinition(Entity):
            """
            List of top\-level policy definitions, keyed by unique
            name.  These policy definitions are expected to be
            referenced (by name) in policy chains specified in import
            or export configuration statements.
            
            .. attribute:: name  <key>
            
            	Reference to the list key
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config>`
            
            .. attribute:: config
            
            	Configuration data for policy defintions
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config>`
            
            .. attribute:: state
            
            	Operational state data for policy definitions
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.State>`
            
            .. attribute:: statements
            
            	Enclosing container for policy statements
            	**type**\:   :py:class:`Statements <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition, self).__init__()

                self.yang_name = "policy-definition"
                self.yang_parent_name = "policy-definitions"

                self.name = YLeaf(YType.str, "name")

                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.statements = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements()
                self.statements.parent = self
                self._children_name_map["statements"] = "statements"
                self._children_yang_names.add("statements")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition, self).__setattr__(name, value)


            class Config(Entity):
                """
                Configuration data for policy defintions
                
                .. attribute:: name
                
                	Name of the top\-level policy definition \-\- this name is used in references to the current policy
                	**type**\:  str
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "policy-definition"

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config, self).__setattr__(name, value)

                def has_data(self):
                    return self.name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

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
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Operational state data for policy definitions
                
                .. attribute:: name
                
                	Name of the top\-level policy definition \-\- this name is used in references to the current policy
                	**type**\:  str
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "policy-definition"

                    self.name = YLeaf(YType.str, "name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.State, self).__setattr__(name, value)

                def has_data(self):
                    return self.name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set)

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
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix


            class Statements(Entity):
                """
                Enclosing container for policy statements
                
                .. attribute:: statement
                
                	Policy statements group conditions and actions within a policy definition.  They are evaluated in the order specified (see the description of policy evaluation at the top of this module
                	**type**\: list of    :py:class:`Statement <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements, self).__init__()

                    self.yang_name = "statements"
                    self.yang_parent_name = "policy-definition"

                    self.statement = YList(self)

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
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements, self).__setattr__(name, value)


                class Statement(Entity):
                    """
                    Policy statements group conditions and actions
                    within a policy definition.  They are evaluated in
                    the order specified (see the description of policy
                    evaluation at the top of this module.
                    
                    .. attribute:: name  <key>
                    
                    	Reference to list key
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config>`
                    
                    .. attribute:: actions
                    
                    	Top\-level container for policy action statements
                    	**type**\:   :py:class:`Actions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions>`
                    
                    .. attribute:: conditions
                    
                    	Condition statements for the current policy statement
                    	**type**\:   :py:class:`Conditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions>`
                    
                    .. attribute:: config
                    
                    	Configuration data for policy statements
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for policy statements
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State>`
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement, self).__init__()

                        self.yang_name = "statement"
                        self.yang_parent_name = "statements"

                        self.name = YLeaf(YType.str, "name")

                        self.actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions()
                        self.actions.parent = self
                        self._children_name_map["actions"] = "actions"
                        self._children_yang_names.add("actions")

                        self.conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions()
                        self.conditions.parent = self
                        self._children_name_map["conditions"] = "conditions"
                        self._children_yang_names.add("conditions")

                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State()
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
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for policy statements
                        
                        .. attribute:: name
                        
                        	name of the policy statement
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "statement"

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return self.name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

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
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for policy statements
                        
                        .. attribute:: name
                        
                        	name of the policy statement
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "statement"

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State, self).__setattr__(name, value)

                        def has_data(self):
                            return self.name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

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
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix


                    class Conditions(Entity):
                        """
                        Condition statements for the current policy statement
                        
                        .. attribute:: bgp_conditions
                        
                        	Top\-level container 
                        	**type**\:   :py:class:`BgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions>`
                        
                        .. attribute:: config
                        
                        	Configuration data for policy conditions
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config>`
                        
                        .. attribute:: igp_conditions
                        
                        	Policy conditions for IGP attributes
                        	**type**\:   :py:class:`IgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions>`
                        
                        .. attribute:: match_interface
                        
                        	Top\-level container for interface match conditions
                        	**type**\:   :py:class:`MatchInterface <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface>`
                        
                        .. attribute:: match_neighbor_set
                        
                        	Match a referenced neighbor set according to the logic defined in the match\-set\-options\-leaf
                        	**type**\:   :py:class:`MatchNeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet>`
                        
                        .. attribute:: match_prefix_set
                        
                        	Match a referenced prefix\-set according to the logic defined in the match\-set\-options leaf
                        	**type**\:   :py:class:`MatchPrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet>`
                        
                        .. attribute:: match_tag_set
                        
                        	Match a referenced tag set according to the logic defined in the match\-options\-set leaf
                        	**type**\:   :py:class:`MatchTagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet>`
                        
                        .. attribute:: state
                        
                        	Operational state data for policy conditions
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions, self).__init__()

                            self.yang_name = "conditions"
                            self.yang_parent_name = "statement"

                            self.bgp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions()
                            self.bgp_conditions.parent = self
                            self._children_name_map["bgp_conditions"] = "bgp-conditions"
                            self._children_yang_names.add("bgp-conditions")

                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.igp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions()
                            self.igp_conditions.parent = self
                            self._children_name_map["igp_conditions"] = "igp-conditions"
                            self._children_yang_names.add("igp-conditions")

                            self.match_interface = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface()
                            self.match_interface.parent = self
                            self._children_name_map["match_interface"] = "match-interface"
                            self._children_yang_names.add("match-interface")

                            self.match_neighbor_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet()
                            self.match_neighbor_set.parent = self
                            self._children_name_map["match_neighbor_set"] = "match-neighbor-set"
                            self._children_yang_names.add("match-neighbor-set")

                            self.match_prefix_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet()
                            self.match_prefix_set.parent = self
                            self._children_name_map["match_prefix_set"] = "match-prefix-set"
                            self._children_yang_names.add("match-prefix-set")

                            self.match_tag_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet()
                            self.match_tag_set.parent = self
                            self._children_name_map["match_tag_set"] = "match-tag-set"
                            self._children_yang_names.add("match-tag-set")

                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")


                        class IgpConditions(Entity):
                            """
                            Policy conditions for IGP attributes
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions, self).__init__()

                                self.yang_name = "igp-conditions"
                                self.yang_parent_name = "conditions"

                            def has_data(self):
                                return False

                            def has_operation(self):
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "igp-conditions" + path_buffer

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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Config(Entity):
                            """
                            Configuration data for policy conditions
                            
                            .. attribute:: call_policy
                            
                            	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: install_protocol_eq
                            
                            	Condition to check the protocol / method used to install the route into the local routing table
                            	**type**\:   :py:class:`Install_Protocol_Type <ydk.models.openconfig.openconfig_policy_types.Install_Protocol_Type>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "conditions"

                                self.call_policy = YLeaf(YType.str, "call-policy")

                                self.install_protocol_eq = YLeaf(YType.identityref, "install-protocol-eq")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("call_policy",
                                                "install_protocol_eq") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.call_policy.is_set or
                                    self.install_protocol_eq.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.call_policy.yfilter != YFilter.not_set or
                                    self.install_protocol_eq.yfilter != YFilter.not_set)

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
                                if (self.call_policy.is_set or self.call_policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.call_policy.get_name_leafdata())
                                if (self.install_protocol_eq.is_set or self.install_protocol_eq.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.install_protocol_eq.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "call-policy" or name == "install-protocol-eq"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "call-policy"):
                                    self.call_policy = value
                                    self.call_policy.value_namespace = name_space
                                    self.call_policy.value_namespace_prefix = name_space_prefix
                                if(value_path == "install-protocol-eq"):
                                    self.install_protocol_eq = value
                                    self.install_protocol_eq.value_namespace = name_space
                                    self.install_protocol_eq.value_namespace_prefix = name_space_prefix


                        class BgpConditions(Entity):
                            """
                            Top\-level container 
                            
                            .. attribute:: as_path_length
                            
                            	Value and comparison operations for conditions based on the length of the AS path in the route update
                            	**type**\:   :py:class:`AsPathLength <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength>`
                            
                            .. attribute:: community_count
                            
                            	Value and comparison operations for conditions based on the number of communities in the route update
                            	**type**\:   :py:class:`CommunityCount <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount>`
                            
                            .. attribute:: config
                            
                            	Configuration data for BGP\-specific policy conditions
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config>`
                            
                            .. attribute:: match_as_path_set
                            
                            	Match a referenced as\-path set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchAsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet>`
                            
                            .. attribute:: match_community_set
                            
                            	Top\-level container for match conditions on communities. Match a referenced community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet>`
                            
                            .. attribute:: match_ext_community_set
                            
                            	Match a referenced extended community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet>`
                            
                            .. attribute:: state
                            
                            	Operational state data for BGP\-specific policy conditions
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp-pol'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions, self).__init__()

                                self.yang_name = "bgp-conditions"
                                self.yang_parent_name = "conditions"

                                self.as_path_length = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength()
                                self.as_path_length.parent = self
                                self._children_name_map["as_path_length"] = "as-path-length"
                                self._children_yang_names.add("as-path-length")

                                self.community_count = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount()
                                self.community_count.parent = self
                                self._children_name_map["community_count"] = "community-count"
                                self._children_yang_names.add("community-count")

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.match_as_path_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet()
                                self.match_as_path_set.parent = self
                                self._children_name_map["match_as_path_set"] = "match-as-path-set"
                                self._children_yang_names.add("match-as-path-set")

                                self.match_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet()
                                self.match_community_set.parent = self
                                self._children_name_map["match_community_set"] = "match-community-set"
                                self._children_yang_names.add("match-community-set")

                                self.match_ext_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet()
                                self.match_ext_community_set.parent = self
                                self._children_name_map["match_ext_community_set"] = "match-ext-community-set"
                                self._children_yang_names.add("match-ext-community-set")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class CommunityCount(Entity):
                                """
                                Value and comparison operations for conditions based on the
                                number of communities in the route update
                                
                                .. attribute:: config
                                
                                	Configuration data for community count condition
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for community count condition
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount, self).__init__()

                                    self.yang_name = "community-count"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for community count condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:   :py:class:`Attribute_Comparison <ydk.models.openconfig.openconfig_policy_types.Attribute_Comparison>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "community-count"

                                        self.operator = YLeaf(YType.identityref, "operator")

                                        self.value = YLeaf(YType.uint32, "value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("operator",
                                                        "value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.operator.is_set or
                                            self.value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.operator.yfilter != YFilter.not_set or
                                            self.value.yfilter != YFilter.not_set)

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
                                        if (self.operator.is_set or self.operator.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.operator.get_name_leafdata())
                                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "operator" or name == "value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "operator"):
                                            self.operator = value
                                            self.operator.value_namespace = name_space
                                            self.operator.value_namespace_prefix = name_space_prefix
                                        if(value_path == "value"):
                                            self.value = value
                                            self.value.value_namespace = name_space
                                            self.value.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for community count condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:   :py:class:`Attribute_Comparison <ydk.models.openconfig.openconfig_policy_types.Attribute_Comparison>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "community-count"

                                        self.operator = YLeaf(YType.identityref, "operator")

                                        self.value = YLeaf(YType.uint32, "value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("operator",
                                                        "value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.operator.is_set or
                                            self.value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.operator.yfilter != YFilter.not_set or
                                            self.value.yfilter != YFilter.not_set)

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
                                        if (self.operator.is_set or self.operator.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.operator.get_name_leafdata())
                                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "operator" or name == "value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "operator"):
                                            self.operator = value
                                            self.operator.value_namespace = name_space
                                            self.operator.value_namespace_prefix = name_space_prefix
                                        if(value_path == "value"):
                                            self.value = value
                                            self.value.value_namespace = name_space
                                            self.value.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "community-count" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State()
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


                            class MatchAsPathSet(Entity):
                                """
                                Match a referenced as\-path set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on AS path set
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for match conditions on AS path set
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet, self).__init__()

                                    self.yang_name = "match-as-path-set"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on AS path set
                                    
                                    .. attribute:: as_path_set
                                    
                                    	References a defined AS path set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-as-path-set"

                                        self.as_path_set = YLeaf(YType.str, "as-path-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("as_path_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.as_path_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.as_path_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.as_path_set.is_set or self.as_path_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_path_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "as-path-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "as-path-set"):
                                            self.as_path_set = value
                                            self.as_path_set.value_namespace = name_space
                                            self.as_path_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for match conditions on AS
                                    path set
                                    
                                    .. attribute:: as_path_set
                                    
                                    	References a defined AS path set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-as-path-set"

                                        self.as_path_set = YLeaf(YType.str, "as-path-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("as_path_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.as_path_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.as_path_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.as_path_set.is_set or self.as_path_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.as_path_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "as-path-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "as-path-set"):
                                            self.as_path_set = value
                                            self.as_path_set.value_namespace = name_space
                                            self.as_path_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "match-as-path-set" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State()
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


                            class AsPathLength(Entity):
                                """
                                Value and comparison operations for conditions based on the
                                length of the AS path in the route update
                                
                                .. attribute:: config
                                
                                	Configuration data for AS path length condition
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for AS path length condition
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength, self).__init__()

                                    self.yang_name = "as-path-length"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for AS path length condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:   :py:class:`Attribute_Comparison <ydk.models.openconfig.openconfig_policy_types.Attribute_Comparison>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "as-path-length"

                                        self.operator = YLeaf(YType.identityref, "operator")

                                        self.value = YLeaf(YType.uint32, "value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("operator",
                                                        "value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.operator.is_set or
                                            self.value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.operator.yfilter != YFilter.not_set or
                                            self.value.yfilter != YFilter.not_set)

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
                                        if (self.operator.is_set or self.operator.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.operator.get_name_leafdata())
                                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "operator" or name == "value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "operator"):
                                            self.operator = value
                                            self.operator.value_namespace = name_space
                                            self.operator.value_namespace_prefix = name_space_prefix
                                        if(value_path == "value"):
                                            self.value = value
                                            self.value.value_namespace = name_space
                                            self.value.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for AS path length condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:   :py:class:`Attribute_Comparison <ydk.models.openconfig.openconfig_policy_types.Attribute_Comparison>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "as-path-length"

                                        self.operator = YLeaf(YType.identityref, "operator")

                                        self.value = YLeaf(YType.uint32, "value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("operator",
                                                        "value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.operator.is_set or
                                            self.value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.operator.yfilter != YFilter.not_set or
                                            self.value.yfilter != YFilter.not_set)

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
                                        if (self.operator.is_set or self.operator.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.operator.get_name_leafdata())
                                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "operator" or name == "value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "operator"):
                                            self.operator = value
                                            self.operator.value_namespace = name_space
                                            self.operator.value_namespace_prefix = name_space_prefix
                                        if(value_path == "value"):
                                            self.value = value
                                            self.value.value_namespace = name_space
                                            self.value.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "as-path-length" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State()
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


                            class MatchCommunitySet(Entity):
                                """
                                Top\-level container for match conditions on communities.
                                Match a referenced community\-set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on communities
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data 
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet, self).__init__()

                                    self.yang_name = "match-community-set"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on communities
                                    
                                    .. attribute:: community_set
                                    
                                    	References a defined community set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-community-set"

                                        self.community_set = YLeaf(YType.str, "community-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("community_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.community_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.community_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.community_set.is_set or self.community_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.community_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "community-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "community-set"):
                                            self.community_set = value
                                            self.community_set.value_namespace = name_space
                                            self.community_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data 
                                    
                                    .. attribute:: community_set
                                    
                                    	References a defined community set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-community-set"

                                        self.community_set = YLeaf(YType.str, "community-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("community_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.community_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.community_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.community_set.is_set or self.community_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.community_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "community-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "community-set"):
                                            self.community_set = value
                                            self.community_set.value_namespace = name_space
                                            self.community_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "match-community-set" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State()
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


                            class Config(Entity):
                                """
                                Configuration data for BGP\-specific policy conditions
                                
                                .. attribute:: afi_safi_in
                                
                                	List of address families which the NLRI may be within
                                	**type**\:  
                                		list of  
                                
                                .. attribute:: local_pref_eq
                                
                                	Condition to check if the local pref attribute is equal to the specified value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med_eq
                                
                                	Condition to check if the received MED value is equal to the specified value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop_in
                                
                                	List of next hop addresses to check for in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: origin_eq
                                
                                	Condition to check if the route origin is equal to the specified value
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: route_type
                                
                                	Condition to check the route type in the route update
                                	**type**\:   :py:class:`RouteType <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config.RouteType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.afi_safi_in = YLeafList(YType.identityref, "afi-safi-in")

                                    self.local_pref_eq = YLeaf(YType.uint32, "local-pref-eq")

                                    self.med_eq = YLeaf(YType.uint32, "med-eq")

                                    self.next_hop_in = YLeafList(YType.str, "next-hop-in")

                                    self.origin_eq = YLeaf(YType.enumeration, "origin-eq")

                                    self.route_type = YLeaf(YType.enumeration, "route-type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi_safi_in",
                                                    "local_pref_eq",
                                                    "med_eq",
                                                    "next_hop_in",
                                                    "origin_eq",
                                                    "route_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config, self).__setattr__(name, value)

                                class RouteType(Enum):
                                    """
                                    RouteType

                                    Condition to check the route type in the route update

                                    .. data:: INTERNAL = 0

                                    	route type is internal

                                    .. data:: EXTERNAL = 1

                                    	route type is external

                                    """

                                    INTERNAL = Enum.YLeaf(0, "INTERNAL")

                                    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")


                                def has_data(self):
                                    for leaf in self.afi_safi_in.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    for leaf in self.next_hop_in.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.local_pref_eq.is_set or
                                        self.med_eq.is_set or
                                        self.origin_eq.is_set or
                                        self.route_type.is_set)

                                def has_operation(self):
                                    for leaf in self.afi_safi_in.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    for leaf in self.next_hop_in.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi_safi_in.yfilter != YFilter.not_set or
                                        self.local_pref_eq.yfilter != YFilter.not_set or
                                        self.med_eq.yfilter != YFilter.not_set or
                                        self.next_hop_in.yfilter != YFilter.not_set or
                                        self.origin_eq.yfilter != YFilter.not_set or
                                        self.route_type.yfilter != YFilter.not_set)

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
                                    if (self.local_pref_eq.is_set or self.local_pref_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_pref_eq.get_name_leafdata())
                                    if (self.med_eq.is_set or self.med_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.med_eq.get_name_leafdata())
                                    if (self.origin_eq.is_set or self.origin_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.origin_eq.get_name_leafdata())
                                    if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.route_type.get_name_leafdata())

                                    leaf_name_data.extend(self.afi_safi_in.get_name_leafdata())

                                    leaf_name_data.extend(self.next_hop_in.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "afi-safi-in" or name == "local-pref-eq" or name == "med-eq" or name == "next-hop-in" or name == "origin-eq" or name == "route-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi-safi-in"):
                                        identity = Identity(name_space, name_space_prefix, value)
                                        self.afi_safi_in.append(identity)
                                    if(value_path == "local-pref-eq"):
                                        self.local_pref_eq = value
                                        self.local_pref_eq.value_namespace = name_space
                                        self.local_pref_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "med-eq"):
                                        self.med_eq = value
                                        self.med_eq.value_namespace = name_space
                                        self.med_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop-in"):
                                        self.next_hop_in.append(value)
                                    if(value_path == "origin-eq"):
                                        self.origin_eq = value
                                        self.origin_eq.value_namespace = name_space
                                        self.origin_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "route-type"):
                                        self.route_type = value
                                        self.route_type.value_namespace = name_space
                                        self.route_type.value_namespace_prefix = name_space_prefix


                            class MatchExtCommunitySet(Entity):
                                """
                                Match a referenced extended community\-set according to the
                                logic defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on extended communities
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for match conditions on extended communities
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet, self).__init__()

                                    self.yang_name = "match-ext-community-set"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on extended
                                    communities
                                    
                                    .. attribute:: ext_community_set
                                    
                                    	References a defined extended community set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-ext-community-set"

                                        self.ext_community_set = YLeaf(YType.str, "ext-community-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ext_community_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.ext_community_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ext_community_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.ext_community_set.is_set or self.ext_community_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ext_community_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ext-community-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ext-community-set"):
                                            self.ext_community_set = value
                                            self.ext_community_set.value_namespace = name_space
                                            self.ext_community_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for match conditions on extended
                                    communities
                                    
                                    .. attribute:: ext_community_set
                                    
                                    	References a defined extended community set
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:   :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-ext-community-set"

                                        self.ext_community_set = YLeaf(YType.str, "ext-community-set")

                                        self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("ext_community_set",
                                                        "match_set_options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.ext_community_set.is_set or
                                            self.match_set_options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.ext_community_set.yfilter != YFilter.not_set or
                                            self.match_set_options.yfilter != YFilter.not_set)

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
                                        if (self.ext_community_set.is_set or self.ext_community_set.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ext_community_set.get_name_leafdata())
                                        if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.match_set_options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "ext-community-set" or name == "match-set-options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "ext-community-set"):
                                            self.ext_community_set = value
                                            self.ext_community_set.value_namespace = name_space
                                            self.ext_community_set.value_namespace_prefix = name_space_prefix
                                        if(value_path == "match-set-options"):
                                            self.match_set_options = value
                                            self.match_set_options.value_namespace = name_space
                                            self.match_set_options.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "match-ext-community-set" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State()
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


                            class State(Entity):
                                """
                                Operational state data for BGP\-specific policy
                                conditions
                                
                                .. attribute:: afi_safi_in
                                
                                	List of address families which the NLRI may be within
                                	**type**\:  
                                		list of  
                                
                                .. attribute:: local_pref_eq
                                
                                	Condition to check if the local pref attribute is equal to the specified value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: med_eq
                                
                                	Condition to check if the received MED value is equal to the specified value
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: next_hop_in
                                
                                	List of next hop addresses to check for in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: origin_eq
                                
                                	Condition to check if the route origin is equal to the specified value
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: route_type
                                
                                	Condition to check the route type in the route update
                                	**type**\:   :py:class:`RouteType <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State.RouteType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "bgp-conditions"

                                    self.afi_safi_in = YLeafList(YType.identityref, "afi-safi-in")

                                    self.local_pref_eq = YLeaf(YType.uint32, "local-pref-eq")

                                    self.med_eq = YLeaf(YType.uint32, "med-eq")

                                    self.next_hop_in = YLeafList(YType.str, "next-hop-in")

                                    self.origin_eq = YLeaf(YType.enumeration, "origin-eq")

                                    self.route_type = YLeaf(YType.enumeration, "route-type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi_safi_in",
                                                    "local_pref_eq",
                                                    "med_eq",
                                                    "next_hop_in",
                                                    "origin_eq",
                                                    "route_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State, self).__setattr__(name, value)

                                class RouteType(Enum):
                                    """
                                    RouteType

                                    Condition to check the route type in the route update

                                    .. data:: INTERNAL = 0

                                    	route type is internal

                                    .. data:: EXTERNAL = 1

                                    	route type is external

                                    """

                                    INTERNAL = Enum.YLeaf(0, "INTERNAL")

                                    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")


                                def has_data(self):
                                    for leaf in self.afi_safi_in.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    for leaf in self.next_hop_in.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.local_pref_eq.is_set or
                                        self.med_eq.is_set or
                                        self.origin_eq.is_set or
                                        self.route_type.is_set)

                                def has_operation(self):
                                    for leaf in self.afi_safi_in.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    for leaf in self.next_hop_in.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi_safi_in.yfilter != YFilter.not_set or
                                        self.local_pref_eq.yfilter != YFilter.not_set or
                                        self.med_eq.yfilter != YFilter.not_set or
                                        self.next_hop_in.yfilter != YFilter.not_set or
                                        self.origin_eq.yfilter != YFilter.not_set or
                                        self.route_type.yfilter != YFilter.not_set)

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
                                    if (self.local_pref_eq.is_set or self.local_pref_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_pref_eq.get_name_leafdata())
                                    if (self.med_eq.is_set or self.med_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.med_eq.get_name_leafdata())
                                    if (self.origin_eq.is_set or self.origin_eq.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.origin_eq.get_name_leafdata())
                                    if (self.route_type.is_set or self.route_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.route_type.get_name_leafdata())

                                    leaf_name_data.extend(self.afi_safi_in.get_name_leafdata())

                                    leaf_name_data.extend(self.next_hop_in.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "afi-safi-in" or name == "local-pref-eq" or name == "med-eq" or name == "next-hop-in" or name == "origin-eq" or name == "route-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi-safi-in"):
                                        identity = Identity(name_space, name_space_prefix, value)
                                        self.afi_safi_in.append(identity)
                                    if(value_path == "local-pref-eq"):
                                        self.local_pref_eq = value
                                        self.local_pref_eq.value_namespace = name_space
                                        self.local_pref_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "med-eq"):
                                        self.med_eq = value
                                        self.med_eq.value_namespace = name_space
                                        self.med_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop-in"):
                                        self.next_hop_in.append(value)
                                    if(value_path == "origin-eq"):
                                        self.origin_eq = value
                                        self.origin_eq.value_namespace = name_space
                                        self.origin_eq.value_namespace_prefix = name_space_prefix
                                    if(value_path == "route-type"):
                                        self.route_type = value
                                        self.route_type.value_namespace = name_space
                                        self.route_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    (self.as_path_length is not None and self.as_path_length.has_data()) or
                                    (self.community_count is not None and self.community_count.has_data()) or
                                    (self.config is not None and self.config.has_data()) or
                                    (self.match_as_path_set is not None and self.match_as_path_set.has_data()) or
                                    (self.match_community_set is not None and self.match_community_set.has_data()) or
                                    (self.match_ext_community_set is not None and self.match_ext_community_set.has_data()) or
                                    (self.state is not None and self.state.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.as_path_length is not None and self.as_path_length.has_operation()) or
                                    (self.community_count is not None and self.community_count.has_operation()) or
                                    (self.config is not None and self.config.has_operation()) or
                                    (self.match_as_path_set is not None and self.match_as_path_set.has_operation()) or
                                    (self.match_community_set is not None and self.match_community_set.has_operation()) or
                                    (self.match_ext_community_set is not None and self.match_ext_community_set.has_operation()) or
                                    (self.state is not None and self.state.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "openconfig-bgp-policy:bgp-conditions" + path_buffer

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

                                if (child_yang_name == "as-path-length"):
                                    if (self.as_path_length is None):
                                        self.as_path_length = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength()
                                        self.as_path_length.parent = self
                                        self._children_name_map["as_path_length"] = "as-path-length"
                                    return self.as_path_length

                                if (child_yang_name == "community-count"):
                                    if (self.community_count is None):
                                        self.community_count = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount()
                                        self.community_count.parent = self
                                        self._children_name_map["community_count"] = "community-count"
                                    return self.community_count

                                if (child_yang_name == "config"):
                                    if (self.config is None):
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "match-as-path-set"):
                                    if (self.match_as_path_set is None):
                                        self.match_as_path_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet()
                                        self.match_as_path_set.parent = self
                                        self._children_name_map["match_as_path_set"] = "match-as-path-set"
                                    return self.match_as_path_set

                                if (child_yang_name == "match-community-set"):
                                    if (self.match_community_set is None):
                                        self.match_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet()
                                        self.match_community_set.parent = self
                                        self._children_name_map["match_community_set"] = "match-community-set"
                                    return self.match_community_set

                                if (child_yang_name == "match-ext-community-set"):
                                    if (self.match_ext_community_set is None):
                                        self.match_ext_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet()
                                        self.match_ext_community_set.parent = self
                                        self._children_name_map["match_ext_community_set"] = "match-ext-community-set"
                                    return self.match_ext_community_set

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                    return self.state

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "as-path-length" or name == "community-count" or name == "config" or name == "match-as-path-set" or name == "match-community-set" or name == "match-ext-community-set" or name == "state"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class MatchPrefixSet(Entity):
                            """
                            Match a referenced prefix\-set according to the logic
                            defined in the match\-set\-options leaf
                            
                            .. attribute:: config
                            
                            	Configuration data for a prefix\-set condition
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for a prefix\-set condition
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet, self).__init__()

                                self.yang_name = "match-prefix-set"
                                self.yang_parent_name = "conditions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data for a prefix\-set condition
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: prefix_set
                                
                                	References a defined prefix set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-prefix-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.prefix_set = YLeaf(YType.str, "prefix-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "prefix_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.prefix_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.prefix_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.prefix_set.is_set or self.prefix_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "prefix-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-set"):
                                        self.prefix_set = value
                                        self.prefix_set.value_namespace = name_space
                                        self.prefix_set.value_namespace_prefix = name_space_prefix


                            class State(Entity):
                                """
                                Operational state data for a prefix\-set condition
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: prefix_set
                                
                                	References a defined prefix set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-prefix-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.prefix_set = YLeaf(YType.str, "prefix-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "prefix_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.prefix_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.prefix_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.prefix_set.is_set or self.prefix_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "prefix-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-set"):
                                        self.prefix_set = value
                                        self.prefix_set.value_namespace = name_space
                                        self.prefix_set.value_namespace_prefix = name_space_prefix

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
                                path_buffer = "match-prefix-set" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State()
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


                        class State(Entity):
                            """
                            Operational state data for policy conditions
                            
                            .. attribute:: call_policy
                            
                            	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: install_protocol_eq
                            
                            	Condition to check the protocol / method used to install the route into the local routing table
                            	**type**\:   :py:class:`Install_Protocol_Type <ydk.models.openconfig.openconfig_policy_types.Install_Protocol_Type>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "conditions"

                                self.call_policy = YLeaf(YType.str, "call-policy")

                                self.install_protocol_eq = YLeaf(YType.identityref, "install-protocol-eq")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("call_policy",
                                                "install_protocol_eq") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.call_policy.is_set or
                                    self.install_protocol_eq.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.call_policy.yfilter != YFilter.not_set or
                                    self.install_protocol_eq.yfilter != YFilter.not_set)

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
                                if (self.call_policy.is_set or self.call_policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.call_policy.get_name_leafdata())
                                if (self.install_protocol_eq.is_set or self.install_protocol_eq.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.install_protocol_eq.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "call-policy" or name == "install-protocol-eq"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "call-policy"):
                                    self.call_policy = value
                                    self.call_policy.value_namespace = name_space
                                    self.call_policy.value_namespace_prefix = name_space_prefix
                                if(value_path == "install-protocol-eq"):
                                    self.install_protocol_eq = value
                                    self.install_protocol_eq.value_namespace = name_space
                                    self.install_protocol_eq.value_namespace_prefix = name_space_prefix


                        class MatchNeighborSet(Entity):
                            """
                            Match a referenced neighbor set according to the logic
                            defined in the match\-set\-options\-leaf
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet, self).__init__()

                                self.yang_name = "match-neighbor-set"
                                self.yang_parent_name = "conditions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: neighbor_set
                                
                                	References a defined neighbor set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-neighbor-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.neighbor_set = YLeaf(YType.str, "neighbor-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "neighbor_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.neighbor_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.neighbor_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.neighbor_set.is_set or self.neighbor_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.neighbor_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "neighbor-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "neighbor-set"):
                                        self.neighbor_set = value
                                        self.neighbor_set.value_namespace = name_space
                                        self.neighbor_set.value_namespace_prefix = name_space_prefix


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: neighbor_set
                                
                                	References a defined neighbor set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-neighbor-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.neighbor_set = YLeaf(YType.str, "neighbor-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "neighbor_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.neighbor_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.neighbor_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.neighbor_set.is_set or self.neighbor_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.neighbor_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "neighbor-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "neighbor-set"):
                                        self.neighbor_set = value
                                        self.neighbor_set.value_namespace = name_space
                                        self.neighbor_set.value_namespace_prefix = name_space_prefix

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
                                path_buffer = "match-neighbor-set" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State()
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


                        class MatchTagSet(Entity):
                            """
                            Match a referenced tag set according to the logic defined
                            in the match\-options\-set leaf
                            
                            .. attribute:: config
                            
                            	Configuration data for tag\-set conditions
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data tag\-set conditions
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet, self).__init__()

                                self.yang_name = "match-tag-set"
                                self.yang_parent_name = "conditions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data for tag\-set conditions
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: tag_set
                                
                                	References a defined tag set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-tag-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.tag_set = YLeaf(YType.str, "tag-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "tag_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.tag_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.tag_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.tag_set.is_set or self.tag_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.tag_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "tag-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "tag-set"):
                                        self.tag_set = value
                                        self.tag_set.value_namespace = name_space
                                        self.tag_set.value_namespace_prefix = name_space_prefix


                            class State(Entity):
                                """
                                Operational state data tag\-set conditions
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:   :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                .. attribute:: tag_set
                                
                                	References a defined tag set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-tag-set"

                                    self.match_set_options = YLeaf(YType.enumeration, "match-set-options")

                                    self.tag_set = YLeaf(YType.str, "tag-set")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("match_set_options",
                                                    "tag_set") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.match_set_options.is_set or
                                        self.tag_set.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.match_set_options.yfilter != YFilter.not_set or
                                        self.tag_set.yfilter != YFilter.not_set)

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
                                    if (self.match_set_options.is_set or self.match_set_options.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.match_set_options.get_name_leafdata())
                                    if (self.tag_set.is_set or self.tag_set.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.tag_set.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match-set-options" or name == "tag-set"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "match-set-options"):
                                        self.match_set_options = value
                                        self.match_set_options.value_namespace = name_space
                                        self.match_set_options.value_namespace_prefix = name_space_prefix
                                    if(value_path == "tag-set"):
                                        self.tag_set = value
                                        self.tag_set.value_namespace = name_space
                                        self.tag_set.value_namespace_prefix = name_space_prefix

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
                                path_buffer = "match-tag-set" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State()
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


                        class MatchInterface(Entity):
                            """
                            Top\-level container for interface match conditions
                            
                            .. attribute:: config
                            
                            	Configuration data for interface match conditions
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for interface match conditions
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface, self).__init__()

                                self.yang_name = "match-interface"
                                self.yang_parent_name = "conditions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data for interface match conditions
                                
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

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-interface"

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
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config, self).__setattr__(name, value)

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
                                Operational state data for interface match conditions
                                
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

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-interface"

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
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State, self).__setattr__(name, value)

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
                                path_buffer = "match-interface" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State()
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
                                (self.bgp_conditions is not None and self.bgp_conditions.has_data()) or
                                (self.config is not None and self.config.has_data()) or
                                (self.igp_conditions is not None and self.igp_conditions.has_data()) or
                                (self.match_interface is not None and self.match_interface.has_data()) or
                                (self.match_neighbor_set is not None and self.match_neighbor_set.has_data()) or
                                (self.match_prefix_set is not None and self.match_prefix_set.has_data()) or
                                (self.match_tag_set is not None and self.match_tag_set.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bgp_conditions is not None and self.bgp_conditions.has_operation()) or
                                (self.config is not None and self.config.has_operation()) or
                                (self.igp_conditions is not None and self.igp_conditions.has_operation()) or
                                (self.match_interface is not None and self.match_interface.has_operation()) or
                                (self.match_neighbor_set is not None and self.match_neighbor_set.has_operation()) or
                                (self.match_prefix_set is not None and self.match_prefix_set.has_operation()) or
                                (self.match_tag_set is not None and self.match_tag_set.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "conditions" + path_buffer

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

                            if (child_yang_name == "bgp-conditions"):
                                if (self.bgp_conditions is None):
                                    self.bgp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions()
                                    self.bgp_conditions.parent = self
                                    self._children_name_map["bgp_conditions"] = "bgp-conditions"
                                return self.bgp_conditions

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "igp-conditions"):
                                if (self.igp_conditions is None):
                                    self.igp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions()
                                    self.igp_conditions.parent = self
                                    self._children_name_map["igp_conditions"] = "igp-conditions"
                                return self.igp_conditions

                            if (child_yang_name == "match-interface"):
                                if (self.match_interface is None):
                                    self.match_interface = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface()
                                    self.match_interface.parent = self
                                    self._children_name_map["match_interface"] = "match-interface"
                                return self.match_interface

                            if (child_yang_name == "match-neighbor-set"):
                                if (self.match_neighbor_set is None):
                                    self.match_neighbor_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet()
                                    self.match_neighbor_set.parent = self
                                    self._children_name_map["match_neighbor_set"] = "match-neighbor-set"
                                return self.match_neighbor_set

                            if (child_yang_name == "match-prefix-set"):
                                if (self.match_prefix_set is None):
                                    self.match_prefix_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet()
                                    self.match_prefix_set.parent = self
                                    self._children_name_map["match_prefix_set"] = "match-prefix-set"
                                return self.match_prefix_set

                            if (child_yang_name == "match-tag-set"):
                                if (self.match_tag_set is None):
                                    self.match_tag_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet()
                                    self.match_tag_set.parent = self
                                    self._children_name_map["match_tag_set"] = "match-tag-set"
                                return self.match_tag_set

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bgp-conditions" or name == "config" or name == "igp-conditions" or name == "match-interface" or name == "match-neighbor-set" or name == "match-prefix-set" or name == "match-tag-set" or name == "state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Actions(Entity):
                        """
                        Top\-level container for policy action statements
                        
                        .. attribute:: bgp_actions
                        
                        	Top\-level container for BGP\-specific actions
                        	**type**\:   :py:class:`BgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions>`
                        
                        .. attribute:: config
                        
                        	Configuration data for policy actions
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config>`
                        
                        .. attribute:: igp_actions
                        
                        	Actions to set IGP route attributes; these actions apply to multiple IGPs
                        	**type**\:   :py:class:`IgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions>`
                        
                        .. attribute:: state
                        
                        	Operational state data for policy actions
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions, self).__init__()

                            self.yang_name = "actions"
                            self.yang_parent_name = "statement"

                            self.bgp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions()
                            self.bgp_actions.parent = self
                            self._children_name_map["bgp_actions"] = "bgp-actions"
                            self._children_yang_names.add("bgp-actions")

                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.igp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions()
                            self.igp_actions.parent = self
                            self._children_name_map["igp_actions"] = "igp-actions"
                            self._children_yang_names.add("igp-actions")

                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")


                        class Config(Entity):
                            """
                            Configuration data for policy actions
                            
                            .. attribute:: accept_route
                            
                            	accepts the route into the routing table
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: reject_route
                            
                            	rejects the route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "actions"

                                self.accept_route = YLeaf(YType.empty, "accept-route")

                                self.reject_route = YLeaf(YType.empty, "reject-route")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accept_route",
                                                "reject_route") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accept_route.is_set or
                                    self.reject_route.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accept_route.yfilter != YFilter.not_set or
                                    self.reject_route.yfilter != YFilter.not_set)

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
                                if (self.accept_route.is_set or self.accept_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accept_route.get_name_leafdata())
                                if (self.reject_route.is_set or self.reject_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reject_route.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accept-route" or name == "reject-route"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accept-route"):
                                    self.accept_route = value
                                    self.accept_route.value_namespace = name_space
                                    self.accept_route.value_namespace_prefix = name_space_prefix
                                if(value_path == "reject-route"):
                                    self.reject_route = value
                                    self.reject_route.value_namespace = name_space
                                    self.reject_route.value_namespace_prefix = name_space_prefix


                        class State(Entity):
                            """
                            Operational state data for policy actions
                            
                            .. attribute:: accept_route
                            
                            	accepts the route into the routing table
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: reject_route
                            
                            	rejects the route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "actions"

                                self.accept_route = YLeaf(YType.empty, "accept-route")

                                self.reject_route = YLeaf(YType.empty, "reject-route")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("accept_route",
                                                "reject_route") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.accept_route.is_set or
                                    self.reject_route.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.accept_route.yfilter != YFilter.not_set or
                                    self.reject_route.yfilter != YFilter.not_set)

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
                                if (self.accept_route.is_set or self.accept_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.accept_route.get_name_leafdata())
                                if (self.reject_route.is_set or self.reject_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.reject_route.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accept-route" or name == "reject-route"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "accept-route"):
                                    self.accept_route = value
                                    self.accept_route.value_namespace = name_space
                                    self.accept_route.value_namespace_prefix = name_space_prefix
                                if(value_path == "reject-route"):
                                    self.reject_route = value
                                    self.reject_route.value_namespace = name_space
                                    self.reject_route.value_namespace_prefix = name_space_prefix


                        class IgpActions(Entity):
                            """
                            Actions to set IGP route attributes; these actions
                            apply to multiple IGPs
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions, self).__init__()

                                self.yang_name = "igp-actions"
                                self.yang_parent_name = "actions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: set_tag
                                
                                	Set the tag value for OSPF or IS\-IS routes
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "igp-actions"

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
                                        if name in ("set_tag") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.set_tag.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
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
                                    if(name == "set-tag"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "set-tag"):
                                        self.set_tag = value
                                        self.set_tag.value_namespace = name_space
                                        self.set_tag.value_namespace_prefix = name_space_prefix


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: set_tag
                                
                                	Set the tag value for OSPF or IS\-IS routes
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "igp-actions"

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
                                        if name in ("set_tag") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.set_tag.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
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
                                    if(name == "set-tag"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "set-tag"):
                                        self.set_tag = value
                                        self.set_tag.value_namespace = name_space
                                        self.set_tag.value_namespace_prefix = name_space_prefix

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
                                path_buffer = "igp-actions" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State()
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


                        class BgpActions(Entity):
                            """
                            Top\-level container for BGP\-specific actions
                            
                            .. attribute:: config
                            
                            	Configuration data for BGP\-specific actions
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config>`
                            
                            .. attribute:: set_as_path_prepend
                            
                            	action to prepend local AS number to the AS\-path a specified number of times
                            	**type**\:   :py:class:`SetAsPathPrepend <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend>`
                            
                            .. attribute:: set_community
                            
                            	Action to set the community attributes of the route, along with options to modify how the community is modified. Communities may be set using an inline list OR reference to an existing defined set (not both)
                            	**type**\:   :py:class:`SetCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity>`
                            
                            .. attribute:: set_ext_community
                            
                            	Action to set the extended community attributes of the route, along with options to modify how the community is modified. Extended communities may be set using an inline list OR a reference to an existing defined set (but not both)
                            	**type**\:   :py:class:`SetExtCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity>`
                            
                            .. attribute:: state
                            
                            	Operational state data for BGP\-specific actions
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State>`
                            
                            

                            """

                            _prefix = 'oc-bgp-pol'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions, self).__init__()

                                self.yang_name = "bgp-actions"
                                self.yang_parent_name = "actions"

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.set_as_path_prepend = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend()
                                self.set_as_path_prepend.parent = self
                                self._children_name_map["set_as_path_prepend"] = "set-as-path-prepend"
                                self._children_yang_names.add("set-as-path-prepend")

                                self.set_community = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity()
                                self.set_community.parent = self
                                self._children_name_map["set_community"] = "set-community"
                                self._children_yang_names.add("set-community")

                                self.set_ext_community = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity()
                                self.set_ext_community.parent = self
                                self._children_name_map["set_ext_community"] = "set-ext-community"
                                self._children_yang_names.add("set-ext-community")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")


                            class Config(Entity):
                                """
                                Configuration data for BGP\-specific actions
                                
                                .. attribute:: set_local_pref
                                
                                	set the local pref attribute on the route update
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: set_med
                                
                                	set the med metric attribute in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ^[+\-][0\-9]+
                                
                                
                                ----
                                	**type**\:   :py:class:`BgpSetMedType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetMedType>`
                                
                                
                                ----
                                .. attribute:: set_next_hop
                                
                                	set the next\-hop attribute in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                
                                ----
                                	**type**\:   :py:class:`BgpNextHopType <ydk.models.openconfig.openconfig_bgp_policy.BgpNextHopType>`
                                
                                
                                ----
                                .. attribute:: set_route_origin
                                
                                	set the origin attribute to the specified value
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "bgp-actions"

                                    self.set_local_pref = YLeaf(YType.uint32, "set-local-pref")

                                    self.set_med = YLeaf(YType.str, "set-med")

                                    self.set_next_hop = YLeaf(YType.str, "set-next-hop")

                                    self.set_route_origin = YLeaf(YType.enumeration, "set-route-origin")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("set_local_pref",
                                                    "set_med",
                                                    "set_next_hop",
                                                    "set_route_origin") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.set_local_pref.is_set or
                                        self.set_med.is_set or
                                        self.set_next_hop.is_set or
                                        self.set_route_origin.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.set_local_pref.yfilter != YFilter.not_set or
                                        self.set_med.yfilter != YFilter.not_set or
                                        self.set_next_hop.yfilter != YFilter.not_set or
                                        self.set_route_origin.yfilter != YFilter.not_set)

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
                                    if (self.set_local_pref.is_set or self.set_local_pref.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_local_pref.get_name_leafdata())
                                    if (self.set_med.is_set or self.set_med.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_med.get_name_leafdata())
                                    if (self.set_next_hop.is_set or self.set_next_hop.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_next_hop.get_name_leafdata())
                                    if (self.set_route_origin.is_set or self.set_route_origin.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_route_origin.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "set-local-pref" or name == "set-med" or name == "set-next-hop" or name == "set-route-origin"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "set-local-pref"):
                                        self.set_local_pref = value
                                        self.set_local_pref.value_namespace = name_space
                                        self.set_local_pref.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-med"):
                                        self.set_med = value
                                        self.set_med.value_namespace = name_space
                                        self.set_med.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-next-hop"):
                                        self.set_next_hop = value
                                        self.set_next_hop.value_namespace = name_space
                                        self.set_next_hop.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-route-origin"):
                                        self.set_route_origin = value
                                        self.set_route_origin.value_namespace = name_space
                                        self.set_route_origin.value_namespace_prefix = name_space_prefix


                            class SetAsPathPrepend(Entity):
                                """
                                action to prepend local AS number to the AS\-path a
                                specified number of times
                                
                                .. attribute:: config
                                
                                	Configuration data for the AS path prepend action
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the AS path prepend action
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend, self).__init__()

                                    self.yang_name = "set-as-path-prepend"
                                    self.yang_parent_name = "bgp-actions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for the AS path prepend action
                                    
                                    .. attribute:: repeat_n
                                    
                                    	Number of times to prepend the local AS number to the AS path.  The value should be between 1 and the maximum supported by the implementation
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-as-path-prepend"

                                        self.repeat_n = YLeaf(YType.uint8, "repeat-n")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("repeat_n") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.repeat_n.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.repeat_n.yfilter != YFilter.not_set)

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
                                        if (self.repeat_n.is_set or self.repeat_n.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.repeat_n.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "repeat-n"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "repeat-n"):
                                            self.repeat_n = value
                                            self.repeat_n.value_namespace = name_space
                                            self.repeat_n.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for the AS path prepend action
                                    
                                    .. attribute:: repeat_n
                                    
                                    	Number of times to prepend the local AS number to the AS path.  The value should be between 1 and the maximum supported by the implementation
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-as-path-prepend"

                                        self.repeat_n = YLeaf(YType.uint8, "repeat-n")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("repeat_n") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.repeat_n.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.repeat_n.yfilter != YFilter.not_set)

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
                                        if (self.repeat_n.is_set or self.repeat_n.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.repeat_n.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "repeat-n"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "repeat-n"):
                                            self.repeat_n = value
                                            self.repeat_n.value_namespace = name_space
                                            self.repeat_n.value_namespace_prefix = name_space_prefix

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
                                    path_buffer = "set-as-path-prepend" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State()
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


                            class SetExtCommunity(Entity):
                                """
                                Action to set the extended community attributes of the
                                route, along with options to modify how the community is
                                modified. Extended communities may be set using an inline
                                list OR a reference to an existing defined set (but not
                                both).
                                
                                .. attribute:: config
                                
                                	Configuration data for the set\-ext\-community action
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config>`
                                
                                .. attribute:: inline
                                
                                	Set the extended community values for the action inline with a list
                                	**type**\:   :py:class:`Inline <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline>`
                                
                                .. attribute:: reference
                                
                                	Provide a reference to an extended community set for the set\-ext\-community action
                                	**type**\:   :py:class:`Reference <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the set\-ext\-community action
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity, self).__init__()

                                    self.yang_name = "set-ext-community"
                                    self.yang_parent_name = "bgp-actions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline()
                                    self.inline.parent = self
                                    self._children_name_map["inline"] = "inline"
                                    self._children_yang_names.add("inline")

                                    self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference()
                                    self.reference.parent = self
                                    self._children_name_map["reference"] = "reference"
                                    self._children_yang_names.add("reference")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for the set\-ext\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:   :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:   :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-ext-community"

                                        self.method = YLeaf(YType.enumeration, "method")

                                        self.options = YLeaf(YType.enumeration, "options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("method",
                                                        "options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config, self).__setattr__(name, value)

                                    class Method(Enum):
                                        """
                                        Method

                                        Indicates the method used to specify the extended

                                        communities for the set\-ext\-community action

                                        .. data:: INLINE = 0

                                        	The extended communities are specified inline as a

                                        	list

                                        .. data:: REFERENCE = 1

                                        	The extended communities are specified by referencing a

                                        	defined ext-community set

                                        """

                                        INLINE = Enum.YLeaf(0, "INLINE")

                                        REFERENCE = Enum.YLeaf(1, "REFERENCE")


                                    def has_data(self):
                                        return (
                                            self.method.is_set or
                                            self.options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.method.yfilter != YFilter.not_set or
                                            self.options.yfilter != YFilter.not_set)

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
                                        if (self.method.is_set or self.method.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.method.get_name_leafdata())
                                        if (self.options.is_set or self.options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "method" or name == "options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "method"):
                                            self.method = value
                                            self.method.value_namespace = name_space
                                            self.method.value_namespace_prefix = name_space_prefix
                                        if(value_path == "options"):
                                            self.options = value
                                            self.options.value_namespace = name_space
                                            self.options.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for the set\-ext\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:   :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:   :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-ext-community"

                                        self.method = YLeaf(YType.enumeration, "method")

                                        self.options = YLeaf(YType.enumeration, "options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("method",
                                                        "options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State, self).__setattr__(name, value)

                                    class Method(Enum):
                                        """
                                        Method

                                        Indicates the method used to specify the extended

                                        communities for the set\-ext\-community action

                                        .. data:: INLINE = 0

                                        	The extended communities are specified inline as a

                                        	list

                                        .. data:: REFERENCE = 1

                                        	The extended communities are specified by referencing a

                                        	defined ext-community set

                                        """

                                        INLINE = Enum.YLeaf(0, "INLINE")

                                        REFERENCE = Enum.YLeaf(1, "REFERENCE")


                                    def has_data(self):
                                        return (
                                            self.method.is_set or
                                            self.options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.method.yfilter != YFilter.not_set or
                                            self.options.yfilter != YFilter.not_set)

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
                                        if (self.method.is_set or self.method.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.method.get_name_leafdata())
                                        if (self.options.is_set or self.options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "method" or name == "options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "method"):
                                            self.method = value
                                            self.method.value_namespace = name_space
                                            self.method.value_namespace_prefix = name_space_prefix
                                        if(value_path == "options"):
                                            self.options = value
                                            self.options.value_namespace = name_space
                                            self.options.value_namespace_prefix = name_space_prefix


                                class Inline(Entity):
                                    """
                                    Set the extended community values for the action inline with
                                    a list.
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data or inline specification of set\-ext\-community action
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data or inline specification of set\-ext\-community action
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline, self).__init__()

                                        self.yang_name = "inline"
                                        self.yang_parent_name = "set-ext-community"

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")


                                    class Config(Entity):
                                        """
                                        Configuration data or inline specification of
                                        set\-ext\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the extended community values for the update inline with a list
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
                                        
                                        ----
                                        	**type**\:  
                                        		list of  
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "inline"

                                            self.communities = YLeafList(YType.str, "communities")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("communities") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config, self).__setattr__(name, value)

                                        def has_data(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.communities.yfilter != YFilter.not_set)

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

                                            leaf_name_data.extend(self.communities.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "communities"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "communities"):
                                                self.communities.append(value)


                                    class State(Entity):
                                        """
                                        Operational state data or inline specification of
                                        set\-ext\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the extended community values for the update inline with a list
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
                                        
                                        ----
                                        	**type**\:  
                                        		list of  
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "inline"

                                            self.communities = YLeafList(YType.str, "communities")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("communities") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State, self).__setattr__(name, value)

                                        def has_data(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.communities.yfilter != YFilter.not_set)

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

                                            leaf_name_data.extend(self.communities.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "communities"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "communities"):
                                                self.communities.append(value)

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
                                        path_buffer = "inline" + path_buffer

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
                                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"
                                            return self.config

                                        if (child_yang_name == "state"):
                                            if (self.state is None):
                                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State()
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


                                class Reference(Entity):
                                    """
                                    Provide a reference to an extended community set for the
                                    set\-ext\-community action
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for referening an extended community\-set in the set\-ext\-community action
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for referening an extended community\-set in the set\-ext\-community action
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference, self).__init__()

                                        self.yang_name = "reference"
                                        self.yang_parent_name = "set-ext-community"

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")


                                    class Config(Entity):
                                        """
                                        Configuration data for referening an extended
                                        community\-set in the set\-ext\-community action
                                        
                                        .. attribute:: ext_community_set_ref
                                        
                                        	References a defined extended community set by name
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "reference"

                                            self.ext_community_set_ref = YLeaf(YType.str, "ext-community-set-ref")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("ext_community_set_ref") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.ext_community_set_ref.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.ext_community_set_ref.yfilter != YFilter.not_set)

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
                                            if (self.ext_community_set_ref.is_set or self.ext_community_set_ref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.ext_community_set_ref.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "ext-community-set-ref"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "ext-community-set-ref"):
                                                self.ext_community_set_ref = value
                                                self.ext_community_set_ref.value_namespace = name_space
                                                self.ext_community_set_ref.value_namespace_prefix = name_space_prefix


                                    class State(Entity):
                                        """
                                        Operational state data for referening an extended
                                        community\-set in the set\-ext\-community action
                                        
                                        .. attribute:: ext_community_set_ref
                                        
                                        	References a defined extended community set by name
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "reference"

                                            self.ext_community_set_ref = YLeaf(YType.str, "ext-community-set-ref")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("ext_community_set_ref") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.ext_community_set_ref.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.ext_community_set_ref.yfilter != YFilter.not_set)

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
                                            if (self.ext_community_set_ref.is_set or self.ext_community_set_ref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.ext_community_set_ref.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "ext-community-set-ref"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "ext-community-set-ref"):
                                                self.ext_community_set_ref = value
                                                self.ext_community_set_ref.value_namespace = name_space
                                                self.ext_community_set_ref.value_namespace_prefix = name_space_prefix

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
                                        path_buffer = "reference" + path_buffer

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
                                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"
                                            return self.config

                                        if (child_yang_name == "state"):
                                            if (self.state is None):
                                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State()
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
                                        (self.config is not None and self.config.has_data()) or
                                        (self.inline is not None and self.inline.has_data()) or
                                        (self.reference is not None and self.reference.has_data()) or
                                        (self.state is not None and self.state.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.config is not None and self.config.has_operation()) or
                                        (self.inline is not None and self.inline.has_operation()) or
                                        (self.reference is not None and self.reference.has_operation()) or
                                        (self.state is not None and self.state.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "set-ext-community" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "inline"):
                                        if (self.inline is None):
                                            self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline()
                                            self.inline.parent = self
                                            self._children_name_map["inline"] = "inline"
                                        return self.inline

                                    if (child_yang_name == "reference"):
                                        if (self.reference is None):
                                            self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference()
                                            self.reference.parent = self
                                            self._children_name_map["reference"] = "reference"
                                        return self.reference

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"
                                        return self.state

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "config" or name == "inline" or name == "reference" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class SetCommunity(Entity):
                                """
                                Action to set the community attributes of the route, along
                                with options to modify how the community is modified.
                                Communities may be set using an inline list OR
                                reference to an existing defined set (not both).
                                
                                .. attribute:: config
                                
                                	Configuration data for the set\-community action
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config>`
                                
                                .. attribute:: inline
                                
                                	Set the community values for the action inline with a list
                                	**type**\:   :py:class:`Inline <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline>`
                                
                                .. attribute:: reference
                                
                                	Provide a reference to a defined community set for the set\-community action
                                	**type**\:   :py:class:`Reference <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the set\-community action
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity, self).__init__()

                                    self.yang_name = "set-community"
                                    self.yang_parent_name = "bgp-actions"

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline()
                                    self.inline.parent = self
                                    self._children_name_map["inline"] = "inline"
                                    self._children_yang_names.add("inline")

                                    self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference()
                                    self.reference.parent = self
                                    self._children_name_map["reference"] = "reference"
                                    self._children_yang_names.add("reference")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")


                                class Config(Entity):
                                    """
                                    Configuration data for the set\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:   :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:   :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-community"

                                        self.method = YLeaf(YType.enumeration, "method")

                                        self.options = YLeaf(YType.enumeration, "options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("method",
                                                        "options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config, self).__setattr__(name, value)

                                    class Method(Enum):
                                        """
                                        Method

                                        Indicates the method used to specify the extended

                                        communities for the set\-ext\-community action

                                        .. data:: INLINE = 0

                                        	The extended communities are specified inline as a

                                        	list

                                        .. data:: REFERENCE = 1

                                        	The extended communities are specified by referencing a

                                        	defined ext-community set

                                        """

                                        INLINE = Enum.YLeaf(0, "INLINE")

                                        REFERENCE = Enum.YLeaf(1, "REFERENCE")


                                    def has_data(self):
                                        return (
                                            self.method.is_set or
                                            self.options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.method.yfilter != YFilter.not_set or
                                            self.options.yfilter != YFilter.not_set)

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
                                        if (self.method.is_set or self.method.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.method.get_name_leafdata())
                                        if (self.options.is_set or self.options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "method" or name == "options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "method"):
                                            self.method = value
                                            self.method.value_namespace = name_space
                                            self.method.value_namespace_prefix = name_space_prefix
                                        if(value_path == "options"):
                                            self.options = value
                                            self.options.value_namespace = name_space
                                            self.options.value_namespace_prefix = name_space_prefix


                                class State(Entity):
                                    """
                                    Operational state data for the set\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:   :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:   :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-community"

                                        self.method = YLeaf(YType.enumeration, "method")

                                        self.options = YLeaf(YType.enumeration, "options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("method",
                                                        "options") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State, self).__setattr__(name, value)

                                    class Method(Enum):
                                        """
                                        Method

                                        Indicates the method used to specify the extended

                                        communities for the set\-ext\-community action

                                        .. data:: INLINE = 0

                                        	The extended communities are specified inline as a

                                        	list

                                        .. data:: REFERENCE = 1

                                        	The extended communities are specified by referencing a

                                        	defined ext-community set

                                        """

                                        INLINE = Enum.YLeaf(0, "INLINE")

                                        REFERENCE = Enum.YLeaf(1, "REFERENCE")


                                    def has_data(self):
                                        return (
                                            self.method.is_set or
                                            self.options.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.method.yfilter != YFilter.not_set or
                                            self.options.yfilter != YFilter.not_set)

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
                                        if (self.method.is_set or self.method.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.method.get_name_leafdata())
                                        if (self.options.is_set or self.options.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.options.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "method" or name == "options"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "method"):
                                            self.method = value
                                            self.method.value_namespace = name_space
                                            self.method.value_namespace_prefix = name_space_prefix
                                        if(value_path == "options"):
                                            self.options = value
                                            self.options.value_namespace = name_space
                                            self.options.value_namespace_prefix = name_space_prefix


                                class Inline(Entity):
                                    """
                                    Set the community values for the action inline with
                                    a list.
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data or inline specification of set\-community action
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data or inline specification of set\-community action
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline, self).__init__()

                                        self.yang_name = "inline"
                                        self.yang_parent_name = "set-community"

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")


                                    class Config(Entity):
                                        """
                                        Configuration data or inline specification of set\-community
                                        action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the community values for the update inline with a list
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        
                                        ----
                                        	**type**\:  
                                        		list of  
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "inline"

                                            self.communities = YLeafList(YType.str, "communities")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("communities") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config, self).__setattr__(name, value)

                                        def has_data(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.communities.yfilter != YFilter.not_set)

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

                                            leaf_name_data.extend(self.communities.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "communities"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "communities"):
                                                self.communities.append(value)


                                    class State(Entity):
                                        """
                                        Operational state data or inline specification of
                                        set\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the community values for the update inline with a list
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of int
                                        
                                        	**range:** 65536..4294901759
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        
                                        ----
                                        
                                        ----
                                        	**type**\:  
                                        		list of  
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "inline"

                                            self.communities = YLeafList(YType.str, "communities")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("communities") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State, self).__setattr__(name, value)

                                        def has_data(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for leaf in self.communities.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.communities.yfilter != YFilter.not_set)

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

                                            leaf_name_data.extend(self.communities.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "communities"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "communities"):
                                                self.communities.append(value)

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
                                        path_buffer = "inline" + path_buffer

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
                                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"
                                            return self.config

                                        if (child_yang_name == "state"):
                                            if (self.state is None):
                                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State()
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


                                class Reference(Entity):
                                    """
                                    Provide a reference to a defined community set for the
                                    set\-community action
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for referening a community\-set in the set\-community action
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for referening a community\-set in the set\-community action
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference, self).__init__()

                                        self.yang_name = "reference"
                                        self.yang_parent_name = "set-community"

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")


                                    class Config(Entity):
                                        """
                                        Configuration data for referening a community\-set in the
                                        set\-community action
                                        
                                        .. attribute:: community_set_ref
                                        
                                        	References a defined community set by name
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "reference"

                                            self.community_set_ref = YLeaf(YType.str, "community-set-ref")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("community_set_ref") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.community_set_ref.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.community_set_ref.yfilter != YFilter.not_set)

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
                                            if (self.community_set_ref.is_set or self.community_set_ref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.community_set_ref.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "community-set-ref"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "community-set-ref"):
                                                self.community_set_ref = value
                                                self.community_set_ref.value_namespace = name_space
                                                self.community_set_ref.value_namespace_prefix = name_space_prefix


                                    class State(Entity):
                                        """
                                        Operational state data for referening a community\-set
                                        in the set\-community action
                                        
                                        .. attribute:: community_set_ref
                                        
                                        	References a defined community set by name
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "reference"

                                            self.community_set_ref = YLeaf(YType.str, "community-set-ref")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("community_set_ref") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.community_set_ref.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.community_set_ref.yfilter != YFilter.not_set)

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
                                            if (self.community_set_ref.is_set or self.community_set_ref.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.community_set_ref.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "community-set-ref"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "community-set-ref"):
                                                self.community_set_ref = value
                                                self.community_set_ref.value_namespace = name_space
                                                self.community_set_ref.value_namespace_prefix = name_space_prefix

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
                                        path_buffer = "reference" + path_buffer

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
                                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config()
                                                self.config.parent = self
                                                self._children_name_map["config"] = "config"
                                            return self.config

                                        if (child_yang_name == "state"):
                                            if (self.state is None):
                                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State()
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
                                        (self.config is not None and self.config.has_data()) or
                                        (self.inline is not None and self.inline.has_data()) or
                                        (self.reference is not None and self.reference.has_data()) or
                                        (self.state is not None and self.state.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.config is not None and self.config.has_operation()) or
                                        (self.inline is not None and self.inline.has_operation()) or
                                        (self.reference is not None and self.reference.has_operation()) or
                                        (self.state is not None and self.state.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "set-community" + path_buffer

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
                                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                        return self.config

                                    if (child_yang_name == "inline"):
                                        if (self.inline is None):
                                            self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline()
                                            self.inline.parent = self
                                            self._children_name_map["inline"] = "inline"
                                        return self.inline

                                    if (child_yang_name == "reference"):
                                        if (self.reference is None):
                                            self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference()
                                            self.reference.parent = self
                                            self._children_name_map["reference"] = "reference"
                                        return self.reference

                                    if (child_yang_name == "state"):
                                        if (self.state is None):
                                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"
                                        return self.state

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "config" or name == "inline" or name == "reference" or name == "state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class State(Entity):
                                """
                                Operational state data for BGP\-specific actions
                                
                                .. attribute:: set_local_pref
                                
                                	set the local pref attribute on the route update
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: set_med
                                
                                	set the med metric attribute in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ^[+\-][0\-9]+
                                
                                
                                ----
                                	**type**\:   :py:class:`BgpSetMedType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetMedType>`
                                
                                
                                ----
                                .. attribute:: set_next_hop
                                
                                	set the next\-hop attribute in the route update
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                
                                ----
                                	**type**\:   :py:class:`BgpNextHopType <ydk.models.openconfig.openconfig_bgp_policy.BgpNextHopType>`
                                
                                
                                ----
                                .. attribute:: set_route_origin
                                
                                	set the origin attribute to the specified value
                                	**type**\:   :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "bgp-actions"

                                    self.set_local_pref = YLeaf(YType.uint32, "set-local-pref")

                                    self.set_med = YLeaf(YType.str, "set-med")

                                    self.set_next_hop = YLeaf(YType.str, "set-next-hop")

                                    self.set_route_origin = YLeaf(YType.enumeration, "set-route-origin")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("set_local_pref",
                                                    "set_med",
                                                    "set_next_hop",
                                                    "set_route_origin") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.set_local_pref.is_set or
                                        self.set_med.is_set or
                                        self.set_next_hop.is_set or
                                        self.set_route_origin.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.set_local_pref.yfilter != YFilter.not_set or
                                        self.set_med.yfilter != YFilter.not_set or
                                        self.set_next_hop.yfilter != YFilter.not_set or
                                        self.set_route_origin.yfilter != YFilter.not_set)

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
                                    if (self.set_local_pref.is_set or self.set_local_pref.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_local_pref.get_name_leafdata())
                                    if (self.set_med.is_set or self.set_med.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_med.get_name_leafdata())
                                    if (self.set_next_hop.is_set or self.set_next_hop.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_next_hop.get_name_leafdata())
                                    if (self.set_route_origin.is_set or self.set_route_origin.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.set_route_origin.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "set-local-pref" or name == "set-med" or name == "set-next-hop" or name == "set-route-origin"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "set-local-pref"):
                                        self.set_local_pref = value
                                        self.set_local_pref.value_namespace = name_space
                                        self.set_local_pref.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-med"):
                                        self.set_med = value
                                        self.set_med.value_namespace = name_space
                                        self.set_med.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-next-hop"):
                                        self.set_next_hop = value
                                        self.set_next_hop.value_namespace = name_space
                                        self.set_next_hop.value_namespace_prefix = name_space_prefix
                                    if(value_path == "set-route-origin"):
                                        self.set_route_origin = value
                                        self.set_route_origin.value_namespace = name_space
                                        self.set_route_origin.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    (self.config is not None and self.config.has_data()) or
                                    (self.set_as_path_prepend is not None and self.set_as_path_prepend.has_data()) or
                                    (self.set_community is not None and self.set_community.has_data()) or
                                    (self.set_ext_community is not None and self.set_ext_community.has_data()) or
                                    (self.state is not None and self.state.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.config is not None and self.config.has_operation()) or
                                    (self.set_as_path_prepend is not None and self.set_as_path_prepend.has_operation()) or
                                    (self.set_community is not None and self.set_community.has_operation()) or
                                    (self.set_ext_community is not None and self.set_ext_community.has_operation()) or
                                    (self.state is not None and self.state.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "openconfig-bgp-policy:bgp-actions" + path_buffer

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
                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                    return self.config

                                if (child_yang_name == "set-as-path-prepend"):
                                    if (self.set_as_path_prepend is None):
                                        self.set_as_path_prepend = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend()
                                        self.set_as_path_prepend.parent = self
                                        self._children_name_map["set_as_path_prepend"] = "set-as-path-prepend"
                                    return self.set_as_path_prepend

                                if (child_yang_name == "set-community"):
                                    if (self.set_community is None):
                                        self.set_community = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity()
                                        self.set_community.parent = self
                                        self._children_name_map["set_community"] = "set-community"
                                    return self.set_community

                                if (child_yang_name == "set-ext-community"):
                                    if (self.set_ext_community is None):
                                        self.set_ext_community = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity()
                                        self.set_ext_community.parent = self
                                        self._children_name_map["set_ext_community"] = "set-ext-community"
                                    return self.set_ext_community

                                if (child_yang_name == "state"):
                                    if (self.state is None):
                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                    return self.state

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "config" or name == "set-as-path-prepend" or name == "set-community" or name == "set-ext-community" or name == "state"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.bgp_actions is not None and self.bgp_actions.has_data()) or
                                (self.config is not None and self.config.has_data()) or
                                (self.igp_actions is not None and self.igp_actions.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.bgp_actions is not None and self.bgp_actions.has_operation()) or
                                (self.config is not None and self.config.has_operation()) or
                                (self.igp_actions is not None and self.igp_actions.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "actions" + path_buffer

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

                            if (child_yang_name == "bgp-actions"):
                                if (self.bgp_actions is None):
                                    self.bgp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions()
                                    self.bgp_actions.parent = self
                                    self._children_name_map["bgp_actions"] = "bgp-actions"
                                return self.bgp_actions

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "igp-actions"):
                                if (self.igp_actions is None):
                                    self.igp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions()
                                    self.igp_actions.parent = self
                                    self._children_name_map["igp_actions"] = "igp-actions"
                                return self.igp_actions

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bgp-actions" or name == "config" or name == "igp-actions" or name == "state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.name.is_set or
                            (self.actions is not None and self.actions.has_data()) or
                            (self.conditions is not None and self.conditions.has_data()) or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            (self.actions is not None and self.actions.has_operation()) or
                            (self.conditions is not None and self.conditions.has_operation()) or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statement" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "actions"):
                            if (self.actions is None):
                                self.actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions()
                                self.actions.parent = self
                                self._children_name_map["actions"] = "actions"
                            return self.actions

                        if (child_yang_name == "conditions"):
                            if (self.conditions is None):
                                self.conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions()
                                self.conditions.parent = self
                                self._children_name_map["conditions"] = "conditions"
                            return self.conditions

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "actions" or name == "conditions" or name == "config" or name == "state" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.statement:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.statement:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statements" + path_buffer

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

                    if (child_yang_name == "statement"):
                        for c in self.statement:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.statement.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statement"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.state is not None and self.state.has_data()) or
                    (self.statements is not None and self.statements.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.state is not None and self.state.has_operation()) or
                    (self.statements is not None and self.statements.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-definition" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-routing-policy:routing-policy/policy-definitions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                if (child_yang_name == "statements"):
                    if (self.statements is None):
                        self.statements = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements()
                        self.statements.parent = self
                        self._children_name_map["statements"] = "statements"
                    return self.statements

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "state" or name == "statements" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.policy_definition:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.policy_definition:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policy-definitions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-routing-policy:routing-policy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "policy-definition"):
                for c in self.policy_definition:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RoutingPolicy.PolicyDefinitions.PolicyDefinition()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.policy_definition.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "policy-definition"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.defined_sets is not None and self.defined_sets.has_data()) or
            (self.policy_definitions is not None and self.policy_definitions.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.defined_sets is not None and self.defined_sets.has_operation()) or
            (self.policy_definitions is not None and self.policy_definitions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-routing-policy:routing-policy" + path_buffer

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

        if (child_yang_name == "defined-sets"):
            if (self.defined_sets is None):
                self.defined_sets = RoutingPolicy.DefinedSets()
                self.defined_sets.parent = self
                self._children_name_map["defined_sets"] = "defined-sets"
            return self.defined_sets

        if (child_yang_name == "policy-definitions"):
            if (self.policy_definitions is None):
                self.policy_definitions = RoutingPolicy.PolicyDefinitions()
                self.policy_definitions.parent = self
                self._children_name_map["policy_definitions"] = "policy-definitions"
            return self.policy_definitions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "defined-sets" or name == "policy-definitions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

