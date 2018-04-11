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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DefaultPolicyType(Enum):
    """
    DefaultPolicyType (Enum Class)

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
    	**type**\:  :py:class:`DefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets>`
    
    .. attribute:: policy_definitions
    
    	Enclosing container for the list of top\-level policy  definitions
    	**type**\:  :py:class:`PolicyDefinitions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions>`
    
    

    """

    _prefix = 'oc-rpol'
    _revision = '2016-05-12'

    def __init__(self):
        super(RoutingPolicy, self).__init__()
        self._top_entity = None

        self.yang_name = "routing-policy"
        self.yang_parent_name = "openconfig-routing-policy"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("defined-sets", ("defined_sets", RoutingPolicy.DefinedSets)), ("policy-definitions", ("policy_definitions", RoutingPolicy.PolicyDefinitions))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.defined_sets = RoutingPolicy.DefinedSets()
        self.defined_sets.parent = self
        self._children_name_map["defined_sets"] = "defined-sets"
        self._children_yang_names.add("defined-sets")

        self.policy_definitions = RoutingPolicy.PolicyDefinitions()
        self.policy_definitions.parent = self
        self._children_name_map["policy_definitions"] = "policy-definitions"
        self._children_yang_names.add("policy-definitions")
        self._segment_path = lambda: "openconfig-routing-policy:routing-policy"


    class DefinedSets(Entity):
        """
        Predefined sets of attributes used in policy match
        statements
        
        .. attribute:: prefix_sets
        
        	Enclosing container 
        	**type**\:  :py:class:`PrefixSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets>`
        
        .. attribute:: neighbor_sets
        
        	Enclosing container for the list of neighbor set definitions
        	**type**\:  :py:class:`NeighborSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets>`
        
        .. attribute:: tag_sets
        
        	Enclosing container for the list of tag sets
        	**type**\:  :py:class:`TagSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets>`
        
        .. attribute:: bgp_defined_sets
        
        	BGP\-related set definitions for policy match conditions
        	**type**\:  :py:class:`BgpDefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets>`
        
        

        """

        _prefix = 'oc-rpol'
        _revision = '2016-05-12'

        def __init__(self):
            super(RoutingPolicy.DefinedSets, self).__init__()

            self.yang_name = "defined-sets"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("prefix-sets", ("prefix_sets", RoutingPolicy.DefinedSets.PrefixSets)), ("neighbor-sets", ("neighbor_sets", RoutingPolicy.DefinedSets.NeighborSets)), ("tag-sets", ("tag_sets", RoutingPolicy.DefinedSets.TagSets)), ("openconfig-bgp-policy:bgp-defined-sets", ("bgp_defined_sets", RoutingPolicy.DefinedSets.BgpDefinedSets))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.prefix_sets = RoutingPolicy.DefinedSets.PrefixSets()
            self.prefix_sets.parent = self
            self._children_name_map["prefix_sets"] = "prefix-sets"
            self._children_yang_names.add("prefix-sets")

            self.neighbor_sets = RoutingPolicy.DefinedSets.NeighborSets()
            self.neighbor_sets.parent = self
            self._children_name_map["neighbor_sets"] = "neighbor-sets"
            self._children_yang_names.add("neighbor-sets")

            self.tag_sets = RoutingPolicy.DefinedSets.TagSets()
            self.tag_sets.parent = self
            self._children_name_map["tag_sets"] = "tag-sets"
            self._children_yang_names.add("tag-sets")

            self.bgp_defined_sets = RoutingPolicy.DefinedSets.BgpDefinedSets()
            self.bgp_defined_sets.parent = self
            self._children_name_map["bgp_defined_sets"] = "openconfig-bgp-policy:bgp-defined-sets"
            self._children_yang_names.add("openconfig-bgp-policy:bgp-defined-sets")
            self._segment_path = lambda: "defined-sets"
            self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/%s" % self._segment_path()


        class PrefixSets(Entity):
            """
            Enclosing container 
            
            .. attribute:: prefix_set
            
            	List of the defined prefix sets
            	**type**\: list of  		 :py:class:`PrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.PrefixSets, self).__init__()

                self.yang_name = "prefix-sets"
                self.yang_parent_name = "defined-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("prefix-set", ("prefix_set", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet))])
                self._leafs = OrderedDict()

                self.prefix_set = YList(self)
                self._segment_path = lambda: "prefix-sets"
                self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets, [], name, value)


            class PrefixSet(Entity):
                """
                List of the defined prefix sets
                
                .. attribute:: prefix_set_name  (key)
                
                	Reference to prefix name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for prefix sets
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config>`
                
                .. attribute:: state
                
                	Operational state data 
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State>`
                
                .. attribute:: prefixes
                
                	Enclosing container for the list of prefixes in a policy prefix list
                	**type**\:  :py:class:`Prefixes <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet, self).__init__()

                    self.yang_name = "prefix-set"
                    self.yang_parent_name = "prefix-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['prefix_set_name']
                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State)), ("prefixes", ("prefixes", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefix_set_name', YLeaf(YType.str, 'prefix-set-name')),
                    ])
                    self.prefix_set_name = None

                    self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.prefixes = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                    self._children_yang_names.add("prefixes")
                    self._segment_path = lambda: "prefix-set" + "[prefix-set-name='" + str(self.prefix_set_name) + "']"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet, ['prefix_set_name'], name, value)


                class Config(Entity):
                    """
                    Configuration data for prefix sets
                    
                    .. attribute:: prefix_set_name
                    
                    	name / label of the prefix set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "prefix-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix_set_name', YLeaf(YType.str, 'prefix-set-name')),
                        ])
                        self.prefix_set_name = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Config, ['prefix_set_name'], name, value)


                class State(Entity):
                    """
                    Operational state data 
                    
                    .. attribute:: prefix_set_name
                    
                    	name / label of the prefix set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "prefix-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix_set_name', YLeaf(YType.str, 'prefix-set-name')),
                        ])
                        self.prefix_set_name = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.State, ['prefix_set_name'], name, value)


                class Prefixes(Entity):
                    """
                    Enclosing container for the list of prefixes in a policy
                    prefix list
                    
                    .. attribute:: prefix
                    
                    	List of prefixes in the prefix set
                    	**type**\: list of  		 :py:class:`Prefix <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes, self).__init__()

                        self.yang_name = "prefixes"
                        self.yang_parent_name = "prefix-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("prefix", ("prefix", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix))])
                        self._leafs = OrderedDict()

                        self.prefix = YList(self)
                        self._segment_path = lambda: "prefixes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes, [], name, value)


                    class Prefix(Entity):
                        """
                        List of prefixes in the prefix set
                        
                        .. attribute:: ip_prefix  (key)
                        
                        	Reference to the ip\-prefix list key
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        	**refers to**\:  :py:class:`ip_prefix <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config>`
                        
                        .. attribute:: masklength_range  (key)
                        
                        	Reference to the masklength\-range list key
                        	**type**\: str
                        
                        	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                        
                        	**refers to**\:  :py:class:`masklength_range <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for prefix definition
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for prefix definition
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefixes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ip_prefix','masklength_range']
                            self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config)), ("state", ("state", RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_prefix', YLeaf(YType.str, 'ip-prefix')),
                                ('masklength_range', YLeaf(YType.str, 'masklength-range')),
                            ])
                            self.ip_prefix = None
                            self.masklength_range = None

                            self.config = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "prefix" + "[ip-prefix='" + str(self.ip_prefix) + "']" + "[masklength-range='" + str(self.masklength_range) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix, ['ip_prefix', 'masklength_range'], name, value)


                        class Config(Entity):
                            """
                            Configuration data for prefix definition
                            
                            .. attribute:: ip_prefix
                            
                            	The prefix member in CIDR notation \-\- while the prefix may be either IPv4 or IPv6, most implementations require all members of the prefix set to be the same address family.  Mixing address types in the same prefix set is likely to cause an error
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: masklength_range
                            
                            	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                            	**type**\: str
                            
                            	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_prefix', YLeaf(YType.str, 'ip-prefix')),
                                    ('masklength_range', YLeaf(YType.str, 'masklength-range')),
                                ])
                                self.ip_prefix = None
                                self.masklength_range = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.Config, ['ip_prefix', 'masklength_range'], name, value)


                        class State(Entity):
                            """
                            Operational state data for prefix definition
                            
                            .. attribute:: ip_prefix
                            
                            	The prefix member in CIDR notation \-\- while the prefix may be either IPv4 or IPv6, most implementations require all members of the prefix set to be the same address family.  Mixing address types in the same prefix set is likely to cause an error
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: masklength_range
                            
                            	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                            	**type**\: str
                            
                            	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_prefix', YLeaf(YType.str, 'ip-prefix')),
                                    ('masklength_range', YLeaf(YType.str, 'masklength-range')),
                                ])
                                self.ip_prefix = None
                                self.masklength_range = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefixes.Prefix.State, ['ip_prefix', 'masklength_range'], name, value)


        class NeighborSets(Entity):
            """
            Enclosing container for the list of neighbor set
            definitions
            
            .. attribute:: neighbor_set
            
            	List of defined neighbor sets for use in policies
            	**type**\: list of  		 :py:class:`NeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.NeighborSets, self).__init__()

                self.yang_name = "neighbor-sets"
                self.yang_parent_name = "defined-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("neighbor-set", ("neighbor_set", RoutingPolicy.DefinedSets.NeighborSets.NeighborSet))])
                self._leafs = OrderedDict()

                self.neighbor_set = YList(self)
                self._segment_path = lambda: "neighbor-sets"
                self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.DefinedSets.NeighborSets, [], name, value)


            class NeighborSet(Entity):
                """
                List of defined neighbor sets for use in policies.
                
                .. attribute:: neighbor_set_name  (key)
                
                	Reference to the neighbor set name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for neighbor sets
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config>`
                
                .. attribute:: state
                
                	Operational state data for neighbor sets
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet, self).__init__()

                    self.yang_name = "neighbor-set"
                    self.yang_parent_name = "neighbor-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['neighbor_set_name']
                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('neighbor_set_name', YLeaf(YType.str, 'neighbor-set-name')),
                    ])
                    self.neighbor_set_name = None

                    self.config = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "neighbor-set" + "[neighbor-set-name='" + str(self.neighbor_set_name) + "']"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/neighbor-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet, ['neighbor_set_name'], name, value)


                class Config(Entity):
                    """
                    Configuration data for neighbor sets.
                    
                    .. attribute:: neighbor_set_name
                    
                    	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    .. attribute:: address
                    
                    	List of IP addresses in the neighbor set
                    	**type**\: union of the below types:
                    
                    		**type**\: list of str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: list of str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "neighbor-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('neighbor_set_name', YLeaf(YType.str, 'neighbor-set-name')),
                            ('address', YLeafList(YType.str, 'address')),
                        ])
                        self.neighbor_set_name = None
                        self.address = []
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Config, ['neighbor_set_name', 'address'], name, value)


                class State(Entity):
                    """
                    Operational state data for neighbor sets.
                    
                    .. attribute:: neighbor_set_name
                    
                    	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    .. attribute:: address
                    
                    	List of IP addresses in the neighbor set
                    	**type**\: union of the below types:
                    
                    		**type**\: list of str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: list of str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "neighbor-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('neighbor_set_name', YLeaf(YType.str, 'neighbor-set-name')),
                            ('address', YLeafList(YType.str, 'address')),
                        ])
                        self.neighbor_set_name = None
                        self.address = []
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.State, ['neighbor_set_name', 'address'], name, value)


        class TagSets(Entity):
            """
            Enclosing container for the list of tag sets.
            
            .. attribute:: tag_set
            
            	List of tag set definitions
            	**type**\: list of  		 :py:class:`TagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.TagSets, self).__init__()

                self.yang_name = "tag-sets"
                self.yang_parent_name = "defined-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("tag-set", ("tag_set", RoutingPolicy.DefinedSets.TagSets.TagSet))])
                self._leafs = OrderedDict()

                self.tag_set = YList(self)
                self._segment_path = lambda: "tag-sets"
                self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.DefinedSets.TagSets, [], name, value)


            class TagSet(Entity):
                """
                List of tag set definitions.
                
                .. attribute:: tag_set_name  (key)
                
                	Reference to the tag set name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Config>`
                
                .. attribute:: config
                
                	Configuration data for tag sets
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Config>`
                
                .. attribute:: state
                
                	Operational state data for tag sets
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.State>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.TagSets.TagSet, self).__init__()

                    self.yang_name = "tag-set"
                    self.yang_parent_name = "tag-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['tag_set_name']
                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.TagSets.TagSet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.TagSets.TagSet.State))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tag_set_name', YLeaf(YType.str, 'tag-set-name')),
                    ])
                    self.tag_set_name = None

                    self.config = RoutingPolicy.DefinedSets.TagSets.TagSet.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = RoutingPolicy.DefinedSets.TagSets.TagSet.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "tag-set" + "[tag-set-name='" + str(self.tag_set_name) + "']"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/tag-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.TagSets.TagSet, ['tag_set_name'], name, value)


                class Config(Entity):
                    """
                    Configuration data for tag sets
                    
                    .. attribute:: tag_set_name
                    
                    	name / label of the tag set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    .. attribute:: tag_value
                    
                    	Value of the tag set member
                    	**type**\: union of the below types:
                    
                    		**type**\: list of int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: list of str
                    
                    			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.TagSets.TagSet.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "tag-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tag_set_name', YLeaf(YType.str, 'tag-set-name')),
                            ('tag_value', YLeafList(YType.str, 'tag-value')),
                        ])
                        self.tag_set_name = None
                        self.tag_value = []
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.TagSets.TagSet.Config, ['tag_set_name', 'tag_value'], name, value)


                class State(Entity):
                    """
                    Operational state data for tag sets
                    
                    .. attribute:: tag_set_name
                    
                    	name / label of the tag set \-\- this is used to reference the set in match conditions
                    	**type**\: str
                    
                    .. attribute:: tag_value
                    
                    	Value of the tag set member
                    	**type**\: union of the below types:
                    
                    		**type**\: list of int
                    
                    			**range:** 0..4294967295
                    
                    		**type**\: list of str
                    
                    			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.TagSets.TagSet.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "tag-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tag_set_name', YLeaf(YType.str, 'tag-set-name')),
                            ('tag_value', YLeafList(YType.str, 'tag-value')),
                        ])
                        self.tag_set_name = None
                        self.tag_value = []
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.TagSets.TagSet.State, ['tag_set_name', 'tag_value'], name, value)


        class BgpDefinedSets(Entity):
            """
            BGP\-related set definitions for policy match conditions
            
            .. attribute:: community_sets
            
            	Enclosing container for list of defined BGP community sets
            	**type**\:  :py:class:`CommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets>`
            
            .. attribute:: ext_community_sets
            
            	Enclosing container for list of extended BGP community sets
            	**type**\:  :py:class:`ExtCommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets>`
            
            .. attribute:: as_path_sets
            
            	Enclosing container for list of define AS path sets
            	**type**\:  :py:class:`AsPathSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets>`
            
            

            """

            _prefix = 'oc-bgp-pol'
            _revision = '2016-06-21'

            def __init__(self):
                super(RoutingPolicy.DefinedSets.BgpDefinedSets, self).__init__()

                self.yang_name = "bgp-defined-sets"
                self.yang_parent_name = "defined-sets"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("community-sets", ("community_sets", RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets)), ("ext-community-sets", ("ext_community_sets", RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets)), ("as-path-sets", ("as_path_sets", RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets()
                self.community_sets.parent = self
                self._children_name_map["community_sets"] = "community-sets"
                self._children_yang_names.add("community-sets")

                self.ext_community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets()
                self.ext_community_sets.parent = self
                self._children_name_map["ext_community_sets"] = "ext-community-sets"
                self._children_yang_names.add("ext-community-sets")

                self.as_path_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets()
                self.as_path_sets.parent = self
                self._children_name_map["as_path_sets"] = "as-path-sets"
                self._children_yang_names.add("as-path-sets")
                self._segment_path = lambda: "openconfig-bgp-policy:bgp-defined-sets"
                self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/%s" % self._segment_path()


            class CommunitySets(Entity):
                """
                Enclosing container for list of defined BGP community sets
                
                .. attribute:: community_set
                
                	List of defined BGP community sets
                	**type**\: list of  		 :py:class:`CommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets, self).__init__()

                    self.yang_name = "community-sets"
                    self.yang_parent_name = "bgp-defined-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("community-set", ("community_set", RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet))])
                    self._leafs = OrderedDict()

                    self.community_set = YList(self)
                    self._segment_path = lambda: "community-sets"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets, [], name, value)


                class CommunitySet(Entity):
                    """
                    List of defined BGP community sets
                    
                    .. attribute:: community_set_name  (key)
                    
                    	Reference to list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for BGP community sets
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for BGP community sets
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet, self).__init__()

                        self.yang_name = "community-set"
                        self.yang_parent_name = "community-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['community_set_name']
                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('community_set_name', YLeaf(YType.str, 'community-set-name')),
                        ])
                        self.community_set_name = None

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "community-set" + "[community-set-name='" + str(self.community_set_name) + "']"
                        self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/community-sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet, ['community_set_name'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for BGP community sets
                        
                        .. attribute:: community_set_name
                        
                        	name / label of the community set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: community_member
                        
                        	members of the community set
                        	**type**\: union of the below types:
                        
                        		**type**\: list of int
                        
                        			**range:** 65536..4294901759
                        
                        		**type**\: list of str
                        
                        			**pattern:** ([0\-9]+\:[0\-9]+)
                        
                        		**type**\: list of str
                        
                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "community-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('community_set_name', YLeaf(YType.str, 'community-set-name')),
                                ('community_member', YLeafList(YType.str, 'community-member')),
                            ])
                            self.community_set_name = None
                            self.community_member = []
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.Config, ['community_set_name', 'community_member'], name, value)


                    class State(Entity):
                        """
                        Operational state data for BGP community sets
                        
                        .. attribute:: community_set_name
                        
                        	name / label of the community set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: community_member
                        
                        	members of the community set
                        	**type**\: union of the below types:
                        
                        		**type**\: list of int
                        
                        			**range:** 65536..4294901759
                        
                        		**type**\: list of str
                        
                        			**pattern:** ([0\-9]+\:[0\-9]+)
                        
                        		**type**\: list of str
                        
                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "community-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('community_set_name', YLeaf(YType.str, 'community-set-name')),
                                ('community_member', YLeafList(YType.str, 'community-member')),
                            ])
                            self.community_set_name = None
                            self.community_member = []
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet.State, ['community_set_name', 'community_member'], name, value)


            class ExtCommunitySets(Entity):
                """
                Enclosing container for list of extended BGP community
                sets
                
                .. attribute:: ext_community_set
                
                	List of defined extended BGP community sets
                	**type**\: list of  		 :py:class:`ExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets, self).__init__()

                    self.yang_name = "ext-community-sets"
                    self.yang_parent_name = "bgp-defined-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ext-community-set", ("ext_community_set", RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet))])
                    self._leafs = OrderedDict()

                    self.ext_community_set = YList(self)
                    self._segment_path = lambda: "ext-community-sets"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets, [], name, value)


                class ExtCommunitySet(Entity):
                    """
                    List of defined extended BGP community sets
                    
                    .. attribute:: ext_community_set_name  (key)
                    
                    	Reference to list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for extended BGP community sets
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for extended BGP community sets
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet, self).__init__()

                        self.yang_name = "ext-community-set"
                        self.yang_parent_name = "ext-community-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ext_community_set_name']
                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ext_community_set_name', YLeaf(YType.str, 'ext-community-set-name')),
                        ])
                        self.ext_community_set_name = None

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "ext-community-set" + "[ext-community-set-name='" + str(self.ext_community_set_name) + "']"
                        self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/ext-community-sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet, ['ext_community_set_name'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for extended BGP community sets
                        
                        .. attribute:: ext_community_set_name
                        
                        	name / label of the extended community set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        .. attribute:: ext_community_member
                        
                        	members of the extended community set
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
                        
                        		**type**\: list of str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ext-community-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ext_community_set_name', YLeaf(YType.str, 'ext-community-set-name')),
                                ('ext_community_member', YLeafList(YType.str, 'ext-community-member')),
                            ])
                            self.ext_community_set_name = None
                            self.ext_community_member = []
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.Config, ['ext_community_set_name', 'ext_community_member'], name, value)


                    class State(Entity):
                        """
                        Operational state data for extended BGP community sets
                        
                        .. attribute:: ext_community_set_name
                        
                        	name / label of the extended community set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        .. attribute:: ext_community_member
                        
                        	members of the extended community set
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
                        
                        		**type**\: list of str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ext-community-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ext_community_set_name', YLeaf(YType.str, 'ext-community-set-name')),
                                ('ext_community_member', YLeafList(YType.str, 'ext-community-member')),
                            ])
                            self.ext_community_set_name = None
                            self.ext_community_member = []
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet.State, ['ext_community_set_name', 'ext_community_member'], name, value)


            class AsPathSets(Entity):
                """
                Enclosing container for list of define AS path sets
                
                .. attribute:: as_path_set
                
                	List of defined AS path sets
                	**type**\: list of  		 :py:class:`AsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                
                

                """

                _prefix = 'oc-bgp-pol'
                _revision = '2016-06-21'

                def __init__(self):
                    super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets, self).__init__()

                    self.yang_name = "as-path-sets"
                    self.yang_parent_name = "bgp-defined-sets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("as-path-set", ("as_path_set", RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet))])
                    self._leafs = OrderedDict()

                    self.as_path_set = YList(self)
                    self._segment_path = lambda: "as-path-sets"
                    self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets, [], name, value)


                class AsPathSet(Entity):
                    """
                    List of defined AS path sets
                    
                    .. attribute:: as_path_set_name  (key)
                    
                    	Reference to list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for AS path sets
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for AS path sets
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State>`
                    
                    

                    """

                    _prefix = 'oc-bgp-pol'
                    _revision = '2016-06-21'

                    def __init__(self):
                        super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet, self).__init__()

                        self.yang_name = "as-path-set"
                        self.yang_parent_name = "as-path-sets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['as_path_set_name']
                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config)), ("state", ("state", RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('as_path_set_name', YLeaf(YType.str, 'as-path-set-name')),
                        ])
                        self.as_path_set_name = None

                        self.config = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "as-path-set" + "[as-path-set-name='" + str(self.as_path_set_name) + "']"
                        self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/defined-sets/openconfig-bgp-policy:bgp-defined-sets/as-path-sets/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet, ['as_path_set_name'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for AS path sets
                        
                        .. attribute:: as_path_set_name
                        
                        	name of the AS path set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        .. attribute:: as_path_set_member
                        
                        	AS path expression \-\- list of ASes in the set
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "as-path-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('as_path_set_name', YLeaf(YType.str, 'as-path-set-name')),
                                ('as_path_set_member', YLeafList(YType.str, 'as-path-set-member')),
                            ])
                            self.as_path_set_name = None
                            self.as_path_set_member = []
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.Config, ['as_path_set_name', 'as_path_set_member'], name, value)


                    class State(Entity):
                        """
                        Operational state data for AS path sets
                        
                        .. attribute:: as_path_set_name
                        
                        	name of the AS path set \-\- this is used to reference the set in match conditions
                        	**type**\: str
                        
                        .. attribute:: as_path_set_member
                        
                        	AS path expression \-\- list of ASes in the set
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'oc-bgp-pol'
                        _revision = '2016-06-21'

                        def __init__(self):
                            super(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "as-path-set"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('as_path_set_name', YLeaf(YType.str, 'as-path-set-name')),
                                ('as_path_set_member', YLeafList(YType.str, 'as-path-set-member')),
                            ])
                            self.as_path_set_name = None
                            self.as_path_set_member = []
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet.State, ['as_path_set_name', 'as_path_set_member'], name, value)


    class PolicyDefinitions(Entity):
        """
        Enclosing container for the list of top\-level policy
         definitions
        
        .. attribute:: policy_definition
        
        	List of top\-level policy definitions, keyed by unique name.  These policy definitions are expected to be referenced (by name) in policy chains specified in import or export configuration statements
        	**type**\: list of  		 :py:class:`PolicyDefinition <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
        
        

        """

        _prefix = 'oc-rpol'
        _revision = '2016-05-12'

        def __init__(self):
            super(RoutingPolicy.PolicyDefinitions, self).__init__()

            self.yang_name = "policy-definitions"
            self.yang_parent_name = "routing-policy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("policy-definition", ("policy_definition", RoutingPolicy.PolicyDefinitions.PolicyDefinition))])
            self._leafs = OrderedDict()

            self.policy_definition = YList(self)
            self._segment_path = lambda: "policy-definitions"
            self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingPolicy.PolicyDefinitions, [], name, value)


        class PolicyDefinition(Entity):
            """
            List of top\-level policy definitions, keyed by unique
            name.  These policy definitions are expected to be
            referenced (by name) in policy chains specified in import
            or export configuration statements.
            
            .. attribute:: name  (key)
            
            	Reference to the list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config>`
            
            .. attribute:: config
            
            	Configuration data for policy defintions
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config>`
            
            .. attribute:: state
            
            	Operational state data for policy definitions
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.State>`
            
            .. attribute:: statements
            
            	Enclosing container for policy statements
            	**type**\:  :py:class:`Statements <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements>`
            
            

            """

            _prefix = 'oc-rpol'
            _revision = '2016-05-12'

            def __init__(self):
                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition, self).__init__()

                self.yang_name = "policy-definition"
                self.yang_parent_name = "policy-definitions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.State)), ("statements", ("statements", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

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
                self._segment_path = lambda: "policy-definition" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-routing-policy:routing-policy/policy-definitions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition, ['name'], name, value)


            class Config(Entity):
                """
                Configuration data for policy defintions
                
                .. attribute:: name
                
                	Name of the top\-level policy definition \-\- this name is used in references to the current policy
                	**type**\: str
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "policy-definition"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Config, ['name'], name, value)


            class State(Entity):
                """
                Operational state data for policy definitions
                
                .. attribute:: name
                
                	Name of the top\-level policy definition \-\- this name is used in references to the current policy
                	**type**\: str
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "policy-definition"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.State, ['name'], name, value)


            class Statements(Entity):
                """
                Enclosing container for policy statements
                
                .. attribute:: statement
                
                	Policy statements group conditions and actions within a policy definition.  They are evaluated in the order specified (see the description of policy evaluation at the top of this module
                	**type**\: list of  		 :py:class:`Statement <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement>`
                
                

                """

                _prefix = 'oc-rpol'
                _revision = '2016-05-12'

                def __init__(self):
                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements, self).__init__()

                    self.yang_name = "statements"
                    self.yang_parent_name = "policy-definition"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("statement", ("statement", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement))])
                    self._leafs = OrderedDict()

                    self.statement = YList(self)
                    self._segment_path = lambda: "statements"

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements, [], name, value)


                class Statement(Entity):
                    """
                    Policy statements group conditions and actions
                    within a policy definition.  They are evaluated in
                    the order specified (see the description of policy
                    evaluation at the top of this module.
                    
                    .. attribute:: name  (key)
                    
                    	Reference to list key
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for policy statements
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for policy statements
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State>`
                    
                    .. attribute:: conditions
                    
                    	Condition statements for the current policy statement
                    	**type**\:  :py:class:`Conditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions>`
                    
                    .. attribute:: actions
                    
                    	Top\-level container for policy action statements
                    	**type**\:  :py:class:`Actions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions>`
                    
                    

                    """

                    _prefix = 'oc-rpol'
                    _revision = '2016-05-12'

                    def __init__(self):
                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement, self).__init__()

                        self.yang_name = "statement"
                        self.yang_parent_name = "statements"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State)), ("conditions", ("conditions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions)), ("actions", ("actions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                        ])
                        self.name = None

                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions()
                        self.conditions.parent = self
                        self._children_name_map["conditions"] = "conditions"
                        self._children_yang_names.add("conditions")

                        self.actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions()
                        self.actions.parent = self
                        self._children_name_map["actions"] = "actions"
                        self._children_yang_names.add("actions")
                        self._segment_path = lambda: "statement" + "[name='" + str(self.name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement, ['name'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for policy statements
                        
                        .. attribute:: name
                        
                        	name of the policy statement
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "statement"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                            ])
                            self.name = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Config, ['name'], name, value)


                    class State(Entity):
                        """
                        Operational state data for policy statements
                        
                        .. attribute:: name
                        
                        	name of the policy statement
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "statement"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                            ])
                            self.name = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.State, ['name'], name, value)


                    class Conditions(Entity):
                        """
                        Condition statements for the current policy statement
                        
                        .. attribute:: config
                        
                        	Configuration data for policy conditions
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for policy conditions
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State>`
                        
                        .. attribute:: match_interface
                        
                        	Top\-level container for interface match conditions
                        	**type**\:  :py:class:`MatchInterface <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface>`
                        
                        .. attribute:: match_prefix_set
                        
                        	Match a referenced prefix\-set according to the logic defined in the match\-set\-options leaf
                        	**type**\:  :py:class:`MatchPrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet>`
                        
                        .. attribute:: match_neighbor_set
                        
                        	Match a referenced neighbor set according to the logic defined in the match\-set\-options\-leaf
                        	**type**\:  :py:class:`MatchNeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet>`
                        
                        .. attribute:: match_tag_set
                        
                        	Match a referenced tag set according to the logic defined in the match\-options\-set leaf
                        	**type**\:  :py:class:`MatchTagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet>`
                        
                        .. attribute:: igp_conditions
                        
                        	Policy conditions for IGP attributes
                        	**type**\:  :py:class:`IgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions>`
                        
                        .. attribute:: bgp_conditions
                        
                        	Top\-level container 
                        	**type**\:  :py:class:`BgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions>`
                        
                        .. attribute:: isis_conditions
                        
                        	Match conditions relating to the IS\-IS protocol
                        	**type**\:  :py:class:`IsisConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions, self).__init__()

                            self.yang_name = "conditions"
                            self.yang_parent_name = "statement"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State)), ("match-interface", ("match_interface", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface)), ("match-prefix-set", ("match_prefix_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet)), ("match-neighbor-set", ("match_neighbor_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet)), ("match-tag-set", ("match_tag_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet)), ("igp-conditions", ("igp_conditions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions)), ("openconfig-bgp-policy:bgp-conditions", ("bgp_conditions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions)), ("openconfig-isis-policy:isis-conditions", ("isis_conditions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.match_interface = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface()
                            self.match_interface.parent = self
                            self._children_name_map["match_interface"] = "match-interface"
                            self._children_yang_names.add("match-interface")

                            self.match_prefix_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet()
                            self.match_prefix_set.parent = self
                            self._children_name_map["match_prefix_set"] = "match-prefix-set"
                            self._children_yang_names.add("match-prefix-set")

                            self.match_neighbor_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet()
                            self.match_neighbor_set.parent = self
                            self._children_name_map["match_neighbor_set"] = "match-neighbor-set"
                            self._children_yang_names.add("match-neighbor-set")

                            self.match_tag_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet()
                            self.match_tag_set.parent = self
                            self._children_name_map["match_tag_set"] = "match-tag-set"
                            self._children_yang_names.add("match-tag-set")

                            self.igp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions()
                            self.igp_conditions.parent = self
                            self._children_name_map["igp_conditions"] = "igp-conditions"
                            self._children_yang_names.add("igp-conditions")

                            self.bgp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions()
                            self.bgp_conditions.parent = self
                            self._children_name_map["bgp_conditions"] = "openconfig-bgp-policy:bgp-conditions"
                            self._children_yang_names.add("openconfig-bgp-policy:bgp-conditions")

                            self.isis_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions()
                            self.isis_conditions.parent = self
                            self._children_name_map["isis_conditions"] = "openconfig-isis-policy:isis-conditions"
                            self._children_yang_names.add("openconfig-isis-policy:isis-conditions")
                            self._segment_path = lambda: "conditions"


                        class Config(Entity):
                            """
                            Configuration data for policy conditions
                            
                            .. attribute:: call_policy
                            
                            	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: install_protocol_eq
                            
                            	Condition to check the protocol / method used to install the route into the local routing table
                            	**type**\:  :py:class:`INSTALLPROTOCOLTYPE <ydk.models.openconfig.openconfig_policy_types.INSTALLPROTOCOLTYPE>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('call_policy', YLeaf(YType.str, 'call-policy')),
                                    ('install_protocol_eq', YLeaf(YType.identityref, 'install-protocol-eq')),
                                ])
                                self.call_policy = None
                                self.install_protocol_eq = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.Config, ['call_policy', 'install_protocol_eq'], name, value)


                        class State(Entity):
                            """
                            Operational state data for policy conditions
                            
                            .. attribute:: call_policy
                            
                            	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                            
                            .. attribute:: install_protocol_eq
                            
                            	Condition to check the protocol / method used to install the route into the local routing table
                            	**type**\:  :py:class:`INSTALLPROTOCOLTYPE <ydk.models.openconfig.openconfig_policy_types.INSTALLPROTOCOLTYPE>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('call_policy', YLeaf(YType.str, 'call-policy')),
                                    ('install_protocol_eq', YLeaf(YType.identityref, 'install-protocol-eq')),
                                ])
                                self.call_policy = None
                                self.install_protocol_eq = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.State, ['call_policy', 'install_protocol_eq'], name, value)


                        class MatchInterface(Entity):
                            """
                            Top\-level container for interface match conditions
                            
                            .. attribute:: config
                            
                            	Configuration data for interface match conditions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for interface match conditions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface, self).__init__()

                                self.yang_name = "match-interface"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "match-interface"


                            class Config(Entity):
                                """
                                Configuration data for interface match conditions
                                
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

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface', YLeaf(YType.str, 'interface')),
                                        ('subinterface', YLeaf(YType.str, 'subinterface')),
                                    ])
                                    self.interface = None
                                    self.subinterface = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.Config, ['interface', 'subinterface'], name, value)


                            class State(Entity):
                                """
                                Operational state data for interface match conditions
                                
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

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-interface"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface', YLeaf(YType.str, 'interface')),
                                        ('subinterface', YLeaf(YType.str, 'subinterface')),
                                    ])
                                    self.interface = None
                                    self.subinterface = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchInterface.State, ['interface', 'subinterface'], name, value)


                        class MatchPrefixSet(Entity):
                            """
                            Match a referenced prefix\-set according to the logic
                            defined in the match\-set\-options leaf
                            
                            .. attribute:: config
                            
                            	Configuration data for a prefix\-set condition
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for a prefix\-set condition
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet, self).__init__()

                                self.yang_name = "match-prefix-set"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "match-prefix-set"


                            class Config(Entity):
                                """
                                Configuration data for a prefix\-set condition
                                
                                .. attribute:: prefix_set
                                
                                	References a defined prefix set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-prefix-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_set', YLeaf(YType.str, 'prefix-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.prefix_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.Config, ['prefix_set', 'match_set_options'], name, value)


                            class State(Entity):
                                """
                                Operational state data for a prefix\-set condition
                                
                                .. attribute:: prefix_set
                                
                                	References a defined prefix set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-prefix-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_set', YLeaf(YType.str, 'prefix-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.prefix_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet.State, ['prefix_set', 'match_set_options'], name, value)


                        class MatchNeighborSet(Entity):
                            """
                            Match a referenced neighbor set according to the logic
                            defined in the match\-set\-options\-leaf
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet, self).__init__()

                                self.yang_name = "match-neighbor-set"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "match-neighbor-set"


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: neighbor_set
                                
                                	References a defined neighbor set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-neighbor-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('neighbor_set', YLeaf(YType.str, 'neighbor-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.neighbor_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.Config, ['neighbor_set', 'match_set_options'], name, value)


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: neighbor_set
                                
                                	References a defined neighbor set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-neighbor-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('neighbor_set', YLeaf(YType.str, 'neighbor-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.neighbor_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet.State, ['neighbor_set', 'match_set_options'], name, value)


                        class MatchTagSet(Entity):
                            """
                            Match a referenced tag set according to the logic defined
                            in the match\-options\-set leaf
                            
                            .. attribute:: config
                            
                            	Configuration data for tag\-set conditions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data tag\-set conditions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet, self).__init__()

                                self.yang_name = "match-tag-set"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "match-tag-set"


                            class Config(Entity):
                                """
                                Configuration data for tag\-set conditions
                                
                                .. attribute:: tag_set
                                
                                	References a defined tag set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "match-tag-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tag_set', YLeaf(YType.str, 'tag-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.tag_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.Config, ['tag_set', 'match_set_options'], name, value)


                            class State(Entity):
                                """
                                Operational state data tag\-set conditions
                                
                                .. attribute:: tag_set
                                
                                	References a defined tag set
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                                	**type**\:  :py:class:`MatchSetOptionsRestrictedType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedType>`
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "match-tag-set"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tag_set', YLeaf(YType.str, 'tag-set')),
                                        ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                    ])
                                    self.tag_set = None
                                    self.match_set_options = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet.State, ['tag_set', 'match_set_options'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "igp-conditions"


                        class BgpConditions(Entity):
                            """
                            Top\-level container 
                            
                            .. attribute:: config
                            
                            	Configuration data for BGP\-specific policy conditions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for BGP\-specific policy conditions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State>`
                            
                            .. attribute:: community_count
                            
                            	Value and comparison operations for conditions based on the number of communities in the route update
                            	**type**\:  :py:class:`CommunityCount <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount>`
                            
                            .. attribute:: as_path_length
                            
                            	Value and comparison operations for conditions based on the length of the AS path in the route update
                            	**type**\:  :py:class:`AsPathLength <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength>`
                            
                            .. attribute:: match_community_set
                            
                            	Top\-level container for match conditions on communities. Match a referenced community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:  :py:class:`MatchCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet>`
                            
                            .. attribute:: match_ext_community_set
                            
                            	Match a referenced extended community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:  :py:class:`MatchExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet>`
                            
                            .. attribute:: match_as_path_set
                            
                            	Match a referenced as\-path set according to the logic defined in the match\-set\-options leaf
                            	**type**\:  :py:class:`MatchAsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet>`
                            
                            

                            """

                            _prefix = 'oc-bgp-pol'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions, self).__init__()

                                self.yang_name = "bgp-conditions"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State)), ("community-count", ("community_count", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount)), ("as-path-length", ("as_path_length", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength)), ("match-community-set", ("match_community_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet)), ("match-ext-community-set", ("match_ext_community_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet)), ("match-as-path-set", ("match_as_path_set", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")

                                self.community_count = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount()
                                self.community_count.parent = self
                                self._children_name_map["community_count"] = "community-count"
                                self._children_yang_names.add("community-count")

                                self.as_path_length = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength()
                                self.as_path_length.parent = self
                                self._children_name_map["as_path_length"] = "as-path-length"
                                self._children_yang_names.add("as-path-length")

                                self.match_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet()
                                self.match_community_set.parent = self
                                self._children_name_map["match_community_set"] = "match-community-set"
                                self._children_yang_names.add("match-community-set")

                                self.match_ext_community_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet()
                                self.match_ext_community_set.parent = self
                                self._children_name_map["match_ext_community_set"] = "match-ext-community-set"
                                self._children_yang_names.add("match-ext-community-set")

                                self.match_as_path_set = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet()
                                self.match_as_path_set.parent = self
                                self._children_name_map["match_as_path_set"] = "match-as-path-set"
                                self._children_yang_names.add("match-as-path-set")
                                self._segment_path = lambda: "openconfig-bgp-policy:bgp-conditions"


                            class Config(Entity):
                                """
                                Configuration data for BGP\-specific policy conditions
                                
                                .. attribute:: med_eq
                                
                                	Condition to check if the received MED value is equal to the specified value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: origin_eq
                                
                                	Condition to check if the route origin is equal to the specified value
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: next_hop_in
                                
                                	List of next hop addresses to check for in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: list of str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: afi_safi_in
                                
                                	List of address families which the NLRI may be within
                                	**type**\: list of   :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                                
                                .. attribute:: local_pref_eq
                                
                                	Condition to check if the local pref attribute is equal to the specified value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: route_type
                                
                                	Condition to check the route type in the route update
                                	**type**\:  :py:class:`RouteType <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config.RouteType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('med_eq', YLeaf(YType.uint32, 'med-eq')),
                                        ('origin_eq', YLeaf(YType.enumeration, 'origin-eq')),
                                        ('next_hop_in', YLeafList(YType.str, 'next-hop-in')),
                                        ('afi_safi_in', YLeafList(YType.identityref, 'afi-safi-in')),
                                        ('local_pref_eq', YLeaf(YType.uint32, 'local-pref-eq')),
                                        ('route_type', YLeaf(YType.enumeration, 'route-type')),
                                    ])
                                    self.med_eq = None
                                    self.origin_eq = None
                                    self.next_hop_in = []
                                    self.afi_safi_in = []
                                    self.local_pref_eq = None
                                    self.route_type = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.Config, ['med_eq', 'origin_eq', 'next_hop_in', 'afi_safi_in', 'local_pref_eq', 'route_type'], name, value)

                                class RouteType(Enum):
                                    """
                                    RouteType (Enum Class)

                                    Condition to check the route type in the route update

                                    .. data:: INTERNAL = 0

                                    	route type is internal

                                    .. data:: EXTERNAL = 1

                                    	route type is external

                                    """

                                    INTERNAL = Enum.YLeaf(0, "INTERNAL")

                                    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")



                            class State(Entity):
                                """
                                Operational state data for BGP\-specific policy
                                conditions
                                
                                .. attribute:: med_eq
                                
                                	Condition to check if the received MED value is equal to the specified value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: origin_eq
                                
                                	Condition to check if the route origin is equal to the specified value
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: next_hop_in
                                
                                	List of next hop addresses to check for in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: list of str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: afi_safi_in
                                
                                	List of address families which the NLRI may be within
                                	**type**\: list of   :py:class:`AFISAFITYPE <ydk.models.openconfig.openconfig_bgp_types.AFISAFITYPE>`
                                
                                .. attribute:: local_pref_eq
                                
                                	Condition to check if the local pref attribute is equal to the specified value
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: route_type
                                
                                	Condition to check the route type in the route update
                                	**type**\:  :py:class:`RouteType <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State.RouteType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('med_eq', YLeaf(YType.uint32, 'med-eq')),
                                        ('origin_eq', YLeaf(YType.enumeration, 'origin-eq')),
                                        ('next_hop_in', YLeafList(YType.str, 'next-hop-in')),
                                        ('afi_safi_in', YLeafList(YType.identityref, 'afi-safi-in')),
                                        ('local_pref_eq', YLeaf(YType.uint32, 'local-pref-eq')),
                                        ('route_type', YLeaf(YType.enumeration, 'route-type')),
                                    ])
                                    self.med_eq = None
                                    self.origin_eq = None
                                    self.next_hop_in = []
                                    self.afi_safi_in = []
                                    self.local_pref_eq = None
                                    self.route_type = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.State, ['med_eq', 'origin_eq', 'next_hop_in', 'afi_safi_in', 'local_pref_eq', 'route_type'], name, value)

                                class RouteType(Enum):
                                    """
                                    RouteType (Enum Class)

                                    Condition to check the route type in the route update

                                    .. data:: INTERNAL = 0

                                    	route type is internal

                                    .. data:: EXTERNAL = 1

                                    	route type is external

                                    """

                                    INTERNAL = Enum.YLeaf(0, "INTERNAL")

                                    EXTERNAL = Enum.YLeaf(1, "EXTERNAL")



                            class CommunityCount(Entity):
                                """
                                Value and comparison operations for conditions based on the
                                number of communities in the route update
                                
                                .. attribute:: config
                                
                                	Configuration data for community count condition
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for community count condition
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount, self).__init__()

                                    self.yang_name = "community-count"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "community-count"


                                class Config(Entity):
                                    """
                                    Configuration data for community count condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:  :py:class:`ATTRIBUTECOMPARISON <ydk.models.openconfig.openconfig_policy_types.ATTRIBUTECOMPARISON>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "community-count"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('operator', YLeaf(YType.identityref, 'operator')),
                                            ('value', YLeaf(YType.uint32, 'value')),
                                        ])
                                        self.operator = None
                                        self.value = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.Config, ['operator', 'value'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for community count condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:  :py:class:`ATTRIBUTECOMPARISON <ydk.models.openconfig.openconfig_policy_types.ATTRIBUTECOMPARISON>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "community-count"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('operator', YLeaf(YType.identityref, 'operator')),
                                            ('value', YLeaf(YType.uint32, 'value')),
                                        ])
                                        self.operator = None
                                        self.value = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount.State, ['operator', 'value'], name, value)


                            class AsPathLength(Entity):
                                """
                                Value and comparison operations for conditions based on the
                                length of the AS path in the route update
                                
                                .. attribute:: config
                                
                                	Configuration data for AS path length condition
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for AS path length condition
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength, self).__init__()

                                    self.yang_name = "as-path-length"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "as-path-length"


                                class Config(Entity):
                                    """
                                    Configuration data for AS path length condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:  :py:class:`ATTRIBUTECOMPARISON <ydk.models.openconfig.openconfig_policy_types.ATTRIBUTECOMPARISON>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "as-path-length"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('operator', YLeaf(YType.identityref, 'operator')),
                                            ('value', YLeaf(YType.uint32, 'value')),
                                        ])
                                        self.operator = None
                                        self.value = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.Config, ['operator', 'value'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for AS path length condition
                                    
                                    .. attribute:: operator
                                    
                                    	type of comparison to be performed
                                    	**type**\:  :py:class:`ATTRIBUTECOMPARISON <ydk.models.openconfig.openconfig_policy_types.ATTRIBUTECOMPARISON>`
                                    
                                    .. attribute:: value
                                    
                                    	value to compare with the community count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "as-path-length"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('operator', YLeaf(YType.identityref, 'operator')),
                                            ('value', YLeaf(YType.uint32, 'value')),
                                        ])
                                        self.operator = None
                                        self.value = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength.State, ['operator', 'value'], name, value)


                            class MatchCommunitySet(Entity):
                                """
                                Top\-level container for match conditions on communities.
                                Match a referenced community\-set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on communities
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data 
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet, self).__init__()

                                    self.yang_name = "match-community-set"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "match-community-set"


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on communities
                                    
                                    .. attribute:: community_set
                                    
                                    	References a defined community set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-community-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('community_set', YLeaf(YType.str, 'community-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.community_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.Config, ['community_set', 'match_set_options'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data 
                                    
                                    .. attribute:: community_set
                                    
                                    	References a defined community set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-community-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('community_set', YLeaf(YType.str, 'community-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.community_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet.State, ['community_set', 'match_set_options'], name, value)


                            class MatchExtCommunitySet(Entity):
                                """
                                Match a referenced extended community\-set according to the
                                logic defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on extended communities
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for match conditions on extended communities
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet, self).__init__()

                                    self.yang_name = "match-ext-community-set"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "match-ext-community-set"


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on extended
                                    communities
                                    
                                    .. attribute:: ext_community_set
                                    
                                    	References a defined extended community set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-ext-community-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ext_community_set', YLeaf(YType.str, 'ext-community-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.ext_community_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.Config, ['ext_community_set', 'match_set_options'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for match conditions on extended
                                    communities
                                    
                                    .. attribute:: ext_community_set
                                    
                                    	References a defined extended community set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-ext-community-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ext_community_set', YLeaf(YType.str, 'ext-community-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.ext_community_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet.State, ['ext_community_set', 'match_set_options'], name, value)


                            class MatchAsPathSet(Entity):
                                """
                                Match a referenced as\-path set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: config
                                
                                	Configuration data for match conditions on AS path set
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for match conditions on AS path set
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet, self).__init__()

                                    self.yang_name = "match-as-path-set"
                                    self.yang_parent_name = "bgp-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "match-as-path-set"


                                class Config(Entity):
                                    """
                                    Configuration data for match conditions on AS path set
                                    
                                    .. attribute:: as_path_set
                                    
                                    	References a defined AS path set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "match-as-path-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_path_set', YLeaf(YType.str, 'as-path-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.as_path_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.Config, ['as_path_set', 'match_set_options'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for match conditions on AS
                                    path set
                                    
                                    .. attribute:: as_path_set
                                    
                                    	References a defined AS path set
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                                    
                                    .. attribute:: match_set_options
                                    
                                    	Optional parameter that governs the behaviour of the match operation
                                    	**type**\:  :py:class:`MatchSetOptionsType <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "match-as-path-set"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_path_set', YLeaf(YType.str, 'as-path-set')),
                                            ('match_set_options', YLeaf(YType.enumeration, 'match-set-options')),
                                        ])
                                        self.as_path_set = None
                                        self.match_set_options = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet.State, ['as_path_set', 'match_set_options'], name, value)


                        class IsisConditions(Entity):
                            """
                            Match conditions relating to the IS\-IS protocol
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to IS\-IS match conditions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state parameters relating to IS\-IS match conditions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.State>`
                            
                            

                            """

                            _prefix = 'oc-isis-pol'
                            _revision = '2017-05-15'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions, self).__init__()

                                self.yang_name = "isis-conditions"
                                self.yang_parent_name = "conditions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "openconfig-isis-policy:isis-conditions"


                            class Config(Entity):
                                """
                                Configuration parameters relating to IS\-IS match
                                conditions
                                
                                .. attribute:: level_eq
                                
                                	Match the level that the IS\-IS prefix is within. This can be used in the case that import or export policies refer to an IS\-IS instance that has multiple levels configured within it
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                

                                """

                                _prefix = 'oc-isis-pol'
                                _revision = '2017-05-15'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "isis-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level_eq', YLeaf(YType.uint8, 'level-eq')),
                                    ])
                                    self.level_eq = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.Config, ['level_eq'], name, value)


                            class State(Entity):
                                """
                                Operational state parameters relating to IS\-IS match
                                conditions
                                
                                .. attribute:: level_eq
                                
                                	Match the level that the IS\-IS prefix is within. This can be used in the case that import or export policies refer to an IS\-IS instance that has multiple levels configured within it
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                

                                """

                                _prefix = 'oc-isis-pol'
                                _revision = '2017-05-15'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "isis-conditions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level_eq', YLeaf(YType.uint8, 'level-eq')),
                                    ])
                                    self.level_eq = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IsisConditions.State, ['level_eq'], name, value)


                    class Actions(Entity):
                        """
                        Top\-level container for policy action statements
                        
                        .. attribute:: config
                        
                        	Configuration data for policy actions
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for policy actions
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State>`
                        
                        .. attribute:: igp_actions
                        
                        	Actions to set IGP route attributes; these actions apply to multiple IGPs
                        	**type**\:  :py:class:`IgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions>`
                        
                        .. attribute:: bgp_actions
                        
                        	Top\-level container for BGP\-specific actions
                        	**type**\:  :py:class:`BgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions>`
                        
                        .. attribute:: isis_actions
                        
                        	Actions that can be performed by IS\-IS within a policy
                        	**type**\:  :py:class:`IsisActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions>`
                        
                        

                        """

                        _prefix = 'oc-rpol'
                        _revision = '2016-05-12'

                        def __init__(self):
                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions, self).__init__()

                            self.yang_name = "actions"
                            self.yang_parent_name = "statement"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State)), ("igp-actions", ("igp_actions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions)), ("openconfig-bgp-policy:bgp-actions", ("bgp_actions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions)), ("openconfig-isis-policy:isis-actions", ("isis_actions", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.igp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions()
                            self.igp_actions.parent = self
                            self._children_name_map["igp_actions"] = "igp-actions"
                            self._children_yang_names.add("igp-actions")

                            self.bgp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions()
                            self.bgp_actions.parent = self
                            self._children_name_map["bgp_actions"] = "openconfig-bgp-policy:bgp-actions"
                            self._children_yang_names.add("openconfig-bgp-policy:bgp-actions")

                            self.isis_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions()
                            self.isis_actions.parent = self
                            self._children_name_map["isis_actions"] = "openconfig-isis-policy:isis-actions"
                            self._children_yang_names.add("openconfig-isis-policy:isis-actions")
                            self._segment_path = lambda: "actions"


                        class Config(Entity):
                            """
                            Configuration data for policy actions
                            
                            .. attribute:: accept_route
                            
                            	accepts the route into the routing table
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: reject_route
                            
                            	rejects the route
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('accept_route', YLeaf(YType.empty, 'accept-route')),
                                    ('reject_route', YLeaf(YType.empty, 'reject-route')),
                                ])
                                self.accept_route = None
                                self.reject_route = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.Config, ['accept_route', 'reject_route'], name, value)


                        class State(Entity):
                            """
                            Operational state data for policy actions
                            
                            .. attribute:: accept_route
                            
                            	accepts the route into the routing table
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: reject_route
                            
                            	rejects the route
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('accept_route', YLeaf(YType.empty, 'accept-route')),
                                    ('reject_route', YLeaf(YType.empty, 'reject-route')),
                                ])
                                self.accept_route = None
                                self.reject_route = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.State, ['accept_route', 'reject_route'], name, value)


                        class IgpActions(Entity):
                            """
                            Actions to set IGP route attributes; these actions
                            apply to multiple IGPs
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State>`
                            
                            

                            """

                            _prefix = 'oc-rpol'
                            _revision = '2016-05-12'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions, self).__init__()

                                self.yang_name = "igp-actions"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "igp-actions"


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: set_tag
                                
                                	Set the tag value for OSPF or IS\-IS routes
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "igp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_tag', YLeaf(YType.str, 'set-tag')),
                                    ])
                                    self.set_tag = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.Config, ['set_tag'], name, value)


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: set_tag
                                
                                	Set the tag value for OSPF or IS\-IS routes
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                

                                """

                                _prefix = 'oc-rpol'
                                _revision = '2016-05-12'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "igp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_tag', YLeaf(YType.str, 'set-tag')),
                                    ])
                                    self.set_tag = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions.State, ['set_tag'], name, value)


                        class BgpActions(Entity):
                            """
                            Top\-level container for BGP\-specific actions
                            
                            .. attribute:: config
                            
                            	Configuration data for BGP\-specific actions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for BGP\-specific actions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State>`
                            
                            .. attribute:: set_as_path_prepend
                            
                            	action to prepend local AS number to the AS\-path a specified number of times
                            	**type**\:  :py:class:`SetAsPathPrepend <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend>`
                            
                            .. attribute:: set_community
                            
                            	Action to set the community attributes of the route, along with options to modify how the community is modified. Communities may be set using an inline list OR reference to an existing defined set (not both)
                            	**type**\:  :py:class:`SetCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity>`
                            
                            .. attribute:: set_ext_community
                            
                            	Action to set the extended community attributes of the route, along with options to modify how the community is modified. Extended communities may be set using an inline list OR a reference to an existing defined set (but not both)
                            	**type**\:  :py:class:`SetExtCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity>`
                            
                            

                            """

                            _prefix = 'oc-bgp-pol'
                            _revision = '2016-06-21'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions, self).__init__()

                                self.yang_name = "bgp-actions"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State)), ("set-as-path-prepend", ("set_as_path_prepend", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend)), ("set-community", ("set_community", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity)), ("set-ext-community", ("set_ext_community", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")

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
                                self._segment_path = lambda: "openconfig-bgp-policy:bgp-actions"


                            class Config(Entity):
                                """
                                Configuration data for BGP\-specific actions
                                
                                .. attribute:: set_route_origin
                                
                                	set the origin attribute to the specified value
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: set_local_pref
                                
                                	set the local pref attribute on the route update
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: set_next_hop
                                
                                	set the next\-hop attribute in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\:  :py:class:`BgpNextHopType <ydk.models.openconfig.openconfig_bgp_policy.BgpNextHopType>`
                                
                                .. attribute:: set_med
                                
                                	set the med metric attribute in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** ^[+\-][0\-9]+
                                
                                		**type**\:  :py:class:`BgpSetMedType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetMedType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "bgp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_route_origin', YLeaf(YType.enumeration, 'set-route-origin')),
                                        ('set_local_pref', YLeaf(YType.uint32, 'set-local-pref')),
                                        ('set_next_hop', YLeaf(YType.str, 'set-next-hop')),
                                        ('set_med', YLeaf(YType.str, 'set-med')),
                                    ])
                                    self.set_route_origin = None
                                    self.set_local_pref = None
                                    self.set_next_hop = None
                                    self.set_med = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.Config, ['set_route_origin', 'set_local_pref', 'set_next_hop', 'set_med'], name, value)


                            class State(Entity):
                                """
                                Operational state data for BGP\-specific actions
                                
                                .. attribute:: set_route_origin
                                
                                	set the origin attribute to the specified value
                                	**type**\:  :py:class:`BgpOriginAttrType <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrType>`
                                
                                .. attribute:: set_local_pref
                                
                                	set the local pref attribute on the route update
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: set_next_hop
                                
                                	set the next\-hop attribute in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\:  :py:class:`BgpNextHopType <ydk.models.openconfig.openconfig_bgp_policy.BgpNextHopType>`
                                
                                .. attribute:: set_med
                                
                                	set the med metric attribute in the route update
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** ^[+\-][0\-9]+
                                
                                		**type**\:  :py:class:`BgpSetMedType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetMedType>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "bgp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_route_origin', YLeaf(YType.enumeration, 'set-route-origin')),
                                        ('set_local_pref', YLeaf(YType.uint32, 'set-local-pref')),
                                        ('set_next_hop', YLeaf(YType.str, 'set-next-hop')),
                                        ('set_med', YLeaf(YType.str, 'set-med')),
                                    ])
                                    self.set_route_origin = None
                                    self.set_local_pref = None
                                    self.set_next_hop = None
                                    self.set_med = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.State, ['set_route_origin', 'set_local_pref', 'set_next_hop', 'set_med'], name, value)


                            class SetAsPathPrepend(Entity):
                                """
                                action to prepend local AS number to the AS\-path a
                                specified number of times
                                
                                .. attribute:: config
                                
                                	Configuration data for the AS path prepend action
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the AS path prepend action
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend, self).__init__()

                                    self.yang_name = "set-as-path-prepend"
                                    self.yang_parent_name = "bgp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "set-as-path-prepend"


                                class Config(Entity):
                                    """
                                    Configuration data for the AS path prepend action
                                    
                                    .. attribute:: repeat_n
                                    
                                    	Number of times to prepend the local AS number to the AS path.  The value should be between 1 and the maximum supported by the implementation
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-as-path-prepend"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('repeat_n', YLeaf(YType.uint8, 'repeat-n')),
                                        ])
                                        self.repeat_n = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.Config, ['repeat_n'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for the AS path prepend action
                                    
                                    .. attribute:: repeat_n
                                    
                                    	Number of times to prepend the local AS number to the AS path.  The value should be between 1 and the maximum supported by the implementation
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-as-path-prepend"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('repeat_n', YLeaf(YType.uint8, 'repeat-n')),
                                        ])
                                        self.repeat_n = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend.State, ['repeat_n'], name, value)


                            class SetCommunity(Entity):
                                """
                                Action to set the community attributes of the route, along
                                with options to modify how the community is modified.
                                Communities may be set using an inline list OR
                                reference to an existing defined set (not both).
                                
                                .. attribute:: config
                                
                                	Configuration data for the set\-community action
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the set\-community action
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State>`
                                
                                .. attribute:: inline
                                
                                	Set the community values for the action inline with a list
                                	**type**\:  :py:class:`Inline <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline>`
                                
                                .. attribute:: reference
                                
                                	Provide a reference to a defined community set for the set\-community action
                                	**type**\:  :py:class:`Reference <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity, self).__init__()

                                    self.yang_name = "set-community"
                                    self.yang_parent_name = "bgp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State)), ("inline", ("inline", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline)), ("reference", ("reference", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")

                                    self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline()
                                    self.inline.parent = self
                                    self._children_name_map["inline"] = "inline"
                                    self._children_yang_names.add("inline")

                                    self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference()
                                    self.reference.parent = self
                                    self._children_name_map["reference"] = "reference"
                                    self._children_yang_names.add("reference")
                                    self._segment_path = lambda: "set-community"


                                class Config(Entity):
                                    """
                                    Configuration data for the set\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:  :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:  :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('method', YLeaf(YType.enumeration, 'method')),
                                            ('options', YLeaf(YType.enumeration, 'options')),
                                        ])
                                        self.method = None
                                        self.options = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Config, ['method', 'options'], name, value)

                                    class Method(Enum):
                                        """
                                        Method (Enum Class)

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



                                class State(Entity):
                                    """
                                    Operational state data for the set\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:  :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:  :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('method', YLeaf(YType.enumeration, 'method')),
                                            ('options', YLeaf(YType.enumeration, 'options')),
                                        ])
                                        self.method = None
                                        self.options = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.State, ['method', 'options'], name, value)

                                    class Method(Enum):
                                        """
                                        Method (Enum Class)

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



                                class Inline(Entity):
                                    """
                                    Set the community values for the action inline with
                                    a list.
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data or inline specification of set\-community action
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data or inline specification of set\-community action
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline, self).__init__()

                                        self.yang_name = "inline"
                                        self.yang_parent_name = "set-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "inline"


                                    class Config(Entity):
                                        """
                                        Configuration data or inline specification of set\-community
                                        action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the community values for the update inline with a list
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "inline"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('communities', YLeafList(YType.str, 'communities')),
                                            ])
                                            self.communities = []
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.Config, ['communities'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data or inline specification of
                                        set\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the community values for the update inline with a list
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: list of int
                                        
                                        			**range:** 65536..4294901759
                                        
                                        		**type**\: list of str
                                        
                                        			**pattern:** ([0\-9]+\:[0\-9]+)
                                        
                                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "inline"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('communities', YLeafList(YType.str, 'communities')),
                                            ])
                                            self.communities = []
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Inline.State, ['communities'], name, value)


                                class Reference(Entity):
                                    """
                                    Provide a reference to a defined community set for the
                                    set\-community action
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for referening a community\-set in the set\-community action
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for referening a community\-set in the set\-community action
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference, self).__init__()

                                        self.yang_name = "reference"
                                        self.yang_parent_name = "set-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "reference"


                                    class Config(Entity):
                                        """
                                        Configuration data for referening a community\-set in the
                                        set\-community action
                                        
                                        .. attribute:: community_set_ref
                                        
                                        	References a defined community set by name
                                        	**type**\: str
                                        
                                        	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "reference"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('community_set_ref', YLeaf(YType.str, 'community-set-ref')),
                                            ])
                                            self.community_set_ref = None
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.Config, ['community_set_ref'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for referening a community\-set
                                        in the set\-community action
                                        
                                        .. attribute:: community_set_ref
                                        
                                        	References a defined community set by name
                                        	**type**\: str
                                        
                                        	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "reference"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('community_set_ref', YLeaf(YType.str, 'community-set-ref')),
                                            ])
                                            self.community_set_ref = None
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity.Reference.State, ['community_set_ref'], name, value)


                            class SetExtCommunity(Entity):
                                """
                                Action to set the extended community attributes of the
                                route, along with options to modify how the community is
                                modified. Extended communities may be set using an inline
                                list OR a reference to an existing defined set (but not
                                both).
                                
                                .. attribute:: config
                                
                                	Configuration data for the set\-ext\-community action
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the set\-ext\-community action
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State>`
                                
                                .. attribute:: inline
                                
                                	Set the extended community values for the action inline with a list
                                	**type**\:  :py:class:`Inline <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline>`
                                
                                .. attribute:: reference
                                
                                	Provide a reference to an extended community set for the set\-ext\-community action
                                	**type**\:  :py:class:`Reference <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference>`
                                
                                

                                """

                                _prefix = 'oc-bgp-pol'
                                _revision = '2016-06-21'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity, self).__init__()

                                    self.yang_name = "set-ext-community"
                                    self.yang_parent_name = "bgp-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State)), ("inline", ("inline", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline)), ("reference", ("reference", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")

                                    self.inline = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline()
                                    self.inline.parent = self
                                    self._children_name_map["inline"] = "inline"
                                    self._children_yang_names.add("inline")

                                    self.reference = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference()
                                    self.reference.parent = self
                                    self._children_name_map["reference"] = "reference"
                                    self._children_yang_names.add("reference")
                                    self._segment_path = lambda: "set-ext-community"


                                class Config(Entity):
                                    """
                                    Configuration data for the set\-ext\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:  :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:  :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "set-ext-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('method', YLeaf(YType.enumeration, 'method')),
                                            ('options', YLeaf(YType.enumeration, 'options')),
                                        ])
                                        self.method = None
                                        self.options = None
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Config, ['method', 'options'], name, value)

                                    class Method(Enum):
                                        """
                                        Method (Enum Class)

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



                                class State(Entity):
                                    """
                                    Operational state data for the set\-ext\-community action
                                    
                                    .. attribute:: method
                                    
                                    	Indicates the method used to specify the extended communities for the set\-ext\-community action
                                    	**type**\:  :py:class:`Method <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State.Method>`
                                    
                                    .. attribute:: options
                                    
                                    	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                    	**type**\:  :py:class:`BgpSetCommunityOptionType <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionType>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "set-ext-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('method', YLeaf(YType.enumeration, 'method')),
                                            ('options', YLeaf(YType.enumeration, 'options')),
                                        ])
                                        self.method = None
                                        self.options = None
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.State, ['method', 'options'], name, value)

                                    class Method(Enum):
                                        """
                                        Method (Enum Class)

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



                                class Inline(Entity):
                                    """
                                    Set the extended community values for the action inline with
                                    a list.
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data or inline specification of set\-ext\-community action
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data or inline specification of set\-ext\-community action
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline, self).__init__()

                                        self.yang_name = "inline"
                                        self.yang_parent_name = "set-ext-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "inline"


                                    class Config(Entity):
                                        """
                                        Configuration data or inline specification of
                                        set\-ext\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the extended community values for the update inline with a list
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
                                        
                                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "inline"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('communities', YLeafList(YType.str, 'communities')),
                                            ])
                                            self.communities = []
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.Config, ['communities'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data or inline specification of
                                        set\-ext\-community action
                                        
                                        .. attribute:: communities
                                        
                                        	Set the extended community values for the update inline with a list
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
                                        
                                        		**type**\: list of   :py:class:`BGPWELLKNOWNSTDCOMMUNITY <ydk.models.openconfig.openconfig_bgp_types.BGPWELLKNOWNSTDCOMMUNITY>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "inline"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('communities', YLeafList(YType.str, 'communities')),
                                            ])
                                            self.communities = []
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Inline.State, ['communities'], name, value)


                                class Reference(Entity):
                                    """
                                    Provide a reference to an extended community set for the
                                    set\-ext\-community action
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for referening an extended community\-set in the set\-ext\-community action
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for referening an extended community\-set in the set\-ext\-community action
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-bgp-pol'
                                    _revision = '2016-06-21'

                                    def __init__(self):
                                        super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference, self).__init__()

                                        self.yang_name = "reference"
                                        self.yang_parent_name = "set-ext-community"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "reference"


                                    class Config(Entity):
                                        """
                                        Configuration data for referening an extended
                                        community\-set in the set\-ext\-community action
                                        
                                        .. attribute:: ext_community_set_ref
                                        
                                        	References a defined extended community set by name
                                        	**type**\: str
                                        
                                        	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "reference"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ext_community_set_ref', YLeaf(YType.str, 'ext-community-set-ref')),
                                            ])
                                            self.ext_community_set_ref = None
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.Config, ['ext_community_set_ref'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for referening an extended
                                        community\-set in the set\-ext\-community action
                                        
                                        .. attribute:: ext_community_set_ref
                                        
                                        	References a defined extended community set by name
                                        	**type**\: str
                                        
                                        	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                        
                                        

                                        """

                                        _prefix = 'oc-bgp-pol'
                                        _revision = '2016-06-21'

                                        def __init__(self):
                                            super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "reference"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ext_community_set_ref', YLeaf(YType.str, 'ext-community-set-ref')),
                                            ])
                                            self.ext_community_set_ref = None
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity.Reference.State, ['ext_community_set_ref'], name, value)


                        class IsisActions(Entity):
                            """
                            Actions that can be performed by IS\-IS within a policy
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to IS\-IS actions
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state associated with IS\-IS actions
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.State>`
                            
                            

                            """

                            _prefix = 'oc-isis-pol'
                            _revision = '2017-05-15'

                            def __init__(self):
                                super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions, self).__init__()

                                self.yang_name = "isis-actions"
                                self.yang_parent_name = "actions"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("config", ("config", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.Config)), ("state", ("state", RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.State))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.config = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "openconfig-isis-policy:isis-actions"


                            class Config(Entity):
                                """
                                Configuration parameters relating to IS\-IS actions
                                
                                .. attribute:: set_level
                                
                                	Set the level that a prefix is to be imported into
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: set_metric_type
                                
                                	Set the type of metric that is to be specified when the set metric leaf is specified
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: set_metric
                                
                                	Set the metric of the IS\-IS prefix
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                

                                """

                                _prefix = 'oc-isis-pol'
                                _revision = '2017-05-15'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "isis-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_level', YLeaf(YType.uint8, 'set-level')),
                                        ('set_metric_type', YLeaf(YType.uint8, 'set-metric-type')),
                                        ('set_metric', YLeaf(YType.uint32, 'set-metric')),
                                    ])
                                    self.set_level = None
                                    self.set_metric_type = None
                                    self.set_metric = None
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.Config, ['set_level', 'set_metric_type', 'set_metric'], name, value)


                            class State(Entity):
                                """
                                Operational state associated with IS\-IS actions
                                
                                .. attribute:: set_level
                                
                                	Set the level that a prefix is to be imported into
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: set_metric_type
                                
                                	Set the type of metric that is to be specified when the set metric leaf is specified
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: set_metric
                                
                                	Set the metric of the IS\-IS prefix
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                

                                """

                                _prefix = 'oc-isis-pol'
                                _revision = '2017-05-15'

                                def __init__(self):
                                    super(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "isis-actions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('set_level', YLeaf(YType.uint8, 'set-level')),
                                        ('set_metric_type', YLeaf(YType.uint8, 'set-metric-type')),
                                        ('set_metric', YLeaf(YType.uint32, 'set-metric')),
                                    ])
                                    self.set_level = None
                                    self.set_metric_type = None
                                    self.set_metric = None
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IsisActions.State, ['set_level', 'set_metric_type', 'set_metric'], name, value)

    def clone_ptr(self):
        self._top_entity = RoutingPolicy()
        return self._top_entity

