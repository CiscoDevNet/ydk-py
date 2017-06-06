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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DefaultPolicyTypeEnum(Enum):
    """
    DefaultPolicyTypeEnum

    type used to specify default route disposition in

    a policy chain

    .. data:: ACCEPT_ROUTE = 0

    	default policy to accept the route

    .. data:: REJECT_ROUTE = 1

    	default policy to reject the route

    """

    ACCEPT_ROUTE = 0

    REJECT_ROUTE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
        return meta._meta_table['DefaultPolicyTypeEnum']



class RoutingPolicy(object):
    """
    top\-level container for all routing policy configuration
    
    .. attribute:: defined_sets
    
    	Predefined sets of attributes used in policy match statements
    	**type**\:   :py:class:`DefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets>`
    
    .. attribute:: policy_definitions
    
    	Enclosing container for the list of top\-level policy definitions
    	**type**\:   :py:class:`PolicyDefinitions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions>`
    
    

    """

    _prefix = 'rpol'
    _revision = '2015-10-09'

    def __init__(self):
        self.defined_sets = RoutingPolicy.DefinedSets()
        self.defined_sets.parent = self
        self.policy_definitions = RoutingPolicy.PolicyDefinitions()
        self.policy_definitions.parent = self


    class DefinedSets(object):
        """
        Predefined sets of attributes used in policy match
        statements
        
        .. attribute:: bgp_defined_sets
        
        	BGP\-related set definitions for policy match conditions
        	**type**\:   :py:class:`BgpDefinedSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets>`
        
        .. attribute:: neighbor_sets
        
        	Enclosing container for defined neighbor sets for matching
        	**type**\:   :py:class:`NeighborSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets>`
        
        .. attribute:: prefix_sets
        
        	Enclosing container for defined prefix sets for matching
        	**type**\:   :py:class:`PrefixSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets>`
        
        .. attribute:: tag_sets
        
        	Enclosing container for defined tag sets for matching
        	**type**\:   :py:class:`TagSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets>`
        
        

        """

        _prefix = 'rpol'
        _revision = '2015-10-09'

        def __init__(self):
            self.parent = None
            self.bgp_defined_sets = RoutingPolicy.DefinedSets.BgpDefinedSets()
            self.bgp_defined_sets.parent = self
            self.neighbor_sets = RoutingPolicy.DefinedSets.NeighborSets()
            self.neighbor_sets.parent = self
            self.prefix_sets = RoutingPolicy.DefinedSets.PrefixSets()
            self.prefix_sets.parent = self
            self.tag_sets = RoutingPolicy.DefinedSets.TagSets()
            self.tag_sets.parent = self


        class PrefixSets(object):
            """
            Enclosing container for defined prefix sets for matching
            
            .. attribute:: prefix_set
            
            	List of the defined prefix sets
            	**type**\: list of    :py:class:`PrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.prefix_set = YList()
                self.prefix_set.parent = self
                self.prefix_set.name = 'prefix_set'


            class PrefixSet(object):
                """
                List of the defined prefix sets
                
                .. attribute:: prefix_set_name  <key>
                
                	name / label of the prefix set \-\- this is used to reference the set in match conditions
                	**type**\:  str
                
                .. attribute:: prefix
                
                	List of prefix expressions that are part of the set
                	**type**\: list of    :py:class:`Prefix <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.prefix_set_name = None
                    self.prefix = YList()
                    self.prefix.parent = self
                    self.prefix.name = 'prefix'


                class Prefix(object):
                    """
                    List of prefix expressions that are part of the set
                    
                    .. attribute:: ip_prefix  <key>
                    
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
                    .. attribute:: masklength_range  <key>
                    
                    	Defines a range for the masklength, or 'exact' if the prefix has an exact length.  Example\: 10.3.192.0/21 through 10.3.192.0/24 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: 21..24.  Example\: 10.3.192.0/21 would be expressed as prefix\: 10.3.192.0/21, masklength\-range\: exact
                    	**type**\:  str
                    
                    	**pattern:** ^([0\-9]+\\.\\.[0\-9]+)\|exact$
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.ip_prefix = None
                        self.masklength_range = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip_prefix is None:
                            raise YPYModelError('Key property ip_prefix is None')
                        if self.masklength_range is None:
                            raise YPYModelError('Key property masklength_range is None')

                        return self.parent._common_path +'/openconfig-routing-policy:prefix[openconfig-routing-policy:ip-prefix = ' + str(self.ip_prefix) + '][openconfig-routing-policy:masklength-range = ' + str(self.masklength_range) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip_prefix is not None:
                            return True

                        if self.masklength_range is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix']['meta_info']

                @property
                def _common_path(self):
                    if self.prefix_set_name is None:
                        raise YPYModelError('Key property prefix_set_name is None')

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:prefix-sets/openconfig-routing-policy:prefix-set[openconfig-routing-policy:prefix-set-name = ' + str(self.prefix_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.prefix_set_name is not None:
                        return True

                    if self.prefix is not None:
                        for child_ref in self.prefix:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:prefix-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prefix_set is not None:
                    for child_ref in self.prefix_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info']


        class NeighborSets(object):
            """
            Enclosing container for defined neighbor sets for matching
            
            .. attribute:: neighbor_set
            
            	Definitions for neighbor sets
            	**type**\: list of    :py:class:`NeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.neighbor_set = YList()
                self.neighbor_set.parent = self
                self.neighbor_set.name = 'neighbor_set'


            class NeighborSet(object):
                """
                Definitions for neighbor sets
                
                .. attribute:: neighbor_set_name  <key>
                
                	name / label of the neighbor set \-\- this is used to reference the set in match conditions
                	**type**\:  str
                
                .. attribute:: neighbor
                
                	list of addresses that are part of the neighbor set
                	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.neighbor_set_name = None
                    self.neighbor = YList()
                    self.neighbor.parent = self
                    self.neighbor.name = 'neighbor'


                class Neighbor(object):
                    """
                    list of addresses that are part of the neighbor set
                    
                    .. attribute:: address  <key>
                    
                    	IP address of the neighbor set member
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')

                        return self.parent._common_path +'/openconfig-routing-policy:neighbor[openconfig-routing-policy:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor']['meta_info']

                @property
                def _common_path(self):
                    if self.neighbor_set_name is None:
                        raise YPYModelError('Key property neighbor_set_name is None')

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:neighbor-sets/openconfig-routing-policy:neighbor-set[openconfig-routing-policy:neighbor-set-name = ' + str(self.neighbor_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.neighbor_set_name is not None:
                        return True

                    if self.neighbor is not None:
                        for child_ref in self.neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:neighbor-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.neighbor_set is not None:
                    for child_ref in self.neighbor_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info']


        class TagSets(object):
            """
            Enclosing container for defined tag sets for matching
            
            .. attribute:: tag_set
            
            	Definitions for tag sets
            	**type**\: list of    :py:class:`TagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.tag_set = YList()
                self.tag_set.parent = self
                self.tag_set.name = 'tag_set'


            class TagSet(object):
                """
                Definitions for tag sets
                
                .. attribute:: tag_set_name  <key>
                
                	name / label of the tag set \-\- this is used to reference the set in match conditions
                	**type**\:  str
                
                .. attribute:: tag
                
                	list of tags that are part of the tag set
                	**type**\: list of    :py:class:`Tag <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet.Tag>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.tag_set_name = None
                    self.tag = YList()
                    self.tag.parent = self
                    self.tag.name = 'tag'


                class Tag(object):
                    """
                    list of tags that are part of the tag set
                    
                    .. attribute:: value  <key>
                    
                    	Value of the tag set member
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.value is None:
                            raise YPYModelError('Key property value is None')

                        return self.parent._common_path +'/openconfig-routing-policy:tag[openconfig-routing-policy:value = ' + str(self.value) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet.Tag']['meta_info']

                @property
                def _common_path(self):
                    if self.tag_set_name is None:
                        raise YPYModelError('Key property tag_set_name is None')

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:tag-sets/openconfig-routing-policy:tag-set[openconfig-routing-policy:tag-set-name = ' + str(self.tag_set_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.tag_set_name is not None:
                        return True

                    if self.tag is not None:
                        for child_ref in self.tag:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-routing-policy:tag-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.tag_set is not None:
                    for child_ref in self.tag_set:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info']


        class BgpDefinedSets(object):
            """
            BGP\-related set definitions for policy match conditions
            
            .. attribute:: as_path_sets
            
            	Enclosing container for AS path sets
            	**type**\:   :py:class:`AsPathSets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets>`
            
            .. attribute:: community_sets
            
            	Enclosing container for community sets
            	**type**\:   :py:class:`CommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets>`
            
            .. attribute:: ext_community_sets
            
            	Enclosing container for extended community sets
            	**type**\:   :py:class:`ExtCommunitySets <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets>`
            
            

            """

            _prefix = 'bgp-pol'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.as_path_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets()
                self.as_path_sets.parent = self
                self.community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets()
                self.community_sets.parent = self
                self.ext_community_sets = RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets()
                self.ext_community_sets.parent = self


            class CommunitySets(object):
                """
                Enclosing container for community sets
                
                .. attribute:: community_set
                
                	Definitions for community sets
                	**type**\: list of    :py:class:`CommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                
                

                """

                _prefix = 'bgp-pol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.community_set = YList()
                    self.community_set.parent = self
                    self.community_set.name = 'community_set'


                class CommunitySet(object):
                    """
                    Definitions for community sets
                    
                    .. attribute:: community_set_name  <key>
                    
                    	name / label of the community set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
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
                    

                    """

                    _prefix = 'bgp-pol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.community_set_name = None
                        self.community_member = YLeafList()
                        self.community_member.parent = self
                        self.community_member.name = 'community_member'

                    @property
                    def _common_path(self):
                        if self.community_set_name is None:
                            raise YPYModelError('Key property community_set_name is None')

                        return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:community-sets/openconfig-bgp-policy:community-set[openconfig-bgp-policy:community-set-name = ' + str(self.community_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.community_set_name is not None:
                            return True

                        if self.community_member is not None:
                            for child in self.community_member:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:community-sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.community_set is not None:
                        for child_ref in self.community_set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets']['meta_info']


            class ExtCommunitySets(object):
                """
                Enclosing container for extended community sets
                
                .. attribute:: ext_community_set
                
                	Definitions for extended community sets
                	**type**\: list of    :py:class:`ExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                
                

                """

                _prefix = 'bgp-pol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.ext_community_set = YList()
                    self.ext_community_set.parent = self
                    self.ext_community_set.name = 'ext_community_set'


                class ExtCommunitySet(object):
                    """
                    Definitions for extended community sets
                    
                    .. attribute:: ext_community_set_name  <key>
                    
                    	name / label of the extended community set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
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
                    

                    """

                    _prefix = 'bgp-pol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.ext_community_set_name = None
                        self.ext_community_member = YLeafList()
                        self.ext_community_member.parent = self
                        self.ext_community_member.name = 'ext_community_member'

                    @property
                    def _common_path(self):
                        if self.ext_community_set_name is None:
                            raise YPYModelError('Key property ext_community_set_name is None')

                        return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:ext-community-sets/openconfig-bgp-policy:ext-community-set[openconfig-bgp-policy:ext-community-set-name = ' + str(self.ext_community_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ext_community_set_name is not None:
                            return True

                        if self.ext_community_member is not None:
                            for child in self.ext_community_member:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:ext-community-sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ext_community_set is not None:
                        for child_ref in self.ext_community_set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets']['meta_info']


            class AsPathSets(object):
                """
                Enclosing container for AS path sets
                
                .. attribute:: as_path_set
                
                	Definitions for AS path sets
                	**type**\: list of    :py:class:`AsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                
                

                """

                _prefix = 'bgp-pol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.as_path_set = YList()
                    self.as_path_set.parent = self
                    self.as_path_set.name = 'as_path_set'


                class AsPathSet(object):
                    """
                    Definitions for AS path sets
                    
                    .. attribute:: as_path_set_name  <key>
                    
                    	name of the AS path set \-\- this is used to reference the set in match conditions
                    	**type**\:  str
                    
                    .. attribute:: as_path_set_member
                    
                    	AS path expression \-\- list of ASes in the set
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'bgp-pol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.as_path_set_name = None
                        self.as_path_set_member = YLeafList()
                        self.as_path_set_member.parent = self
                        self.as_path_set_member.name = 'as_path_set_member'

                    @property
                    def _common_path(self):
                        if self.as_path_set_name is None:
                            raise YPYModelError('Key property as_path_set_name is None')

                        return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:as-path-sets/openconfig-bgp-policy:as-path-set[openconfig-bgp-policy:as-path-set-name = ' + str(self.as_path_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.as_path_set_name is not None:
                            return True

                        if self.as_path_set_member is not None:
                            for child in self.as_path_set_member:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet']['meta_info']

                @property
                def _common_path(self):

                    return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets/openconfig-bgp-policy:as-path-sets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.as_path_set is not None:
                        for child_ref in self.as_path_set:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets']['meta_info']

            @property
            def _common_path(self):

                return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets/openconfig-bgp-policy:bgp-defined-sets'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.as_path_sets is not None and self.as_path_sets._has_data():
                    return True

                if self.community_sets is not None and self.community_sets._has_data():
                    return True

                if self.ext_community_sets is not None and self.ext_community_sets._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                return meta._meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:defined-sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bgp_defined_sets is not None and self.bgp_defined_sets._has_data():
                return True

            if self.neighbor_sets is not None and self.neighbor_sets._has_data():
                return True

            if self.prefix_sets is not None and self.prefix_sets._has_data():
                return True

            if self.tag_sets is not None and self.tag_sets._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
            return meta._meta_table['RoutingPolicy.DefinedSets']['meta_info']


    class PolicyDefinitions(object):
        """
        Enclosing container for the list of top\-level policy
        definitions
        
        .. attribute:: policy_definition
        
        	List of top\-level policy definitions, keyed by unique name.  These policy definitions are expected to be referenced (by name) in policy chains specified in import or export configuration statements
        	**type**\: list of    :py:class:`PolicyDefinition <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
        
        

        """

        _prefix = 'rpol'
        _revision = '2015-10-09'

        def __init__(self):
            self.parent = None
            self.policy_definition = YList()
            self.policy_definition.parent = self
            self.policy_definition.name = 'policy_definition'


        class PolicyDefinition(object):
            """
            List of top\-level policy definitions, keyed by unique
            name.  These policy definitions are expected to be
            referenced (by name) in policy chains specified in import
            or export configuration statements.
            
            .. attribute:: name  <key>
            
            	Name of the top\-level policy definition \-\- this name  is used in references to the current policy
            	**type**\:  str
            
            .. attribute:: statements
            
            	Enclosing container for policy statements
            	**type**\:   :py:class:`Statements <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements>`
            
            

            """

            _prefix = 'rpol'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.statements = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements()
                self.statements.parent = self


            class Statements(object):
                """
                Enclosing container for policy statements
                
                .. attribute:: statement
                
                	Policy statements group conditions and actions within a policy definition.  They are evaluated in the order specified (see the description of policy evaluation at the top of this module
                	**type**\: list of    :py:class:`Statement <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement>`
                
                

                """

                _prefix = 'rpol'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.statement = YList()
                    self.statement.parent = self
                    self.statement.name = 'statement'


                class Statement(object):
                    """
                    Policy statements group conditions and actions
                    within a policy definition.  They are evaluated in
                    the order specified (see the description of policy
                    evaluation at the top of this module.
                    
                    .. attribute:: name  <key>
                    
                    	name of the policy statement
                    	**type**\:  str
                    
                    .. attribute:: actions
                    
                    	Action statements for this policy statement
                    	**type**\:   :py:class:`Actions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions>`
                    
                    .. attribute:: conditions
                    
                    	Condition statements for this policy statement
                    	**type**\:   :py:class:`Conditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions>`
                    
                    

                    """

                    _prefix = 'rpol'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions()
                        self.actions.parent = self
                        self.conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions()
                        self.conditions.parent = self


                    class Conditions(object):
                        """
                        Condition statements for this
                        policy statement
                        
                        .. attribute:: bgp_conditions
                        
                        	Policy conditions for matching BGP\-specific defined sets or comparing BGP\-specific attributes
                        	**type**\:   :py:class:`BgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions>`
                        
                        .. attribute:: call_policy
                        
                        	Applies the statements from the specified policy definition and then returns control the current policy statement. Note that the called policy may itself call other policies (subject to implementation limitations). This is intended to provide a policy 'subroutine' capability.  The called policy should contain an explicit or a default route disposition that returns an effective true (accept\-route) or false (reject\-route), otherwise the behavior may be ambiguous and implementation dependent
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition>`
                        
                        .. attribute:: igp_conditions
                        
                        	Policy conditions for IGP attributes
                        	**type**\:   :py:class:`IgpConditions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions>`
                        
                        .. attribute:: install_protocol_eq
                        
                        	Condition to check the protocol / method used to install which installed the route into the local routing table
                        	**type**\:   :py:class:`InstallProtocolTypeIdentity <ydk.models.openconfig.openconfig_policy_types.InstallProtocolTypeIdentity>`
                        
                        .. attribute:: match_neighbor_set
                        
                        	Match a referenced neighbor set according to the logic defined in the match\-set\-options\-leaf
                        	**type**\:   :py:class:`MatchNeighborSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: match_prefix_set
                        
                        	Match a referenced prefix\-set according to the logic defined in the match\-set\-options leaf
                        	**type**\:   :py:class:`MatchPrefixSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: match_tag_set
                        
                        	Match a referenced tag set according to the logic defined in the match\-options\-set leaf
                        	**type**\:   :py:class:`MatchTagSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'rpol'
                        _revision = '2015-10-09'

                        def __init__(self):
                            self.parent = None
                            self.bgp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions()
                            self.bgp_conditions.parent = self
                            self.call_policy = None
                            self.igp_conditions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions()
                            self.igp_conditions.parent = self
                            self.install_protocol_eq = None
                            self.match_neighbor_set = None
                            self.match_prefix_set = None
                            self.match_tag_set = None


                        class MatchPrefixSet(object):
                            """
                            Match a referenced prefix\-set according to the logic
                            defined in the match\-set\-options leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\:   :py:class:`MatchSetOptionsRestrictedTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedTypeEnum>`
                            
                            .. attribute:: prefix_set
                            
                            	References a defined prefix set
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`prefix_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.PrefixSets.PrefixSet>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.match_set_options = None
                                self.prefix_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-routing-policy:match-prefix-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.prefix_set is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet']['meta_info']


                        class MatchNeighborSet(object):
                            """
                            Match a referenced neighbor set according to the logic
                            defined in the match\-set\-options\-leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\:   :py:class:`MatchSetOptionsRestrictedTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedTypeEnum>`
                            
                            .. attribute:: neighbor_set
                            
                            	References a defined neighbor set
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`neighbor_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.NeighborSets.NeighborSet>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.match_set_options = None
                                self.neighbor_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-routing-policy:match-neighbor-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.neighbor_set is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet']['meta_info']


                        class MatchTagSet(object):
                            """
                            Match a referenced tag set according to the logic defined
                            in the match\-options\-set leaf
                            
                            .. attribute:: match_set_options
                            
                            	Optional parameter that governs the behaviour of the match operation.  This leaf only supports matching on ANY member of the set or inverting the match.  Matching on ALL is not supported)
                            	**type**\:   :py:class:`MatchSetOptionsRestrictedTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsRestrictedTypeEnum>`
                            
                            .. attribute:: tag_set
                            
                            	References a defined tag set
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`tag_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.TagSets.TagSet>`
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'rpol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.match_set_options = None
                                self.tag_set = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-routing-policy:match-tag-set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.match_set_options is not None:
                                    return True

                                if self.tag_set is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet']['meta_info']


                        class IgpConditions(object):
                            """
                            Policy conditions for IGP attributes
                            
                            

                            """

                            _prefix = 'rpol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-routing-policy:igp-conditions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions']['meta_info']


                        class BgpConditions(object):
                            """
                            Policy conditions for matching
                            BGP\-specific defined sets or comparing BGP\-specific
                            attributes
                            
                            .. attribute:: afi_safi_in
                            
                            	List of address families which the NLRI may be within
                            	**type**\:  
                            		list of  
                            
                            .. attribute:: as_path_length
                            
                            	Value and comparison operations for conditions based on the length of the AS path in the route update
                            	**type**\:   :py:class:`AsPathLength <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: community_count
                            
                            	Value and comparison operations for conditions based on the number of communities in the route update
                            	**type**\:   :py:class:`CommunityCount <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: local_pref_eq
                            
                            	Condition to check if the local pref attribute is equal to the specified value
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: match_as_path_set
                            
                            	Match a referenced as\-path set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchAsPathSet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: match_community_set
                            
                            	Match a referenced community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: match_ext_community_set
                            
                            	Match a referenced extended community\-set according to the logic defined in the match\-set\-options leaf
                            	**type**\:   :py:class:`MatchExtCommunitySet <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet>`
                            
                            	**presence node**\: True
                            
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
                            	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                            
                            .. attribute:: route_type
                            
                            	Condition to check the route type in the route update
                            	**type**\:   :py:class:`RouteTypeEnum <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.RouteTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp-pol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self.afi_safi_in = YLeafList()
                                self.afi_safi_in.parent = self
                                self.afi_safi_in.name = 'afi_safi_in'
                                self.as_path_length = None
                                self.community_count = None
                                self.local_pref_eq = None
                                self.match_as_path_set = None
                                self.match_community_set = None
                                self.match_ext_community_set = None
                                self.med_eq = None
                                self.next_hop_in = YLeafList()
                                self.next_hop_in.parent = self
                                self.next_hop_in.name = 'next_hop_in'
                                self.origin_eq = None
                                self.route_type = None

                            class RouteTypeEnum(Enum):
                                """
                                RouteTypeEnum

                                Condition to check the route type in the route update

                                .. data:: INTERNAL = 0

                                	route type is internal

                                .. data:: EXTERNAL = 1

                                	route type is external

                                """

                                INTERNAL = 0

                                EXTERNAL = 1


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.RouteTypeEnum']



                            class MatchCommunitySet(object):
                                """
                                Match a referenced community\-set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: community_set
                                
                                	References a defined community set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation
                                	**type**\:   :py:class:`MatchSetOptionsTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsTypeEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.community_set = None
                                    self.match_set_options = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:match-community-set'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.community_set is not None:
                                        return True

                                    if self.match_set_options is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet']['meta_info']


                            class MatchExtCommunitySet(object):
                                """
                                Match a referenced extended community\-set according to the
                                logic defined in the match\-set\-options leaf
                                
                                .. attribute:: ext_community_set
                                
                                	References a defined extended community set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation
                                	**type**\:   :py:class:`MatchSetOptionsTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsTypeEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.ext_community_set = None
                                    self.match_set_options = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:match-ext-community-set'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.ext_community_set is not None:
                                        return True

                                    if self.match_set_options is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet']['meta_info']


                            class MatchAsPathSet(object):
                                """
                                Match a referenced as\-path set according to the logic
                                defined in the match\-set\-options leaf
                                
                                .. attribute:: as_path_set
                                
                                	References a defined AS path set
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`as_path_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet>`
                                
                                .. attribute:: match_set_options
                                
                                	Optional parameter that governs the behaviour of the match operation
                                	**type**\:   :py:class:`MatchSetOptionsTypeEnum <ydk.models.openconfig.openconfig_policy_types.MatchSetOptionsTypeEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.as_path_set = None
                                    self.match_set_options = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:match-as-path-set'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.as_path_set is not None:
                                        return True

                                    if self.match_set_options is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet']['meta_info']


                            class CommunityCount(object):
                                """
                                Value and comparison operations for conditions based on the
                                number of communities in the route update
                                
                                .. attribute:: operator
                                
                                	type of comparison to be performed
                                	**type**\:   :py:class:`AttributeComparisonIdentity <ydk.models.openconfig.openconfig_policy_types.AttributeComparisonIdentity>`
                                
                                .. attribute:: value
                                
                                	value to compare with the community count
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.operator = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:community-count'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.operator is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount']['meta_info']


                            class AsPathLength(object):
                                """
                                Value and comparison operations for conditions based on the
                                length of the AS path in the route update
                                
                                .. attribute:: operator
                                
                                	type of comparison to be performed
                                	**type**\:   :py:class:`AttributeComparisonIdentity <ydk.models.openconfig.openconfig_policy_types.AttributeComparisonIdentity>`
                                
                                .. attribute:: value
                                
                                	value to compare with the community count
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.operator = None
                                    self.value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:as-path-length'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.operator is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-bgp-policy:bgp-conditions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.afi_safi_in is not None:
                                    for child_ref in self.afi_safi_in:
                                        if child_ref._has_data():
                                            return True

                                if self.as_path_length is not None and self.as_path_length._has_data():
                                    return True

                                if self.community_count is not None and self.community_count._has_data():
                                    return True

                                if self.local_pref_eq is not None:
                                    return True

                                if self.match_as_path_set is not None and self.match_as_path_set._has_data():
                                    return True

                                if self.match_community_set is not None and self.match_community_set._has_data():
                                    return True

                                if self.match_ext_community_set is not None and self.match_ext_community_set._has_data():
                                    return True

                                if self.med_eq is not None:
                                    return True

                                if self.next_hop_in is not None:
                                    for child in self.next_hop_in:
                                        if child is not None:
                                            return True

                                if self.origin_eq is not None:
                                    return True

                                if self.route_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-routing-policy:conditions'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.bgp_conditions is not None and self.bgp_conditions._has_data():
                                return True

                            if self.call_policy is not None:
                                return True

                            if self.igp_conditions is not None and self.igp_conditions._has_data():
                                return True

                            if self.install_protocol_eq is not None:
                                return True

                            if self.match_neighbor_set is not None and self.match_neighbor_set._has_data():
                                return True

                            if self.match_prefix_set is not None and self.match_prefix_set._has_data():
                                return True

                            if self.match_tag_set is not None and self.match_tag_set._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                            return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']


                    class Actions(object):
                        """
                        Action statements for this policy
                        statement
                        
                        .. attribute:: accept_route
                        
                        	accepts the route into the routing table
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bgp_actions
                        
                        	Definitions for policy action statements that change BGP\-specific attributes of the route
                        	**type**\:   :py:class:`BgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions>`
                        
                        .. attribute:: igp_actions
                        
                        	Actions to set IGP route attributes; these actions apply to multiple IGPs
                        	**type**\:   :py:class:`IgpActions <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions>`
                        
                        .. attribute:: reject_route
                        
                        	rejects the route
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'rpol'
                        _revision = '2015-10-09'

                        def __init__(self):
                            self.parent = None
                            self.accept_route = None
                            self.bgp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions()
                            self.bgp_actions.parent = self
                            self.igp_actions = RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions()
                            self.igp_actions.parent = self
                            self.reject_route = None


                        class IgpActions(object):
                            """
                            Actions to set IGP route attributes; these actions
                            apply to multiple IGPs
                            
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

                            _prefix = 'rpol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self.set_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-routing-policy:igp-actions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.set_tag is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions']['meta_info']


                        class BgpActions(object):
                            """
                            Definitions for policy action statements that
                            change BGP\-specific attributes of the route
                            
                            .. attribute:: set_as_path_prepend
                            
                            	action to prepend local AS number to the AS\-path a specified number of times
                            	**type**\:   :py:class:`SetAsPathPrepend <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: set_community
                            
                            	action to set the community attributes of the route, along with options to modify how the community is modified
                            	**type**\:   :py:class:`SetCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: set_ext_community
                            
                            	Action to set the extended community attributes of the route, along with options to modify how the community is modified
                            	**type**\:   :py:class:`SetExtCommunity <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity>`
                            
                            	**presence node**\: True
                            
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
                            	**type**\:   :py:class:`BgpSetMedTypeEnum <ydk.models.openconfig.openconfig_bgp_policy.BgpSetMedTypeEnum>`
                            
                            
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
                            	**type**\:   :py:class:`BgpNextHopTypeEnum <ydk.models.openconfig.openconfig_bgp_policy.BgpNextHopTypeEnum>`
                            
                            
                            ----
                            .. attribute:: set_route_origin
                            
                            	set the origin attribute to the specified value
                            	**type**\:   :py:class:`BgpOriginAttrTypeEnum <ydk.models.openconfig.openconfig_bgp_types.BgpOriginAttrTypeEnum>`
                            
                            

                            """

                            _prefix = 'bgp-pol'
                            _revision = '2015-10-09'

                            def __init__(self):
                                self.parent = None
                                self.set_as_path_prepend = None
                                self.set_community = None
                                self.set_ext_community = None
                                self.set_local_pref = None
                                self.set_med = None
                                self.set_next_hop = None
                                self.set_route_origin = None


                            class SetAsPathPrepend(object):
                                """
                                action to prepend local AS number to the AS\-path a
                                specified number of times
                                
                                .. attribute:: repeat_n
                                
                                	number of times to prepend the local AS number
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.repeat_n = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:set-as-path-prepend'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.repeat_n is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend']['meta_info']


                            class SetCommunity(object):
                                """
                                action to set the community attributes of the route, along
                                with options to modify how the community is modified
                                
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
                                .. attribute:: community_set_ref
                                
                                	References a defined community set by name
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet>`
                                
                                .. attribute:: options
                                
                                	Options for modifying the community attribute with the specified values.  These options apply to both methods of setting the community attribute
                                	**type**\:   :py:class:`BgpSetCommunityOptionTypeEnum <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionTypeEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.communities = YLeafList()
                                    self.communities.parent = self
                                    self.communities.name = 'communities'
                                    self.community_set_ref = None
                                    self.options = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:set-community'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.communities is not None:
                                        for child in self.communities:
                                            if child is not None:
                                                return True

                                    if self.community_set_ref is not None:
                                        return True

                                    if self.options is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity']['meta_info']


                            class SetExtCommunity(object):
                                """
                                Action to set the extended community attributes of the
                                route, along with options to modify how the community is
                                modified
                                
                                .. attribute:: communities
                                
                                	Set the community values for the update inline with a list
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
                                .. attribute:: ext_community_set_ref
                                
                                	References a defined extended community set by name
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`ext_community_set_name <ydk.models.openconfig.openconfig_routing_policy.RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet>`
                                
                                .. attribute:: options
                                
                                	options for modifying the extended community attribute with the specified values. These options apply to both methods of setting the community attribute
                                	**type**\:   :py:class:`BgpSetCommunityOptionTypeEnum <ydk.models.openconfig.openconfig_bgp_policy.BgpSetCommunityOptionTypeEnum>`
                                
                                .. attribute:: _is_presence
                                
                                	Is present if this instance represents presence container else not
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'bgp-pol'
                                _revision = '2015-10-09'

                                def __init__(self):
                                    self.parent = None
                                    self._is_presence = True
                                    self.communities = YLeafList()
                                    self.communities.parent = self
                                    self.communities.name = 'communities'
                                    self.ext_community_set_ref = None
                                    self.options = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-bgp-policy:set-ext-community'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self._is_presence:
                                        return True
                                    if self.communities is not None:
                                        for child in self.communities:
                                            if child is not None:
                                                return True

                                    if self.ext_community_set_ref is not None:
                                        return True

                                    if self.options is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-bgp-policy:bgp-actions'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.set_as_path_prepend is not None and self.set_as_path_prepend._has_data():
                                    return True

                                if self.set_community is not None and self.set_community._has_data():
                                    return True

                                if self.set_ext_community is not None and self.set_ext_community._has_data():
                                    return True

                                if self.set_local_pref is not None:
                                    return True

                                if self.set_med is not None:
                                    return True

                                if self.set_next_hop is not None:
                                    return True

                                if self.set_route_origin is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-routing-policy:actions'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.accept_route is not None:
                                return True

                            if self.bgp_actions is not None and self.bgp_actions._has_data():
                                return True

                            if self.igp_actions is not None and self.igp_actions._has_data():
                                return True

                            if self.reject_route is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                            return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/openconfig-routing-policy:statement[openconfig-routing-policy:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.actions is not None and self.actions._has_data():
                            return True

                        if self.conditions is not None and self.conditions._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                        return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-routing-policy:statements'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.statement is not None:
                        for child_ref in self.statement:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                    return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:policy-definitions/openconfig-routing-policy:policy-definition[openconfig-routing-policy:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.statements is not None and self.statements._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
                return meta._meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info']

        @property
        def _common_path(self):

            return '/openconfig-routing-policy:routing-policy/openconfig-routing-policy:policy-definitions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.policy_definition is not None:
                for child_ref in self.policy_definition:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
            return meta._meta_table['RoutingPolicy.PolicyDefinitions']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-routing-policy:routing-policy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.defined_sets is not None and self.defined_sets._has_data():
            return True

        if self.policy_definitions is not None and self.policy_definitions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_routing_policy as meta
        return meta._meta_table['RoutingPolicy']['meta_info']


